# Zoroastrian Knowledge Graph Start Here

This is the current entry point for the Zoroastrian/Mithras corpus.

## What Is Ready

- Canonical Graphify project: `/Users/ali/GRAPHIFY-zoroastrianism`
- Canonical Cognee project: `/Users/ali/COGNEE-zoroastrianism`
- Clean corpus input: `/Users/ali/GRAPHIFY-zoroastrianism/graphify-input/ocr-markdown-clean`
- Graphify UI: `/Users/ali/GRAPHIFY-zoroastrianism/graphify-out/graph.html`
- Graphify graph: `/Users/ali/GRAPHIFY-zoroastrianism/graphify-out/graph.json`
- Graphify report: `/Users/ali/GRAPHIFY-zoroastrianism/graphify-out/GRAPH_REPORT.md`
- Cognee dataset: `zoroastrianism_corpus`

Current validated state:

- Corpus guard: GO
- Corpus files: 32 clean Markdown files
- Duplicate text groups: 0
- Tooling/API contamination: 0
- Graphify graph: 996 nodes, 2,449 edges, 167 hyperedges
- Cognee indexed status: 32 updated, 0 pending, 0 failed
- Cognee improve: completed on 2026-04-30, 9,336 nodes and 19,248 edges projected

## Open The Workspace

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
scripts/open_research_workspace.sh
```

That opens the Graphify HTML graph and prints the official query commands. It
does not rebuild, OCR, merge, or re-ingest anything.

## Ask Conversational Questions With Cognee

Cognee is the conversational memory layer.

```bash
cd /Users/ali/COGNEE-zoroastrianism
.venv/bin/cognee-zoro recall "What does this corpus say about Mithra or Mithras?"
.venv/bin/cognee-zoro recall "How are khvarnah, farr, and kingship related?" --query-type GRAPH_COMPLETION
```

Inspect retrieved evidence without relying only on prose:

```bash
cd /Users/ali/COGNEE-zoroastrianism
.venv/bin/cognee-zoro search-context "What evidence connects the winged disk, Ahura Mazda, Farvahar, and khvarnah?"
```

## Navigate The Graph With Graphify

Graphify is the map/navigation layer.

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
.venv/bin/graphify query "What connects Mithra to khvarnah?" --graph graphify-out/graph.json --budget 1500
.venv/bin/graphify path "Mithra" "Ahura Mazda" --graph graphify-out/graph.json
.venv/bin/graphify explain "Zarathustra" --graph graphify-out/graph.json
```

Run the saved read-only smoke test:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
scripts/graphify_official_smoke.sh
```

## Keep It Fresh

Cognee has a LaunchAgent installed:

```bash
launchctl print gui/$(id -u)/com.evanon.cognee-zoro
launchctl kickstart -k gui/$(id -u)/com.evanon.cognee-zoro
```

It runs `/Users/ali/COGNEE-zoroastrianism/scripts/cognee_worker.sh`, detects
already-current documents by content hash, and retries failed ingestion after
throttling.

Graphify git hooks are installed:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
.venv/bin/graphify hook status
```

## Add New Content Later

1. Put new accepted Markdown text into:
   `/Users/ali/GRAPHIFY-zoroastrianism/graphify-input/ocr-markdown-clean`
2. Run the corpus guard before any LLM work:
   `python3 /Users/ali/.codex/skills/corpus-graph-guard/scripts/audit_corpus.py --project /Users/ali/GRAPHIFY-zoroastrianism --source /Users/ali/GRAPHIFY-zoroastrianism/graphify-input/ocr-markdown-clean --graph-input /Users/ali/GRAPHIFY-zoroastrianism/graphify-input/ocr-markdown-clean --markdown`
3. If the gate says GO, run Graphify update through the project worker:
   `cd /Users/ali/GRAPHIFY-zoroastrianism && scripts/graphify_worker.sh`
4. Refresh Cognee:
   `cd /Users/ali/COGNEE-zoroastrianism && .venv/bin/cognee-zoro remember-folder --batch-size 5`

Do not place OCR API docs, assistant instructions, generated graph output,
Graphify docs, or Cognee docs into the corpus input folder.

