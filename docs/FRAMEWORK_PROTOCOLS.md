# Graphify Framework Protocol

This project uses Graphify as the graph navigation framework for the
Zoroastrian/Mithras corpus.

## Source Checks

The current protocol is based on three checks:

- Official Graphify site/docs:
  - https://graphify.net/knowledge-graph-for-ai-coding-assistants.html
  - https://graphify.net/graphify-cli-commands.html
  - https://graphify.net/tree-sitter-ast-extraction.html
  - https://graphify.net/leiden-community-detection.html
  - https://graphify.net/graphify-claude-code-integration.html
- Those docs define `graphify-out/graph.html`, `graphify-out/graph.json`, and
  `graphify-out/GRAPH_REPORT.md`; graph navigation uses `graphify query`,
  `graphify path`, and `graphify explain`.
- Official Graphify repository/package: the installed package is `graphifyy`
  and the local CLI exposes query/path/explain/MCP/benchmark/hook commands.
- Local project artifacts: the canonical graph is
  `/Users/ali/GRAPHIFY-zoroastrianism/graphify-out/graph.json`, built only from
  `/Users/ali/GRAPHIFY-zoroastrianism/graphify-input/ocr-markdown-clean`.

## Correct Graphify Model

Graphify is not the conversational answer layer by itself. It is the map:

- `GRAPH_REPORT.md` gives orientation: god nodes, communities, surprises, and
  suggested questions.
- `graphify query` extracts a focused subgraph for a question.
- `graphify path` traces exact concept-to-concept paths.
- `graphify explain` shows one node and its neighbors.
- `python -m graphify.serve graphify-out/graph.json` exposes the graph through
  MCP tools for assistants that support MCP.

The assistant then uses the graph evidence to produce language answers. Do not
paste all of `graph.json` into prompts.

## Required Query Commands

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate

graphify query "What connects Mithra to khvarnah?" --graph graphify-out/graph.json --budget 1500
graphify path "Mithra" "Ahura Mazdā" --graph graphify-out/graph.json
graphify explain "Zarathustra" --graph graphify-out/graph.json
graphify benchmark graphify-out/graph.json
```

## MCP Server

Run this when an assistant can consume MCP tools:

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
python -m graphify.serve graphify-out/graph.json
```

This is read-only graph access. It should be pointed at the canonical
`graphify-out/graph.json`.

## Assistant Integration

Codex integration is installed in this repo:

- `AGENTS.md` tells Codex to read `graphify-out/GRAPH_REPORT.md`.
- `.codex/hooks.json` emits the Graphify reminder before Bash tool use.

The intended use is:

1. Read `GRAPH_REPORT.md` for orientation.
2. Use `graphify query/path/explain` for exact evidence.
3. Cite source files and edge confidence tags when answering.

## Rebuild Discipline

Do not run Graphify over the project root when the intended corpus is the
Zoroastrian OCR corpus. That would mix helper code, instructions, and generated
files into the domain graph.

Correct graph input:

```bash
/Users/ali/GRAPHIFY-zoroastrianism/graphify-input/ocr-markdown-clean
```

Correct graph output:

```bash
/Users/ali/GRAPHIFY-zoroastrianism/graphify-out
```

Datalab/OCR API documentation belongs in:

```bash
/Users/ali/GRAPHIFY-datalab-api-docs
```

It must not be merged into the canonical Zoroastrian graph.

## Verification

Use the official smoke script:

```bash
scripts/graphify_official_smoke.sh
```

It runs only read-only official Graphify commands and writes
`docs/graphify-official-smoke.md`.
