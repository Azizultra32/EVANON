# Status

- Source corpus path: `/Users/ali/Documents/EVANON/MITHRAS 3`
- Graphify project root: `/Users/ali/GRAPHIFY-zoroastrianism`
- In-repo source corpus path: `/Users/ali/GRAPHIFY-zoroastrianism/raw/source`
- This project is responsible for:
  - OCR / conversion with Datalab
  - Graphify raw corpus preparation
  - Graphify LLM graph extraction, query, and graph artifacts
- Cognee was not used for this build.
- Git is initialized locally. Large source PDFs/TIFFs/images/media are tracked with Git LFS.
- The separate Datalab API documentation graph at `/Users/ali/GRAPHIFY-datalab-api-docs` is tooling reference only. It is not part of the canonical Zoroastrian content graph and should not be merged into `graphify-out/graph.json`.

## Important Notes

- The corpus contains PDFs and TIFFs. TIFFs are intentionally ignored for now.
- API keys should be stored in `.env`, not hard-coded into scripts or documentation.
- Graphify should be installed into this folder's agent instructions with:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
/Users/ali/.local/bin/graphify codex install
```

- After OCR output exists in `raw/ocr/`, rebuild `graphify-input/ocr-markdown-clean/` with `scripts/build_clean_markdown_input.py` and rerun the LLM graph command below.
- Git hooks are installed through `core.hooksPath=.githooks`. They are corpus-safe and write `graphify-out/needs_update` when `raw/source/`, `raw/ocr/`, or `graphify-input/` changes.

## OCR Status

- Total PDFs found: 190
- Converted PDFs: 52
- Pending PDFs: 138
- Stop reason: Datalab returned 403 during the OCR run.
- Latest status files:
  - `docs/ocr-status/20260429-121842-summary.txt`
  - `docs/ocr-status/20260429-121842-converted-pdfs.txt`
  - `docs/ocr-status/20260429-121842-pending-pdfs.txt`
  - `docs/ocr-status/20260429-121759-api-stop.txt`

Resume OCR later:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
graphify-zoro-ocr --suffix .pdf
graphify-zoro-ocr-status
```

## Current Graph Build

- Build type: Graphify LLM semantic extraction
- Input used: `graphify-input/ocr-markdown-clean`
- OCR Markdown files included: 32 unique files after dedupe from 52 converted Markdown files
- Graph output: `graphify-out/`
- Current graph size: 1,492 nodes, 3,962 graph links, 272 hyperedges
- LLM extraction chunks: 141/142 succeeded
- LLM token usage: 919,614 input tokens, 1,718,022 output tokens
- Final LLM failures: 1 documented in `graphify-out/llm-failures.json`
- Runtime query layer verified with `graphify query`, `graphify explain`, and `graphify path`.
- Current accepted model: `gpt-5.5` through OpenAI Responses API.
- Current accepted reasoning effort: `xhigh`.
- Acceptance policy: one transient failed chunk is acceptable when documented; the graph remains valid and queryable.

Build or rebuild the graph:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
python scripts/build_clean_markdown_input.py
graphify-zoro-llm --input graphify-input/ocr-markdown-clean --workers 2 --timeout 1200
```

The LLM cache is in `graphify-out/llm-cache/`; reruns should be cheap unless new OCR Markdown files are added or `--force` is used.

Unattended finalization:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
scripts/graphify_worker.sh
```

The worker writes `graphify-out/worker-status.json`, `docs/query-smoke-tests.md`, commits graph artifacts, and pushes to `origin main`.

Safe model/API smoke test without overwriting graph outputs:

```bash
graphify-zoro-llm --input graphify-input/ocr-markdown-clean --smoke-test --max-chars 1800 --timeout 300
```

Latest smoke test result:

- `gpt-5.5`
- `reasoning_effort=xhigh`
- `max_output_tokens=30000`
- Completed successfully without overwriting graph outputs.
- One small chunk used 2,025 input tokens, 11,134 output tokens, including 8,804 reasoning tokens.

## Current Outputs

- `graphify-out/GRAPH_REPORT.md`
- `graphify-out/graph.html`
- `graphify-out/graph.json`
- `graphify-out/graph.svg`
- `graphify-out/graph.graphml`
- `graphify-out/obsidian/`
- `graphify-out/.graphify_semantic_llm.json`
- `graphify-out/.graphify_extract.json`
