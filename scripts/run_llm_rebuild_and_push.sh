#!/usr/bin/env bash
set -u

PROJECT_ROOT="/Users/ali/GRAPHIFY-zoroastrianism"
cd "$PROJECT_ROOT" || exit 1

echo "started_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "project_root=$PROJECT_ROOT"
echo "command=.venv/bin/python -u -m graphify_zoro.llm_graphify --input graphify-input/ocr-markdown --workers 2 --timeout 1200"

.venv/bin/python -u -m graphify_zoro.llm_graphify \
  --input graphify-input/ocr-markdown \
  --workers 2 \
  --timeout 1200
extract_status=$?
echo "extract_exit=$extract_status"
if [ "$extract_status" -ne 0 ]; then
  echo "extraction failed; not committing"
  exit "$extract_status"
fi

.venv/bin/python - <<'PY'
import json
import sys
from pathlib import Path

path = Path("graphify-out/.graphify_semantic_llm.json")
if not path.exists():
    print("missing graphify-out/.graphify_semantic_llm.json")
    sys.exit(2)

data = json.loads(path.read_text(encoding="utf-8"))
summary = {
    "model": data.get("model"),
    "reasoning_effort": data.get("reasoning_effort"),
    "chunks_total": data.get("chunks_total"),
    "chunks_succeeded": data.get("chunks_succeeded"),
    "chunks_failed": data.get("chunks_failed"),
    "input_tokens": data.get("input_tokens"),
    "output_tokens": data.get("output_tokens"),
}
print(json.dumps(summary, indent=2))

ok = (
    data.get("chunks_total")
    and data.get("chunks_succeeded") == data.get("chunks_total")
    and data.get("chunks_failed") == 0
)
sys.exit(0 if ok else 3)
PY
verify_status=$?
if [ "$verify_status" -ne 0 ]; then
  echo "graph verification failed; not committing"
  exit "$verify_status"
fi

git add \
  .graphify_detect.json \
  .graphify_ast.json \
  .graphify_transcripts.json \
  .graphify_semantic_llm.json \
  .graphify_semantic.json \
  .graphify_extract.json \
  graphify-out \
  scripts/run_llm_rebuild_and_push.sh

if git diff --cached --quiet; then
  echo "no graph changes to commit"
else
  git commit -m "Rebuild Zoroastrian graph with gpt-5.5 xhigh"
fi

git push origin main
push_status=$?
echo "push_exit=$push_status"
echo "finished_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
exit "$push_status"
