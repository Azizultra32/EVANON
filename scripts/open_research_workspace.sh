#!/usr/bin/env bash
set -euo pipefail

GRAPHIFY_ROOT="/Users/ali/GRAPHIFY-zoroastrianism"
COGNEE_ROOT="/Users/ali/COGNEE-zoroastrianism"

open "$GRAPHIFY_ROOT/graphify-out/graph.html"

cat <<'MSG'
Zoroastrian/Mithras knowledge workspace is ready.

Opened:
  /Users/ali/GRAPHIFY-zoroastrianism/graphify-out/graph.html

Read first:
  /Users/ali/GRAPHIFY-zoroastrianism/START_HERE.md
  /Users/ali/GRAPHIFY-zoroastrianism/graphify-out/GRAPH_REPORT.md

Graphify graph navigation:
  cd /Users/ali/GRAPHIFY-zoroastrianism
  .venv/bin/graphify query "What connects Mithra to khvarnah?" --graph graphify-out/graph.json --budget 1500
  .venv/bin/graphify path "Mithra" "Ahura Mazda" --graph graphify-out/graph.json
  .venv/bin/graphify explain "Zarathustra" --graph graphify-out/graph.json

Cognee conversational memory:
  cd /Users/ali/COGNEE-zoroastrianism
  .venv/bin/cognee-zoro recall "What does this corpus say about Mithra or Mithras?"
  .venv/bin/cognee-zoro search-context "What evidence connects the winged disk, Ahura Mazda, Farvahar, and khvarnah?"

Status checks:
  cd /Users/ali/GRAPHIFY-zoroastrianism && scripts/graphify_official_smoke.sh
  cd /Users/ali/COGNEE-zoroastrianism && .venv/bin/cognee-zoro stats
MSG

echo
echo "Cognee current indexed status:"
"$COGNEE_ROOT/.venv/bin/cognee-zoro" stats

