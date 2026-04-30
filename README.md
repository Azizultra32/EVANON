# GRAPHIFY Zoroastrianism

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
- `graphify-input/ocr-markdown/`
  Symlinks to OCR Markdown files that are included in the graph build.
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

The graph build uses only OCR Markdown files. Datalab-generated image assets are not included.

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
find graphify-input/ocr-markdown -type l -delete
find raw/ocr -maxdepth 1 -type f -name '*.md' -exec ln -sf "$PWD/{}" graphify-input/ocr-markdown/ \;
graphify-zoro-llm --input graphify-input/ocr-markdown --workers 4
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

- 52 OCR Markdown files included.
- 142/142 chunks succeeded.
- 612 semantic nodes.
- 1,685 graph edges in `graph.json`.
- 36 hyperedges.
- 21 communities.
- Token usage: 885,633 input tokens, 237,077 output tokens.
- No final LLM failures.

The current graph was built before the model upgrade, using the earlier configured model. The graph builder is now configured for OpenAI's Responses API, `gpt-5.5`, `LLM_REASONING_EFFORT=xhigh`, and `LLM_MAX_OUTPUT_TOKENS=30000` for future full rebuilds.

The LLM pass samples very large documents into representative chunks rather than sending every byte of every long PDF. It is still the semantic Graphify layer: entities, relations, communities, inferred edges, reports, HTML, SVG, GraphML, and Obsidian notes are generated from LLM extraction output.

Safe model/API smoke test without overwriting the graph:

```bash
graphify-zoro-llm --input graphify-input/ocr-markdown --smoke-test --max-chars 1800 --timeout 300
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

Smoke tests already verified:

- `graphify explain "Ahura Mazdā"` works.
- `graphify query "What does the LLM graph say about Mithra and kingship?"` works.
- `graphify path "Mithra" "Ahura Mazda"` works.

## Add More PDFs Later

When more Datalab credit is available, resume OCR and rebuild:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
graphify-zoro-ocr --suffix .pdf
graphify-zoro-ocr-status
find graphify-input/ocr-markdown -type l -delete
find raw/ocr -maxdepth 1 -type f -name '*.md' -exec ln -sf "$PWD/{}" graphify-input/ocr-markdown/ \;
graphify-zoro-llm --input graphify-input/ocr-markdown --workers 4
```

The existing `graphify-out/llm-cache/` prevents paying again for chunks that were already processed.
