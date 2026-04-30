# GRAPHIFY Zoroastrianism

Start here:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
scripts/open_research_workspace.sh
```

Detailed operator guide: `START_HERE.md`.

Graph-first research workspace for the corpus at:

`/Users/ali/Documents/EVANON/MITHRAS 3`

This project does three things:

1. OCR / convert the source corpus into machine-readable text with Datalab.
2. Build a Graphify knowledge graph over the OCR Markdown.
3. Keep corpus graph inputs separate from OCR vendor/API reference material.

Cognee is intentionally not used in this folder.

This folder is also a Git repository. The original corpus is copied into `raw/source/` and tracked with Git LFS. OCR Markdown and graph outputs are tracked in normal Git so future agents can start from the same corpus, OCR state, and graph.

## Project Layout

- `raw/source/`
  Original source corpus copied into this repo. Large PDFs, TIFFs, images, and media are tracked with Git LFS.
- `raw/ocr/`
  Datalab conversion output for corpus files.
- `graphify-input/ocr-markdown-clean/`
  Deduped symlinks to OCR Markdown files that are included in the graph build and shared with Cognee.
- `graphify-out/`
  Graphify artifacts for the Zoroastrian/Mithras corpus, such as `graph.json`, `graph.html`, and `GRAPH_REPORT.md`.
- `graphify-out/llm-cache/`
  Per-chunk LLM extraction cache. Reruns reuse this cache unless `--force` is used or inputs/prompts change.
- `docs/ocr-status/`
  OCR status snapshots, including converted and pending PDF lists.
- `.githooks/`
  Versioned Git hooks for Git LFS and corpus-safe Graphify update flags.

## First Setup

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
```

The local `.env` should contain:

```bash
DATALAB_API_KEY=...
OPENAI_API_KEY=...
LLM_MODEL=gpt-5.5
LLM_REASONING_EFFORT=xhigh
LLM_MAX_OUTPUT_TOKENS=30000
```

Do not commit or paste `.env` contents into documentation.

Install Graphify's Codex integration:

```bash
/Users/ali/.local/bin/graphify codex install
```

Git/LFS setup is already initialized in this repo. See `docs/GIT_WORKFLOW.md` for the exact tracking and hook behavior.

## OCR The Corpus

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
graphify-zoro-bootstrap
graphify-zoro-ocr --suffix .pdf
```

This uses Datalab conversion in `accurate` mode and writes outputs into `raw/ocr/`.

Current OCR status:

- 190 PDFs found in the source corpus.
- 52 PDFs converted to Markdown.
- 138 PDFs still pending because Datalab returned 403 during the run.
- TIFF files are intentionally ignored for now.

Check status:

```bash
graphify-zoro-ocr-status
```

Latest known logs:

- `docs/ocr-status/20260429-121842-summary.txt`
- `docs/ocr-status/20260429-121842-converted-pdfs.txt`
- `docs/ocr-status/20260429-121842-pending-pdfs.txt`
- `docs/ocr-status/20260429-121759-api-stop.txt`

## Build The LLM Graphify Graph

The graph build uses only deduped OCR Markdown files. Datalab-generated image assets and duplicate Markdown outputs are not included.

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
python scripts/build_clean_markdown_input.py
graphify-zoro-llm --input graphify-input/ocr-markdown-clean --workers 2 --timeout 1200
```

Main outputs:

- `graphify-out/graph.json`
- `graphify-out/graph.html`
- `graphify-out/GRAPH_REPORT.md`
- `graphify-out/graph.svg`
- `graphify-out/graph.graphml`
- `graphify-out/obsidian/`
- `graphify-out/.graphify_semantic_llm.json`
- `graphify-out/.graphify_extract.json`

Current LLM build:

- 32 unique OCR Markdown files included after dedupe from 52 converted Markdown files.
- Model: `gpt-5.5`
- Reasoning effort: `xhigh`
- 86/86 chunks succeeded.
- 0 failed chunks.
- 996 semantic nodes.
- 2,449 graph edges in `graph.json`.
- 167 hyperedges.
- Token usage: 564,147 input tokens, 1,037,291 output tokens.

The accepted graph is the clean `gpt-5.5` / `xhigh` rebuild over `graphify-input/ocr-markdown-clean`.

The LLM pass samples very large documents into representative chunks rather than sending every byte of every long PDF. It is still the semantic Graphify layer: entities, relations, communities, inferred edges, reports, HTML, SVG, GraphML, and Obsidian notes are generated from LLM extraction output.

Safe model/API smoke test without overwriting the graph:

```bash
graphify-zoro-llm --input graphify-input/ocr-markdown-clean --smoke-test --max-chars 1800 --timeout 300
```

Latest smoke test result:

- `gpt-5.5`
- `reasoning_effort=xhigh`
- `max_output_tokens=30000`
- Completed successfully without overwriting graph outputs.
- One small chunk used 2,025 input tokens, 11,134 output tokens, including 8,804 reasoning tokens.

## Fallback Heuristic Graph

If the OpenAI key is unavailable or you want a cheap non-LLM baseline:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
graphify-zoro-analyze --input graphify-input/ocr-markdown
```

That command is deterministic and cheaper, but it is not the full semantic LLM graph.

## Query The Graph

Query examples:

```bash
graphify query "What does this corpus connect Mithra or Mithras to?" --graph graphify-out/graph.json
graphify explain "Ahura Mazdā" --graph graphify-out/graph.json
graphify path "Mithra" "Ahura Mazda" --graph graphify-out/graph.json
```

Official Graphify framework protocol:

```bash
scripts/graphify_official_smoke.sh
scripts/graphify_mcp_server.sh
```

`graphify_official_smoke.sh` runs read-only official Graphify commands and
writes `docs/graphify-official-smoke.md`. `graphify_mcp_server.sh` starts the
official Graphify MCP server over `graphify-out/graph.json`.

Smoke tests already verified:

- `graphify explain "Ahura Mazdā"` works.
- `graphify query "What does the LLM graph say about Mithra and kingship?"` works.
- `graphify path "Mithra" "Ahura Mazda"` works.
- Latest saved query smoke report: `docs/query-smoke-tests.md`.
- Full framework protocol notes: `docs/FRAMEWORK_PROTOCOLS.md`.

## Persistent Worker

The repo includes `scripts/graphify_worker.sh` for unattended finalization. It accepts a graph when at least 99% of chunks succeeded and all failures are documented, writes `graphify-out/worker-status.json`, runs query smoke tests, commits graph artifacts, and pushes `origin main`.

The user LaunchAgent at `/Users/ali/Library/LaunchAgents/com.evanon.graphify-zoro-llm.plist` points to this worker and writes local logs under `logs/`.

## Add More PDFs Later

When more Datalab credit is available, resume OCR and rebuild:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
graphify-zoro-ocr --suffix .pdf
graphify-zoro-ocr-status
python scripts/build_clean_markdown_input.py
graphify-zoro-llm --input graphify-input/ocr-markdown-clean --workers 4
```

The existing `graphify-out/llm-cache/` prevents paying again for chunks that were already processed.
