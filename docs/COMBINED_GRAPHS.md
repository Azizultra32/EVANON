# Combined Graphs

There are two separate Graphify runs:

- Datalab/OCR API docs graph: `/Users/ali/GRAPHIFY-datalab-api-docs/graphify-out/datalab-docs/graph.json`
- Zoroastrian corpus graph: `graphify-out/graph.json`

The long LLM extraction was run against the Zoroastrian OCR Markdown corpus only. It was not run over the Datalab API docs graph.

## Canonical Graph

Use `graphify-out/graph.json` and `graphify-out/graph.html` as the canonical Zoroastrian content graph.

This keeps concepts like Mithras, Ahura Mazda, dēn, Avesta, Sasanian law, and ritual purity separate from implementation/tooling concepts like `Convert API` and `X-API-Key Authentication`.

## Optional Combined Graph

For operational questions that need both OCR tooling and content context, use:

- `graphify-out/combined-datalab-zoro-graph.json`
- `graphify-out/combined-datalab-zoro-graph.html`

This combined graph is a side artifact. It does not replace the canonical Zoroastrian graph.

The combined graph:

- Preserves all Zoro nodes, links, and hyperedges.
- Adds the Datalab/OCR API documentation graph.
- Offsets Datalab community IDs so they do not collide with Zoro communities.
- Adds explicit provenance bridge edges from Datalab OCR concepts to the Zoro OCR Markdown corpus.

The bridge edges are operational provenance, sourced from `docs/STATUS.md`, not a fresh LLM re-extraction of the source corpus.

## Rebuild

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
python scripts/merge_datalab_zoro_graphs.py
```

## Query

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
graphify query "what connects the Datalab OCR pipeline to the Zoroastrian corpus?" --graph graphify-out/combined-datalab-zoro-graph.json
```
