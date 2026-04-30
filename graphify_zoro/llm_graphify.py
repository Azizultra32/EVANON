from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

from graphify_zoro.config import get_settings
from graphify_zoro.graphify_analyze import _write_outputs


OPENAI_RESPONSES_URL = "https://api.openai.com/v1/responses"
DEFAULT_MODEL = "gpt-5.5"
DEFAULT_REASONING_EFFORT = "xhigh"
DEFAULT_MAX_OUTPUT_TOKENS = 30_000
PROMPT_VERSION = "zoro-llm-graph-v2-responses"


GRAPH_FRAGMENT_FORMAT = {
    "type": "json_schema",
    "name": "graph_fragment",
    "strict": True,
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "nodes": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "string"},
                        "label": {"type": "string"},
                        "file_type": {"type": "string"},
                        "source_file": {"type": "string"},
                        "source_location": {"type": ["string", "null"]},
                        "source_url": {"type": ["string", "null"]},
                        "captured_at": {"type": ["string", "null"]},
                        "author": {"type": ["string", "null"]},
                        "contributor": {"type": ["string", "null"]},
                    },
                    "required": [
                        "id",
                        "label",
                        "file_type",
                        "source_file",
                        "source_location",
                        "source_url",
                        "captured_at",
                        "author",
                        "contributor",
                    ],
                },
            },
            "edges": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "source": {"type": "string"},
                        "target": {"type": "string"},
                        "relation": {"type": "string"},
                        "confidence": {"type": "string", "enum": ["EXTRACTED", "INFERRED", "AMBIGUOUS"]},
                        "confidence_score": {"type": "number"},
                        "source_file": {"type": "string"},
                        "source_location": {"type": ["string", "null"]},
                        "weight": {"type": "number"},
                    },
                    "required": [
                        "source",
                        "target",
                        "relation",
                        "confidence",
                        "confidence_score",
                        "source_file",
                        "source_location",
                        "weight",
                    ],
                },
            },
            "hyperedges": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "string"},
                        "label": {"type": "string"},
                        "nodes": {"type": "array", "items": {"type": "string"}},
                        "relation": {"type": "string"},
                        "confidence": {"type": "string", "enum": ["EXTRACTED", "INFERRED"]},
                        "confidence_score": {"type": "number"},
                        "source_file": {"type": "string"},
                    },
                    "required": [
                        "id",
                        "label",
                        "nodes",
                        "relation",
                        "confidence",
                        "confidence_score",
                        "source_file",
                    ],
                },
            },
        },
        "required": ["nodes", "edges", "hyperedges"],
    },
}


@dataclass(frozen=True)
class Chunk:
    source_path: Path
    source_file: str
    title: str
    index: int
    total: int
    text: str


def _load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def _api_key() -> str:
    settings = get_settings()
    _load_env_file(settings.project_root / ".env")
    _load_env_file(Path("/Users/ali/COGNEE-zoroastrianism/.env"))
    key = os.environ.get("OPENAI_API_KEY") or os.environ.get("LLM_API_KEY")
    if not key:
        raise SystemExit("No OpenAI API key found in OPENAI_API_KEY or LLM_API_KEY.")
    return key


def _slug(value: str, prefix: str = "llm_") -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    if not slug:
        slug = hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}{slug}"


def _source_file(project_root: Path, path: Path) -> str:
    real = path.resolve()
    try:
        return str(real.relative_to(project_root))
    except ValueError:
        return str(path)


def _title(text: str, path: Path) -> str:
    for line in text.splitlines()[:120]:
        match = re.match(r"^\s{0,3}#{1,4}\s+(.+?)\s*$", line)
        if match:
            title = re.sub(r"\s+", " ", match.group(1)).strip(" #")
            if 5 <= len(title) <= 180:
                return title
    return path.stem.replace("_", " ").replace("-", " ").strip()


def _important_headings(text: str, max_chars: int = 4000) -> str:
    headings = []
    for line in text.splitlines():
        if re.match(r"^\s{0,3}#{1,4}\s+", line):
            clean = re.sub(r"\s+", " ", line.strip())
            if len(clean) > 5:
                headings.append(clean)
    joined = "\n".join(headings[:100])
    return joined[:max_chars]


def _split_text(text: str, max_chars: int) -> list[str]:
    text = text.strip()
    if len(text) <= max_chars:
        return [text]

    headings = _important_headings(text)
    excerpt_chars = max(4000, max_chars - len(headings) - 300)
    pieces = []
    thirds = [0, max(0, len(text) // 2 - excerpt_chars // 2), max(0, len(text) - excerpt_chars)]
    seen: set[int] = set()
    for start in thirds:
        if start in seen:
            continue
        seen.add(start)
        body = text[start : start + excerpt_chars]
        pieces.append(f"Important headings:\n{headings}\n\nExcerpt:\n{body}" if headings else body)
    return pieces


def _chunks(input_dir: Path, project_root: Path, max_chars: int) -> list[Chunk]:
    chunks: list[Chunk] = []
    for path in sorted(input_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        title = _title(text, path)
        source_file = _source_file(project_root, path)
        parts = _split_text(text, max_chars)
        for idx, part in enumerate(parts, start=1):
            chunks.append(
                Chunk(
                    source_path=path,
                    source_file=source_file,
                    title=title,
                    index=idx,
                    total=len(parts),
                    text=part,
                )
            )
    return chunks


def _prompt(chunk: Chunk) -> list[dict]:
    system = (
        "You are Graphify's semantic extraction pass for a scholarly OCR corpus. "
        "Extract a useful knowledge graph fragment. Return only JSON."
    )
    user = f"""
Source file: {chunk.source_file}
Document title: {chunk.title}
Chunk: {chunk.index} of {chunk.total}

Extract:
- important entities, concepts, texts, historical persons, traditions, rituals, places, and arguments
- explicit citations or references when visible
- inferred relationships only when the text supports them
- rationale nodes for claims, debates, or interpretive arguments

Rules:
- Prefer specific scholarly concepts over generic words.
- Do not include OCR junk, page furniture, navigation text, or bibliography-only noise unless it is substantively important.
- Use EXTRACTED for explicit relationships in the text.
- Use INFERRED for reasonable conceptual relationships grounded in the text.
- Use AMBIGUOUS for uncertain OCR readings or uncertain interpretations.
- Keep output compact: max 12 nodes, max 18 edges, max 2 hyperedges.
- IDs should be snake_case and stable.
- source_file must be exactly: {chunk.source_file}

Output exactly this JSON object:
{{
  "nodes": [
    {{
      "id": "snake_case_id",
      "label": "Human Readable Name",
      "file_type": "document",
      "source_file": "{chunk.source_file}",
      "source_location": "chunk {chunk.index}/{chunk.total}",
      "source_url": null,
      "captured_at": null,
      "author": null,
      "contributor": null
    }}
  ],
  "edges": [
    {{
      "source": "source_node_id",
      "target": "target_node_id",
      "relation": "references|cites|conceptually_related_to|semantically_similar_to|rationale_for|participates_in|contrasts_with",
      "confidence": "EXTRACTED|INFERRED|AMBIGUOUS",
      "confidence_score": 1.0,
      "source_file": "{chunk.source_file}",
      "source_location": "chunk {chunk.index}/{chunk.total}",
      "weight": 1.0
    }}
  ],
  "hyperedges": [
    {{
      "id": "snake_case_id",
      "label": "Human Readable Label",
      "nodes": ["node_id_1", "node_id_2", "node_id_3"],
      "relation": "form|participate_in|debate",
      "confidence": "EXTRACTED|INFERRED",
      "confidence_score": 0.75,
      "source_file": "{chunk.source_file}"
    }}
  ]
}}

Text:
{chunk.text}
""".strip()
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def _cache_key(chunk: Chunk, model: str, reasoning_effort: str, max_output_tokens: int) -> str:
    payload = "\n".join(
        [
            PROMPT_VERSION,
            model,
            reasoning_effort,
            str(max_output_tokens),
            chunk.source_file,
            str(chunk.index),
            chunk.text,
        ]
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _extract_response_text(data: dict) -> str:
    texts: list[str] = []
    for item in data.get("output", []):
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                texts.append(str(content.get("text") or ""))
            elif content.get("type") == "refusal":
                raise RuntimeError(f"OpenAI refusal: {content.get('refusal')}")
    text = "\n".join(texts).strip()
    if not text:
        raise RuntimeError("OpenAI response did not include output_text.")
    return text


def _call_openai(key: str, model: str, reasoning_effort: str, max_output_tokens: int, chunk: Chunk, timeout: int) -> dict:
    body = {
        "model": model,
        "input": _prompt(chunk),
        "reasoning": {"effort": reasoning_effort},
        "max_output_tokens": max_output_tokens,
        "text": {"format": GRAPH_FRAGMENT_FORMAT},
        "store": False,
    }
    encoded_body = json.dumps(body).encode("utf-8")
    last_error: Exception | None = None
    for attempt in range(1, 4):
        request = urllib.request.Request(
            OPENAI_RESPONSES_URL,
            data=encoded_body,
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="ignore")
            last_error = RuntimeError(f"OpenAI HTTP {exc.code}: {detail[:1000]}")
            if exc.code not in {429, 500, 502, 503, 504} or attempt == 3:
                raise last_error from exc
            time.sleep(2**attempt)
        except urllib.error.URLError as exc:
            last_error = RuntimeError(f"OpenAI request failed: {exc}")
            if attempt == 3:
                raise last_error from exc
            time.sleep(2**attempt)
    else:
        raise RuntimeError(f"OpenAI request failed: {last_error}")
    if data.get("status") != "completed":
        raise RuntimeError(f"OpenAI response status={data.get('status')} details={data.get('incomplete_details') or data.get('error')}")
    parsed = json.loads(_extract_response_text(data))
    parsed["_usage"] = data.get("usage", {})
    return parsed


def _normalize_fragment(fragment: dict, chunk: Chunk) -> dict:
    raw_nodes = fragment.get("nodes", [])
    raw_edges = fragment.get("edges", [])
    raw_hyperedges = fragment.get("hyperedges", [])
    id_map: dict[str, str] = {}
    nodes: list[dict] = []

    doc_id = _slug(f"document:{chunk.source_file}", "doc_")
    nodes.append(
        {
            "id": doc_id,
            "label": chunk.title,
            "file_type": "document",
            "source_file": chunk.source_file,
            "source_location": None,
            "source_url": None,
            "captured_at": None,
            "author": None,
            "contributor": None,
        }
    )

    for node in raw_nodes:
        label = str(node.get("label") or node.get("id") or "").strip()
        if not label or len(label) < 3:
            continue
        old_id = str(node.get("id") or label)
        node_id = _slug(label, "llm_")
        id_map[old_id] = node_id
        nodes.append(
            {
                "id": node_id,
                "label": label[:180],
                "file_type": "document",
                "source_file": chunk.source_file,
                "source_location": node.get("source_location") or f"chunk {chunk.index}/{chunk.total}",
                "source_url": node.get("source_url"),
                "captured_at": node.get("captured_at"),
                "author": node.get("author"),
                "contributor": node.get("contributor"),
            }
        )

    edges = []
    node_ids = {node["id"] for node in nodes}
    for node_id in sorted(node_ids - {doc_id}):
        edges.append(_edge(doc_id, node_id, "references", "EXTRACTED", 1.0, chunk.source_file, f"chunk {chunk.index}/{chunk.total}", 1.0))

    for edge in raw_edges:
        source = id_map.get(str(edge.get("source")), _slug(str(edge.get("source")), "llm_"))
        target = id_map.get(str(edge.get("target")), _slug(str(edge.get("target")), "llm_"))
        if source not in node_ids or target not in node_ids or source == target:
            continue
        confidence = str(edge.get("confidence") or "INFERRED").upper()
        if confidence not in {"EXTRACTED", "INFERRED", "AMBIGUOUS"}:
            confidence = "INFERRED"
        try:
            score = float(edge.get("confidence_score", 0.7))
        except Exception:
            score = 0.7
        relation = str(edge.get("relation") or "conceptually_related_to")
        edges.append(_edge(source, target, relation, confidence, score, chunk.source_file, edge.get("source_location") or f"chunk {chunk.index}/{chunk.total}", float(edge.get("weight") or 1.0)))

    hyperedges = []
    for hyperedge in raw_hyperedges:
        ids = [id_map.get(str(n), _slug(str(n), "llm_")) for n in hyperedge.get("nodes", [])]
        ids = [n for n in ids if n in node_ids]
        if len(set(ids)) < 3:
            continue
        hyperedges.append(
            {
                "id": _slug(str(hyperedge.get("label") or hyperedge.get("id") or "group"), "hyper_"),
                "label": str(hyperedge.get("label") or "Group")[:160],
                "nodes": sorted(set(ids)),
                "relation": str(hyperedge.get("relation") or "form"),
                "confidence": str(hyperedge.get("confidence") or "INFERRED").upper(),
                "confidence_score": float(hyperedge.get("confidence_score") or 0.75),
                "source_file": chunk.source_file,
            }
        )

    return {"nodes": nodes, "edges": edges, "hyperedges": hyperedges, "usage": fragment.get("_usage", {})}


def _edge(source: str, target: str, relation: str, confidence: str, score: float, source_file: str, source_location: str | None, weight: float) -> dict:
    return {
        "source": source,
        "target": target,
        "relation": relation,
        "confidence": confidence,
        "confidence_score": max(0.0, min(1.0, round(score, 2))),
        "source_file": source_file,
        "source_location": source_location,
        "weight": round(weight, 3),
    }


def _merge(fragments: list[dict]) -> dict:
    nodes_by_id: dict[str, dict] = {}
    edges_by_key: dict[tuple, dict] = {}
    hyperedges_by_id: dict[str, dict] = {}
    input_tokens = 0
    output_tokens = 0

    for fragment in fragments:
        usage = fragment.get("usage") or {}
        input_tokens += int(usage.get("prompt_tokens") or usage.get("input_tokens") or 0)
        output_tokens += int(usage.get("completion_tokens") or usage.get("output_tokens") or 0)
        for node in fragment.get("nodes", []):
            nodes_by_id.setdefault(node["id"], node)
        for edge in fragment.get("edges", []):
            key = (edge["source"], edge["target"], edge["relation"], edge.get("source_file"), edge.get("source_location"))
            edges_by_key.setdefault(key, edge)
        for hyperedge in fragment.get("hyperedges", []):
            hyperedges_by_id.setdefault(hyperedge["id"], hyperedge)

    return {
        "nodes": list(nodes_by_id.values()),
        "edges": list(edges_by_key.values()),
        "hyperedges": list(hyperedges_by_id.values()),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
    }


def _write_non_llm_pass_artifacts(detection: dict, out_dir: Path) -> None:
    """Write explicit Graphify pass artifacts for layers that are deterministic or no-op."""
    from graphify.extract import collect_files, extract

    Path(".graphify_detect.json").write_text(json.dumps(detection, indent=2), encoding="utf-8")
    (out_dir / ".graphify_detect.json").write_text(json.dumps(detection, indent=2), encoding="utf-8")

    code_files = []
    for filename in detection.get("files", {}).get("code", []):
        path = Path(filename)
        code_files.extend(collect_files(path) if path.is_dir() else [path])
    if code_files:
        ast = extract(code_files)
    else:
        ast = {
            "nodes": [],
            "edges": [],
            "input_tokens": 0,
            "output_tokens": 0,
            "skipped": "no code files detected in this corpus",
        }
    Path(".graphify_ast.json").write_text(json.dumps(ast, indent=2), encoding="utf-8")
    (out_dir / ".graphify_ast.json").write_text(json.dumps(ast, indent=2), encoding="utf-8")

    video_files = detection.get("files", {}).get("video", [])
    if video_files:
        from graphify.transcribe import transcribe_all

        transcripts = transcribe_all(video_files)
        pass2 = {"input_files": video_files, "transcripts": transcripts}
    else:
        pass2 = {"input_files": [], "transcripts": [], "skipped": "no video or audio files detected"}
    Path(".graphify_transcripts.json").write_text(json.dumps(pass2, indent=2), encoding="utf-8")
    (out_dir / ".graphify_transcripts.json").write_text(json.dumps(pass2, indent=2), encoding="utf-8")


def _load_or_extract_chunk(
    index: int,
    total: int,
    chunk: Chunk,
    key: str,
    model: str,
    reasoning_effort: str,
    max_output_tokens: int,
    timeout: int,
    cache_dir: Path,
    force: bool,
) -> tuple[int, dict | None, dict | None, str]:
    key_hash = _cache_key(chunk, model, reasoning_effort, max_output_tokens)
    cache_path = cache_dir / f"{key_hash}.json"
    label = f"{chunk.source_file} chunk {chunk.index}/{chunk.total}"
    if cache_path.exists() and not force:
        fragment = json.loads(cache_path.read_text(encoding="utf-8"))
        return index, fragment, None, f"[{index}/{total}] cache {label}"

    try:
        raw = _call_openai(key, model, reasoning_effort, max_output_tokens, chunk, timeout)
        fragment = _normalize_fragment(raw, chunk)
        cache_path.write_text(json.dumps(fragment, indent=2), encoding="utf-8")
        return index, fragment, None, f"[{index}/{total}] llm ok {label}"
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError, RuntimeError) as exc:
        detail = str(exc)
        if isinstance(exc, urllib.error.HTTPError):
            try:
                detail = exc.read().decode("utf-8", errors="ignore")
            except Exception:
                detail = str(exc)
        failure = {"source_file": chunk.source_file, "chunk": chunk.index, "error": detail[:1000]}
        return index, None, failure, f"[{index}/{total}] failed {label}: {detail[:300]}"


def main() -> None:
    parser = argparse.ArgumentParser(prog="graphify-zoro-llm")
    parser.add_argument("--input", type=Path, default=Path("graphify-input/ocr-markdown"))
    parser.add_argument("--model", default=None)
    parser.add_argument("--reasoning-effort", choices=["none", "minimal", "low", "medium", "high", "xhigh"], default=None)
    parser.add_argument("--max-output-tokens", type=int, default=None)
    parser.add_argument("--max-chars", type=int, default=22_000)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--smoke-test", action="store_true", help="Call the model for one chunk and exit without writing graph outputs.")
    args = parser.parse_args()

    settings = get_settings()
    project_root = settings.project_root
    input_path = args.input if args.input.is_absolute() else project_root / args.input
    key = _api_key()
    model = args.model or os.environ.get("LLM_MODEL") or DEFAULT_MODEL
    reasoning_effort = args.reasoning_effort or os.environ.get("LLM_REASONING_EFFORT") or DEFAULT_REASONING_EFFORT
    max_output_tokens = args.max_output_tokens or int(os.environ.get("LLM_MAX_OUTPUT_TOKENS") or DEFAULT_MAX_OUTPUT_TOKENS)
    chunks = _chunks(input_path, project_root, args.max_chars)
    if args.limit is not None:
        chunks = chunks[: args.limit]
    if not chunks:
        raise SystemExit(f"No Markdown chunks found in {input_path}")

    if args.smoke_test:
        chunk = chunks[0]
        print(f"Smoke test: model={model}, reasoning_effort={reasoning_effort}, max_output_tokens={max_output_tokens}")
        raw = _call_openai(key, model, reasoning_effort, max_output_tokens, chunk, args.timeout)
        fragment = _normalize_fragment(raw, chunk)
        print(
            json.dumps(
                {
                    "source_file": chunk.source_file,
                    "nodes": len(fragment.get("nodes", [])),
                    "edges": len(fragment.get("edges", [])),
                    "hyperedges": len(fragment.get("hyperedges", [])),
                    "usage": fragment.get("usage", {}),
                },
                indent=2,
            )
        )
        return

    cache_dir = settings.graphify_out_dir / "llm-cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    fragments: list[dict] = []
    failures: list[dict] = []

    workers = max(1, min(args.workers, 8))
    print(
        f"LLM extraction: {len(chunks)} chunk(s), model={model}, "
        f"reasoning_effort={reasoning_effort}, max_output_tokens={max_output_tokens}, workers={workers}"
    )
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(
                _load_or_extract_chunk,
                index,
                len(chunks),
                chunk,
                key,
                model,
                reasoning_effort,
                max_output_tokens,
                args.timeout,
                cache_dir,
                args.force,
            )
            for index, chunk in enumerate(chunks, start=1)
        ]
        results = []
        for future in as_completed(futures):
            index, fragment, failure, message = future.result()
            print(message)
            results.append((index, fragment, failure))

    for _, fragment, failure in sorted(results, key=lambda item: item[0]):
        if fragment is not None:
            fragments.append(fragment)
        if failure is not None:
            failures.append(failure)

    extraction = _merge(fragments)
    extraction.update(
        {
            "model": model,
            "reasoning_effort": reasoning_effort,
            "max_output_tokens": max_output_tokens,
            "prompt_version": PROMPT_VERSION,
            "chunks_total": len(chunks),
            "chunks_succeeded": len(fragments),
            "chunks_failed": len(failures),
        }
    )
    if not fragments:
        if failures:
            (settings.graphify_out_dir / "llm-failures.json").write_text(json.dumps(failures, indent=2), encoding="utf-8")
        raise SystemExit("LLM extraction produced no successful chunks; existing graph was left unchanged.")

    Path(".graphify_semantic_llm.json").write_text(json.dumps(extraction, indent=2), encoding="utf-8")
    Path(".graphify_semantic.json").write_text(json.dumps(extraction, indent=2), encoding="utf-8")
    Path(".graphify_extract.json").write_text(json.dumps(extraction, indent=2), encoding="utf-8")
    (settings.graphify_out_dir / ".graphify_semantic_llm.json").write_text(json.dumps(extraction, indent=2), encoding="utf-8")
    (settings.graphify_out_dir / ".graphify_extract.json").write_text(json.dumps(extraction, indent=2), encoding="utf-8")
    if failures:
        (settings.graphify_out_dir / "llm-failures.json").write_text(json.dumps(failures, indent=2), encoding="utf-8")
    else:
        (settings.graphify_out_dir / "llm-failures.json").unlink(missing_ok=True)

    from graphify.detect import detect

    detection = detect(input_path)
    _write_non_llm_pass_artifacts(detection, settings.graphify_out_dir)
    _write_outputs(extraction, detection, str(input_path), settings.graphify_out_dir)
    print(
        json.dumps(
            {
                "chunks_total": len(chunks),
                "chunks_succeeded": len(fragments),
                "chunks_failed": len(failures),
                "input_tokens": extraction.get("input_tokens", 0),
                "output_tokens": extraction.get("output_tokens", 0),
                "semantic_file": ".graphify_semantic_llm.json",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
