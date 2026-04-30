#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/Users/ali/GRAPHIFY-zoroastrianism"
GRAPH_PATH="graphify-out/graph.json"
REPORT_PATH="docs/graphify-official-smoke.md"
GRAPHIFY_BIN="${GRAPHIFY_BIN:-.venv/bin/graphify}"

cd "$PROJECT_ROOT"
mkdir -p docs

tmp="$(mktemp)"
{
  echo "# Graphify Official Smoke Test"
  echo
  echo "- Generated at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "- Graph: \`$PROJECT_ROOT/$GRAPH_PATH\`"
  echo "- Scope: read-only official Graphify commands; no rebuild, no merge, no OCR."
  echo
} > "$tmp"

run_section() {
  local title="$1"
  shift
  local output
  local status
  set +e
  output=$("$@" 2>&1)
  status=$?
  set -e
  {
    echo "## $title"
    echo
    echo "- Exit status: \`$status\`"
    echo
    echo '```text'
    printf '$'
    printf ' %q' "$@"
    printf '\n'
    printf '%s\n' "$output" | sed -n '1,160p'
    echo '```'
    echo
  } >> "$tmp"
  return "$status"
}

failures=0

run_section "Query" \
  "$GRAPHIFY_BIN" query "What connects Mithra to khvarnah?" --graph "$GRAPH_PATH" --budget 1200 || failures=1

run_section "Path" \
  "$GRAPHIFY_BIN" path "Mithra" "Ahura Mazdā" --graph "$GRAPH_PATH" || failures=1

run_section "Explain" \
  "$GRAPHIFY_BIN" explain "Zarathustra" --graph "$GRAPH_PATH" || failures=1

run_section "Benchmark" \
  "$GRAPHIFY_BIN" benchmark "$GRAPH_PATH" || failures=1

run_section "Hook Status" \
  "$GRAPHIFY_BIN" hook status || failures=1

mv "$tmp" "$REPORT_PATH"
exit "$failures"
