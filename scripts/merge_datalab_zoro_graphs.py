#!/usr/bin/env python3
"""Build an optional combined Datalab-OCR + Zoroastrian corpus graph.

The main Zoroastrian graph remains the canonical content graph. This script
creates a side artifact for questions that need both OCR pipeline context and
the extracted Zoroastrian knowledge graph.
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

from networkx.readwrite import json_graph

from graphify.export import to_html


ROOT = Path(__file__).resolve().parents[1]
ZORO_GRAPH = ROOT / "graphify-out" / "graph.json"
DATALAB_GRAPH = Path(
    "/Users/ali/GRAPHIFY-datalab-api-docs/graphify-out/datalab-docs/graph.json"
)
OUT_JSON = ROOT / "graphify-out" / "combined-datalab-zoro-graph.json"
OUT_HTML = ROOT / "graphify-out" / "combined-datalab-zoro-graph.html"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def max_community(graph_data: dict) -> int:
    communities = [
        node.get("community")
        for node in graph_data.get("nodes", [])
        if isinstance(node.get("community"), int)
    ]
    return max(communities, default=-1)


def add_edge(
    links: list[dict],
    source: str,
    target: str,
    relation: str,
    confidence: str,
    score: float,
    location: str,
) -> None:
    links.append(
        {
            "source": source,
            "target": target,
            "_src": source,
            "_tgt": target,
            "relation": relation,
            "confidence": confidence,
            "confidence_score": score,
            "source_file": "docs/STATUS.md",
            "source_location": location,
            "weight": score,
        }
    )


def build_combined() -> dict:
    zoro = load_json(ZORO_GRAPH)
    datalab = load_json(DATALAB_GRAPH)

    combined = {
        "directed": zoro.get("directed", False),
        "multigraph": zoro.get("multigraph", False),
        "graph": deepcopy(zoro.get("graph", {})),
        "nodes": deepcopy(zoro.get("nodes", [])),
        "links": deepcopy(zoro.get("links", [])),
        "hyperedges": deepcopy(zoro.get("hyperedges", [])),
    }

    datalab_offset = max_community(zoro) + 1
    for node in datalab.get("nodes", []):
        copied = deepcopy(node)
        if isinstance(copied.get("community"), int):
            copied["community"] = copied["community"] + datalab_offset
        combined["nodes"].append(copied)

    combined["links"].extend(deepcopy(datalab.get("links", [])))
    combined["hyperedges"].extend(deepcopy(datalab.get("hyperedges", [])))

    bridge_community = max_community(combined) + 1
    bridge_nodes = [
        {
            "id": "ops_datalab_ocr_pipeline_zoroastrian_corpus",
            "label": "Datalab OCR Pipeline for Zoroastrian Corpus",
            "file_type": "operations",
            "source_file": "docs/STATUS.md",
            "source_location": "OCR Status",
            "source_url": None,
            "captured_at": "2026-04-29",
            "author": None,
            "contributor": "Codex",
            "community": bridge_community,
            "norm_label": "datalab ocr pipeline for zoroastrian corpus",
        },
        {
            "id": "ops_zoroastrian_ocr_markdown_corpus",
            "label": "Zoroastrian OCR Markdown Corpus",
            "file_type": "corpus",
            "source_file": "docs/STATUS.md",
            "source_location": "Current Graph Build",
            "source_url": None,
            "captured_at": "2026-04-29",
            "author": None,
            "contributor": "Codex",
            "community": bridge_community,
            "norm_label": "zoroastrian ocr markdown corpus",
        },
    ]
    combined["nodes"].extend(bridge_nodes)

    add_edge(
        combined["links"],
        "datalab_document_conversion",
        "ops_datalab_ocr_pipeline_zoroastrian_corpus",
        "documents",
        "EXTRACTED",
        1.0,
        "Datalab API docs graph + project OCR status",
    )
    add_edge(
        combined["links"],
        "convert_api",
        "ops_datalab_ocr_pipeline_zoroastrian_corpus",
        "used_by",
        "EXTRACTED",
        1.0,
        "Datalab API docs graph + project OCR status",
    )
    add_edge(
        combined["links"],
        "ocr_capability",
        "ops_datalab_ocr_pipeline_zoroastrian_corpus",
        "capability_used_by",
        "EXTRACTED",
        1.0,
        "Datalab API docs graph + project OCR status",
    )
    add_edge(
        combined["links"],
        "ops_datalab_ocr_pipeline_zoroastrian_corpus",
        "ops_zoroastrian_ocr_markdown_corpus",
        "produced",
        "EXTRACTED",
        1.0,
        "OCR Status",
    )
    add_edge(
        combined["links"],
        "ops_zoroastrian_ocr_markdown_corpus",
        "llm_zoroastrianism",
        "contains_topic",
        "INFERRED",
        0.95,
        "Current Graph Build",
    )
    add_edge(
        combined["links"],
        "ops_zoroastrian_ocr_markdown_corpus",
        "llm_mithras",
        "contains_topic",
        "INFERRED",
        0.95,
        "Current Graph Build",
    )

    combined["hyperedges"].append(
        {
            "id": "hyper_datalab_ocr_to_zoro_graph_pipeline",
            "label": "Datalab OCR Pipeline Feeding Zoroastrian Graphify Corpus",
            "nodes": [
                "datalab_document_conversion",
                "convert_api",
                "ocr_capability",
                "ops_datalab_ocr_pipeline_zoroastrian_corpus",
                "ops_zoroastrian_ocr_markdown_corpus",
                "llm_zoroastrianism",
                "llm_mithras",
            ],
            "relation": "operationally_connects",
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "source_file": "docs/STATUS.md",
        }
    )

    combined["graph"]["hyperedges"] = deepcopy(combined["hyperedges"])
    combined["graph"]["combined_from"] = [
        str(DATALAB_GRAPH),
        str(ZORO_GRAPH),
    ]
    combined["graph"]["note"] = (
        "Optional operations+content graph. The canonical Zoroastrian content "
        "graph remains graphify-out/graph.json."
    )
    return combined


def write_html(graph_data: dict) -> None:
    graph = json_graph.node_link_graph(graph_data, edges="links")
    graph.graph["hyperedges"] = graph_data.get("hyperedges", [])
    communities: dict[int, list[str]] = {}
    for node_id, attrs in graph.nodes(data=True):
        community = attrs.get("community")
        if not isinstance(community, int):
            community = 0
        communities.setdefault(community, []).append(node_id)
    labels = {cid: f"Community {cid}" for cid in communities}
    labels[max(labels)] = "OCR Provenance Bridge"
    to_html(graph, communities, str(OUT_HTML), community_labels=labels)


def main() -> None:
    combined = build_combined()
    OUT_JSON.write_text(json.dumps(combined, indent=2, ensure_ascii=False), encoding="utf-8")
    write_html(combined)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_HTML}")
    print(
        f"{len(combined['nodes'])} nodes, "
        f"{len(combined['links'])} links, "
        f"{len(combined['hyperedges'])} hyperedges"
    )


if __name__ == "__main__":
    main()
