#!/bin/bash
# Run a GPT review of one chapter through the Codex CLI, isolated from the project.
# Usage: tools/run_codex_review.sh STEM [MODEL] [EFFORT]
#   defaults: MODEL=gpt-6-astra EFFORT=high
# Rebuilds notes/review-packets/STEM.md, feeds it on stdin to `codex exec` running
# in an empty directory with a read-only sandbox and no user config, saves the
# final message to notes/reviews/STEM-gpt.md and the event log to
# notes/reviews/runs/STEM-gpt.jsonl, and records the model and effort that the
# Codex session file reports in notes/reviews/runs/STEM-gpt.model.
set -euo pipefail
stem=$1; model=${2:-gpt-6-astra}; effort=${3:-high}
root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
empty=$(mktemp -d)
python3 -I tools/make_review_packet.py "$stem"
mkdir -p notes/reviews/runs
codex exec --ignore-user-config --skip-git-repo-check -s read-only -C "$empty" \
  -m "$model" -c "model_reasoning_effort=\"$effort\"" --json \
  -o "notes/reviews/$stem-gpt.md" \
  "The review packet is in the <stdin> block below. It is self-contained: follow its instructions. Do not run commands or read files; you need nothing beyond the packet. Your final message is the review itself, in Markdown." \
  < "notes/review-packets/$stem.md" \
  > "notes/reviews/runs/$stem-gpt.jsonl" 2> "notes/reviews/runs/$stem-gpt.stderr"
rmdir "$empty"
thread=$(python3 -I -c 'import json,sys; print(json.loads(open(sys.argv[1]).readline())["thread_id"])' "notes/reviews/runs/$stem-gpt.jsonl")
session=$(grep -rl "$thread" ~/.codex/sessions | head -1)
{ echo "thread: $thread"; echo "session: $session"
  grep -o '"model":"[^"]*"\|"effort":"[^"]*"' "$session" | sort | uniq -c
  printf 'tool calls: '; grep -c '"type":"function_call"' "$session" || true
  grep -o '"usage":{[^}]*}' "notes/reviews/runs/$stem-gpt.jsonl" | tail -1
} > "notes/reviews/runs/$stem-gpt.model"
cat "notes/reviews/runs/$stem-gpt.model"
