from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import networkx as nx
from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.detect import detect
from graphify.export import to_canvas, to_graphml, to_html, to_json, to_obsidian, to_svg
from graphify.report import generate

from graphify_zoro.config import get_settings


DOMAIN_TERMS = [
    "Ahura Mazda",
    "Auramazda",
    "Angra Mainyu",
    "Ahriman",
    "Amesha Spenta",
    "Anahita",
    "Asha",
    "Arta",
    "Atar",
    "Avesta",
    "Avestan",
    "Denkard",
    "Druj",
    "Fravashi",
    "Gathas",
    "Haoma",
    "Khvarenah",
    "Mithra",
    "Mithras",
    "Mithraism",
    "Mitra",
    "Pahlavi",
    "Sasanian",
    "Sassanian",
    "Vendidad",
    "Visperad",
    "Vohu Manah",
    "Xvarenah",
    "Yasht",
    "Yasna",
    "Yazata",
    "Zarathustra",
    "Zoroaster",
    "Zoroastrian",
    "Zoroastrianism",
    "Zurvan",
    "Achaemenid",
    "Cyrus",
    "Darius",
    "Iranian",
    "Persian",
    "Indo-Iranian",
    "Vedic",
    "Eschatology",
    "Monotheism",
    "Dualism",
    "Kingship",
    "Cosmology",
    "Creation",
    "Judgment",
    "Resurrection",
    "Ritual purity",
    "Pollution",
    "Fire temple",
    "Sacrifice",
    "Covenant",
    "Chinvat Bridge",
    "Magi",
    "Manichaeism",
    "Mithraic",
]

SYNONYMS = {
    "auramazda": "Ahura Mazda",
    "ahura mazda": "Ahura Mazda",
    "ahriman": "Angra Mainyu / Ahriman",
    "angra mainyu": "Angra Mainyu / Ahriman",
    "mithra": "Mithra / Mithras / Mitra",
    "mithras": "Mithra / Mithras / Mitra",
    "mitra": "Mithra / Mithras / Mitra",
    "zarathustra": "Zarathustra / Zoroaster",
    "zoroaster": "Zarathustra / Zoroaster",
    "khvarenah": "Khvarenah / Xvarenah",
    "xvarenah": "Khvarenah / Xvarenah",
    "sassanian": "Sasanian",
}

STOPWORDS = {
    "about",
    "after",
    "also",
    "among",
    "ancient",
    "another",
    "because",
    "been",
    "before",
    "being",
    "between",
    "both",
    "chapter",
    "could",
    "during",
    "early",
    "from",
    "have",
    "into",
    "later",
    "many",
    "more",
    "most",
    "other",
    "over",
    "part",
    "same",
    "section",
    "should",
    "such",
    "than",
    "that",
    "their",
    "there",
    "these",
    "this",
    "those",
    "through",
    "under",
    "where",
    "which",
    "while",
    "with",
    "within",
    "without",
}

TITLE_RE = re.compile(r"^\s{0,3}#{1,4}\s+(.+?)\s*$")
CAP_PHRASE_RE = re.compile(
    r"\b(?:[A-Z][A-Za-z]{2,}|[A-Z]{2,})(?:\s+(?:of|and|the|in|for|to|de|di|[A-Z][A-Za-z]{2,}|[A-Z]{2,})){1,5}\b"
)
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]{2,}")


def _slug(value: str, prefix: str = "") -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    if not slug:
        slug = hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}{slug}" if prefix else slug


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _source_file(project_root: Path, path: Path) -> str:
    real = path.resolve()
    try:
        return str(real.relative_to(project_root))
    except ValueError:
        return str(path)


def _title_from_text(path: Path, text: str) -> str:
    for line in text.splitlines()[:200]:
        match = TITLE_RE.match(line)
        if match:
            title = re.sub(r"\s+", " ", match.group(1)).strip(" #")
            if 8 <= len(title) <= 180:
                return title
    return path.stem.replace("_", " ").replace("-", " ").strip()


def _canonical_term(term: str) -> str:
    clean = re.sub(r"\s+", " ", term).strip(" .,:;()[]{}")
    key = clean.lower()
    return SYNONYMS.get(key, clean)


def _term_count(text: str, term: str) -> int:
    pattern = re.compile(rf"\b{re.escape(term)}\b", re.IGNORECASE)
    return len(pattern.findall(text))


def _heading_phrases(text: str) -> list[str]:
    phrases = []
    for line in text.splitlines():
        match = TITLE_RE.match(line)
        if not match:
            continue
        phrase = re.sub(r"[*_`#\[\]()]|\d+", " ", match.group(1))
        phrase = re.sub(r"\s+", " ", phrase).strip(" .,:;-")
        if 4 <= len(phrase) <= 90:
            phrases.append(phrase)
    return phrases


def _candidate_phrases(text: str, limit: int = 40) -> Counter[str]:
    counts: Counter[str] = Counter()
    for phrase in CAP_PHRASE_RE.findall(text[:80_000]):
        words = [w for w in WORD_RE.findall(phrase) if w.lower() not in STOPWORDS]
        if len(words) < 2 or len(words) > 6:
            continue
        normalized = " ".join(words)
        if len(normalized) < 6 or len(normalized) > 80:
            continue
        counts[_canonical_term(normalized)] += 1
    return Counter(dict(counts.most_common(limit)))


def _concept_node(label: str, source_file: str) -> dict:
    return {
        "id": _slug(label, "concept_"),
        "label": label,
        "file_type": "document",
        "source_file": source_file,
        "source_location": None,
        "source_url": None,
        "captured_at": None,
        "author": None,
        "contributor": None,
    }


def _doc_node(doc_id: str, title: str, source_file: str, file_type: str) -> dict:
    return {
        "id": doc_id,
        "label": title,
        "file_type": file_type,
        "source_file": source_file,
        "source_location": None,
        "source_url": None,
        "captured_at": None,
        "author": None,
        "contributor": None,
    }


def _edge(source: str, target: str, relation: str, confidence: str, score: float, source_file: str, weight: float = 1.0) -> dict:
    return {
        "source": source,
        "target": target,
        "relation": relation,
        "confidence": confidence,
        "confidence_score": round(score, 2),
        "source_file": source_file,
        "source_location": None,
        "weight": round(weight, 3),
    }


def _jaccard(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def _looks_like_paper(text: str) -> bool:
    signals = ("abstract", "doi", "journal", "bibliography", "references", "proceedings")
    lower = text[:10_000].lower()
    return sum(1 for signal in signals if signal in lower) >= 2


def _extract_semantic(files: list[Path], project_root: Path) -> dict:
    nodes: list[dict] = []
    edges: list[dict] = []
    concept_sources: dict[str, str] = {}
    concept_labels: dict[str, str] = {}
    doc_concepts: dict[str, set[str]] = {}
    doc_titles: dict[str, str] = {}
    doc_source_files: dict[str, str] = {}
    pair_docs: dict[tuple[str, str], set[str]] = defaultdict(set)
    term_document_counts: Counter[str] = Counter()

    corpus_id = "corpus_zoroastrian_mithras_ocr"
    nodes.append(
        {
            "id": corpus_id,
            "label": "Zoroastrian and Mithras OCR Corpus",
            "file_type": "document",
            "source_file": "graphify-input/ocr-markdown",
            "source_location": None,
            "source_url": None,
            "captured_at": None,
            "author": None,
            "contributor": None,
        }
    )

    for path in files:
        text = _read_text(path)
        source_file = _source_file(project_root, path)
        title = _title_from_text(path, text)
        doc_id = _slug(f"doc:{source_file}", "doc_")
        file_type = "paper" if _looks_like_paper(text) else "document"
        doc_titles[doc_id] = title
        doc_source_files[doc_id] = source_file
        nodes.append(_doc_node(doc_id, title, source_file, file_type))
        edges.append(_edge(corpus_id, doc_id, "references", "EXTRACTED", 1.0, source_file, 1.0))

        candidates: Counter[str] = Counter()
        for term in DOMAIN_TERMS:
            count = _term_count(text, term)
            if count:
                candidates[_canonical_term(term)] += count * 3
        for phrase in _heading_phrases(text):
            candidates[_canonical_term(phrase)] += 5
        candidates.update(_candidate_phrases(text))

        selected = []
        for label, count in candidates.most_common(16):
            words = [w.lower() for w in WORD_RE.findall(label)]
            if not words or all(word in STOPWORDS for word in words):
                continue
            selected.append((label, count))
        selected = selected[:14]

        concept_ids: set[str] = set()
        for label, count in selected:
            concept_id = _slug(label, "concept_")
            concept_sources.setdefault(concept_id, source_file)
            concept_labels[concept_id] = label
            concept_ids.add(concept_id)
            term_document_counts[concept_id] += 1
            weight = 1.0 + min(4.0, math.log1p(count))
            edges.append(_edge(doc_id, concept_id, "references", "EXTRACTED", 1.0, source_file, weight))

        doc_concepts[doc_id] = concept_ids
        for left, right in combinations(sorted(concept_ids), 2):
            pair_docs[(left, right)].add(doc_id)

    for concept_id, label in concept_labels.items():
        nodes.append(_concept_node(label, concept_sources[concept_id]))

    for (left, right), docs in pair_docs.items():
        if len(docs) < 2:
            continue
        left_count = term_document_counts[left]
        right_count = term_document_counts[right]
        confidence = min(0.9, 0.55 + (0.08 * len(docs)) + (0.02 * min(left_count, right_count)))
        source_doc = sorted(docs)[0]
        edges.append(
            _edge(
                left,
                right,
                "conceptually_related_to",
                "INFERRED",
                confidence,
                doc_source_files[source_doc],
                1.0 + math.log1p(len(docs)),
            )
        )

    doc_ids = sorted(doc_concepts)
    for left, right in combinations(doc_ids, 2):
        score = _jaccard(doc_concepts[left], doc_concepts[right])
        if score < 0.38:
            continue
        confidence = min(0.88, 0.55 + score)
        edges.append(
            _edge(
                left,
                right,
                "semantically_similar_to",
                "INFERRED",
                confidence,
                doc_source_files[left],
                1.0 + score,
            )
        )

    hyperedges = _make_hyperedges(set(concept_labels), doc_source_files)
    return {
        "nodes": _dedupe_nodes(nodes),
        "edges": _dedupe_edges(edges),
        "hyperedges": hyperedges,
        "input_tokens": 0,
        "output_tokens": 0,
    }


def _dedupe_nodes(nodes: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out = []
    for node in nodes:
        if node["id"] in seen:
            continue
        seen.add(node["id"])
        out.append(node)
    return out


def _dedupe_edges(edges: list[dict]) -> list[dict]:
    seen: set[tuple] = set()
    out = []
    for edge in edges:
        key = (
            edge["source"],
            edge["target"],
            edge["relation"],
            edge.get("source_file"),
        )
        if key in seen or edge["source"] == edge["target"]:
            continue
        seen.add(key)
        out.append(edge)
    return out


def _make_hyperedges(concept_ids: set[str], doc_source_files: dict[str, str]) -> list[dict]:
    groups = [
        (
            "zoroastrian_theology",
            "Zoroastrian Theology",
            ["Ahura Mazda", "Angra Mainyu / Ahriman", "Asha", "Amesha Spenta", "Druj", "Dualism"],
        ),
        (
            "mithraic_tradition",
            "Mithraic Tradition",
            ["Mithra / Mithras / Mitra", "Mithraism", "Mithraic", "Covenant", "Sacrifice"],
        ),
        (
            "iranian_kingship",
            "Iranian Kingship",
            ["Achaemenid", "Sasanian", "Kingship", "Cyrus", "Khvarenah / Xvarenah", "Darius"],
        ),
        (
            "ritual_and_afterlife",
            "Ritual Purity and Afterlife",
            ["Ritual purity", "Pollution", "Eschatology", "Judgment", "Resurrection", "Chinvat Bridge"],
        ),
    ]
    source_file = next(iter(doc_source_files.values()), "graphify-input/ocr-markdown")
    hyperedges = []
    for group_id, label, terms in groups:
        nodes = [_slug(term, "concept_") for term in terms if _slug(term, "concept_") in concept_ids]
        if len(nodes) >= 3:
            hyperedges.append(
                {
                    "id": group_id,
                    "label": label,
                    "nodes": nodes,
                    "relation": "form",
                    "confidence": "INFERRED",
                    "confidence_score": 0.76,
                    "source_file": source_file,
                }
            )
    return hyperedges


def _label_communities(G, communities: dict[int, list[str]]) -> dict[int, str]:
    labels: dict[int, str] = {}
    for cid, node_ids in communities.items():
        node_labels = [G.nodes[n].get("label", n) for n in node_ids]
        joined = " | ".join(node_labels).lower()
        if any(term in joined for term in ("mithra", "mithras", "mitra", "mithraic")):
            labels[cid] = "Mithraic Studies"
        elif any(term in joined for term in ("kingship", "cyrus", "achaemenid", "sasanian", "khvarenah", "xvarenah")):
            labels[cid] = "Iranian Kingship"
        elif any(term in joined for term in ("avesta", "avestan", "gathas", "yasna", "yasht", "pahlavi")):
            labels[cid] = "Avestan Texts"
        elif any(term in joined for term in ("eschatology", "judgment", "resurrection", "chinvat")):
            labels[cid] = "Afterlife Doctrine"
        elif any(term in joined for term in ("pollution", "purity", "ritual", "sacrifice")):
            labels[cid] = "Ritual Practice"
        elif any(term in joined for term in ("ahura", "ahriman", "angra", "asha", "dualism", "monotheism")):
            labels[cid] = "Zoroastrian Theology"
        elif any(term in joined for term in ("cosmology", "creation", "babylonian")):
            labels[cid] = "Creation Cosmology"
        else:
            counts = sorted(
                ((G.degree(n), G.nodes[n].get("label", n)) for n in node_ids),
                reverse=True,
            )
            labels[cid] = re.sub(r"\s+", " ", counts[0][1])[:48] if counts else f"Community {cid}"
    return labels


def _write_outputs(extraction: dict, detection: dict, input_path: str, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    G = build_from_json(extraction)
    communities = cluster(G)
    cohesion = score_all(G, communities)
    labels = _label_communities(G, communities)
    gods = god_nodes(G)
    surprises = surprising_connections(G, communities)
    questions = suggest_questions(G, communities, labels)
    tokens = {
        "input": extraction.get("input_tokens", 0),
        "output": extraction.get("output_tokens", 0),
    }

    report = generate(
        G,
        communities,
        cohesion,
        labels,
        gods,
        surprises,
        detection,
        tokens,
        input_path,
        suggested_questions=questions,
    )
    (out_dir / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    to_json(G, communities, str(out_dir / "graph.json"), force=True)
    to_html(G, communities, str(out_dir / "graph.html"), community_labels=labels)
    optional_exports: dict[str, str] = {}
    try:
        to_svg(G, communities, str(out_dir / "graph.svg"), community_labels=labels)
        optional_exports["svg"] = str(out_dir / "graph.svg")
    except Exception as exc:
        optional_exports["svg_error"] = str(exc)

    try:
        to_graphml(_graphml_safe_graph(G), communities, str(out_dir / "graph.graphml"))
        optional_exports["graphml"] = str(out_dir / "graph.graphml")
    except Exception as exc:
        optional_exports["graphml_error"] = str(exc)

    obsidian_count = 0
    try:
        obsidian_count = to_obsidian(G, communities, str(out_dir / "obsidian"), community_labels=labels, cohesion=cohesion)
        to_canvas(G, communities, str(out_dir / "obsidian" / "graph.canvas"), community_labels=labels)
        optional_exports["obsidian"] = str(out_dir / "obsidian")
    except Exception as exc:
        optional_exports["obsidian_error"] = str(exc)

    analysis = {
        "communities": {str(k): v for k, v in communities.items()},
        "cohesion": {str(k): v for k, v in cohesion.items()},
        "labels": {str(k): v for k, v in labels.items()},
        "gods": gods,
        "surprises": surprises,
        "questions": questions,
        "obsidian_notes": obsidian_count,
        "optional_exports": optional_exports,
    }
    Path(".graphify_analysis.json").write_text(json.dumps(analysis, indent=2), encoding="utf-8")
    Path(".graphify_labels.json").write_text(json.dumps({str(k): v for k, v in labels.items()}, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "nodes": G.number_of_nodes(),
                "edges": G.number_of_edges(),
                "communities": len(communities),
                "obsidian_notes": obsidian_count,
                "optional_exports": optional_exports,
                "out_dir": str(out_dir),
            },
            indent=2,
        )
    )


def _graphml_safe_graph(G) -> nx.Graph:
    H = G.__class__()
    H.graph.update({k: _graphml_value(v) for k, v in G.graph.items() if k != "hyperedges"})
    for node_id, attrs in G.nodes(data=True):
        H.add_node(node_id, **{k: _graphml_value(v) for k, v in attrs.items()})
    for source, target, attrs in G.edges(data=True):
        H.add_edge(source, target, **{k: _graphml_value(v) for k, v in attrs.items()})
    return H


def _graphml_value(value):
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return value
    return json.dumps(value, ensure_ascii=True)


def main() -> None:
    parser = argparse.ArgumentParser(prog="graphify-zoro-analyze")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("graphify-input/ocr-markdown"),
        help="Markdown-only input directory to graph.",
    )
    args = parser.parse_args()

    settings = get_settings()
    project_root = settings.project_root
    input_path = args.input
    if not input_path.is_absolute():
        input_path = project_root / input_path

    files = sorted(path for path in input_path.rglob("*.md") if path.is_file())
    if not files:
        raise SystemExit(f"No Markdown files found in {input_path}")

    detection = detect(input_path)
    Path(".graphify_detect.json").write_text(json.dumps(detection, indent=2), encoding="utf-8")
    Path(".graphify_ast.json").write_text(
        json.dumps({"nodes": [], "edges": [], "input_tokens": 0, "output_tokens": 0}, indent=2),
        encoding="utf-8",
    )

    semantic = _extract_semantic(files, project_root)
    Path(".graphify_semantic.json").write_text(json.dumps(semantic, indent=2), encoding="utf-8")
    Path(".graphify_extract.json").write_text(json.dumps(semantic, indent=2), encoding="utf-8")
    _write_outputs(semantic, detection, str(input_path), settings.graphify_out_dir)


if __name__ == "__main__":
    main()
