#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/Users/ali/GRAPHIFY-zoroastrianism"
GRAPH_JSON="graphify-out/graph.json"
SEMANTIC_JSON="graphify-out/.graphify_semantic_llm.json"
FAILURES_JSON="graphify-out/llm-failures.json"
STATUS_JSON="graphify-out/worker-status.json"
QUERY_REPORT="docs/query-smoke-tests.md"
MIN_SUCCESS_RATE="${GRAPHIFY_MIN_SUCCESS_RATE:-0.99}"
MAX_ATTEMPTS="${GRAPHIFY_WORKER_MAX_ATTEMPTS:-3}"
LOCK_DIR="logs/graphify-worker.lock"

cd "$PROJECT_ROOT"
mkdir -p logs docs graphify-out

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "another graphify worker is already running: $LOCK_DIR"
  exit 0
fi
trap 'rm -rf "$LOCK_DIR"' EXIT

log() {
  printf '[%s] %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*"
}

write_status() {
  .venv/bin/python - <<'PY'
import json
from datetime import datetime, timezone
from pathlib import Path

semantic_path = Path("graphify-out/.graphify_semantic_llm.json")
graph_path = Path("graphify-out/graph.json")
failures_path = Path("graphify-out/llm-failures.json")
status_path = Path("graphify-out/worker-status.json")

semantic = json.loads(semantic_path.read_text(encoding="utf-8")) if semantic_path.exists() else {}
graph = json.loads(graph_path.read_text(encoding="utf-8")) if graph_path.exists() else {}
failures = json.loads(failures_path.read_text(encoding="utf-8")) if failures_path.exists() else []

chunks_total = int(semantic.get("chunks_total") or 0)
chunks_succeeded = int(semantic.get("chunks_succeeded") or 0)
success_rate = (chunks_succeeded / chunks_total) if chunks_total else 0.0

status = {
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "finalized": bool(chunks_total and success_rate >= 0.99 and graph_path.exists()),
    "acceptance_policy": "accept if >=99% chunks succeeded and all failed chunks are documented",
    "model": semantic.get("model"),
    "reasoning_effort": semantic.get("reasoning_effort"),
    "chunks_total": chunks_total,
    "chunks_succeeded": chunks_succeeded,
    "chunks_failed": int(semantic.get("chunks_failed") or 0),
    "success_rate": round(success_rate, 6),
    "input_tokens": semantic.get("input_tokens"),
    "output_tokens": semantic.get("output_tokens"),
    "semantic_nodes": len(semantic.get("nodes", [])),
    "semantic_edges": len(semantic.get("edges", [])),
    "hyperedges": len(semantic.get("hyperedges", [])),
    "graph_nodes": len(graph.get("nodes", [])),
    "graph_links": len(graph.get("links", graph.get("edges", []))),
    "failed_chunks": failures,
}
status_path.write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
print(json.dumps(status, indent=2))
PY
}

is_acceptable_graph() {
  .venv/bin/python - "$MIN_SUCCESS_RATE" <<'PY'
import json
import sys
from pathlib import Path

min_success_rate = float(sys.argv[1])
semantic_path = Path("graphify-out/.graphify_semantic_llm.json")
graph_path = Path("graphify-out/graph.json")
if not semantic_path.exists() or not graph_path.exists():
    sys.exit(1)

data = json.loads(semantic_path.read_text(encoding="utf-8"))
total = int(data.get("chunks_total") or 0)
succeeded = int(data.get("chunks_succeeded") or 0)
if not total:
    sys.exit(1)

success_rate = succeeded / total
print(f"success_rate={success_rate:.6f} chunks={succeeded}/{total}")
sys.exit(0 if success_rate >= min_success_rate else 1)
PY
}

run_llm_attempts_if_needed() {
  if is_acceptable_graph; then
    log "graph is already acceptable; skipping LLM rerun"
    return 0
  fi

  for attempt in $(seq 1 "$MAX_ATTEMPTS"); do
    log "LLM rebuild attempt $attempt/$MAX_ATTEMPTS"
    .venv/bin/python -u -m graphify_zoro.llm_graphify \
      --input graphify-input/ocr-markdown \
      --workers 2 \
      --timeout 1200 || true

    if is_acceptable_graph; then
      log "graph became acceptable after attempt $attempt"
      return 0
    fi

    sleep_seconds=$((attempt * 300))
    log "graph still not acceptable; sleeping ${sleep_seconds}s before next attempt"
    sleep "$sleep_seconds"
  done

  if is_acceptable_graph; then
    return 0
  fi

  log "graph did not meet acceptance threshold after retries"
  return 1
}

run_query_report() {
  local tmp
  tmp="$(mktemp)"

  {
    echo "# Graphify Query Smoke Tests"
    echo
    echo "- Generated at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "- Graph: \`graphify-out/graph.json\`"
    echo "- Purpose: verify the finalized Graphify graph is queryable after the gpt-5.5/xhigh rebuild."
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
      printf '%s\n' "$output" | sed -n '1,120p'
      echo '```'
      echo
    } >> "$tmp"
  }

  run_section "Mithra / Mithras Connections" \
    .venv/bin/graphify query "What does this corpus connect Mithra or Mithras to?" --graph "$GRAPH_JSON"
  run_section "Ahura Mazda Explanation" \
    .venv/bin/graphify explain "Ahura Mazdā" --graph "$GRAPH_JSON"
  run_section "Mithra To Ahura Mazda Path" \
    .venv/bin/graphify path "Mithra" "Ahura Mazdā" --graph "$GRAPH_JSON"
  run_section "Khvarnah / Farr Royal Glory" \
    .venv/bin/graphify query "What does the graph say about Khvarnah, Farr, royal glory, and kingship?" --graph "$GRAPH_JSON"
  run_section "Sasanian Kingship" \
    .venv/bin/graphify query "What does the graph say about Sasanian kingship, divine sanction, and legitimacy?" --graph "$GRAPH_JSON"

  mv "$tmp" "$QUERY_REPORT"
}

commit_and_push() {
  git add \
    .graphify_analysis.json \
    .graphify_ast.json \
    .graphify_detect.json \
    .graphify_extract.json \
    .graphify_labels.json \
    .graphify_semantic.json \
    .graphify_semantic_llm.json \
    .graphify_transcripts.json \
    graphify-out \
    docs/query-smoke-tests.md \
    docs/STATUS.md \
    README.md \
    scripts/graphify_worker.sh \
    scripts/run_llm_rebuild_and_push.sh

  if git diff --cached --quiet; then
    log "no graph changes to commit"
  else
    git commit -m "Finalize Zoroastrian Graphify rebuild"
  fi

  git push origin main
}

log "graphify worker started"
run_llm_attempts_if_needed || log "continuing with documented partial graph"
write_status
run_query_report
commit_and_push
log "graphify worker finished"
