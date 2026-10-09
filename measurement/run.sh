#!/usr/bin/env bash
# Business Frameworks — with/without measurement runner (Claude Code headless).
# Usage: ./run.sh <model: haiku|opus|sonnet> <condition: with|without|forced> [question ids...]
# Each run: a fresh empty working directory (no CLAUDE.md), the question as the only prompt,
# tools limited to WebSearch, WebFetch and curl, 12 turns max; "with" adds --plugin-dir <plugin>.
# Output: results/<model>/<condition>/<qid>.jsonl — Claude Code's stream-json: every assistant
# message (tool_use blocks show Skill / Bash / WebSearch / WebFetch calls) and the final
# "result" record with usage per iteration, num_turns, total_cost_usd, duration_ms and the answer.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
MODEL="${1:?model}"; COND="${2:?with|without|forced|paid}"; shift 2
PLUGIN="${PLUGIN_DIR:-/mnt/user-data/outputs/Work/github/business-frameworks}"
OUT="$HERE/results/$MODEL/$COND"; mkdir -p "$OUT"
IDS=("$@"); if [ ${#IDS[@]} -eq 0 ]; then mapfile -t IDS < <(python3 -c "import json;[print(q['id']) for q in json.load(open('$HERE/questions.json'))]"); fi
for QID in "${IDS[@]}"; do
  if [ -s "$OUT/$QID.jsonl" ]; then echo "skip $MODEL/$COND/$QID (exists)"; continue; fi
  Q="$(python3 -c "import json,sys;print([q for q in json.load(open('$HERE/questions.json')) if q['id']=='$QID'][0]['question'])")"
  WD="$(mktemp -d /tmp/ab-XXXXXX)"
  ARGS=(-p "$Q" --model "$MODEL" --output-format stream-json --verbose --max-turns 12 --no-session-persistence
        --setting-sources project --allowedTools "WebSearch" "WebFetch" "Bash(curl *)" "Read" --disallowedTools "Projects" "Glob" "Grep" "Write" "Edit" )
  if [ "$COND" = "with" ]; then ARGS+=(--plugin-dir "$PLUGIN"); fi
  # "forced" = the operator-configured case: the plugin is installed AND a one-line standing instruction says to use it.
  # "paid" = forced, with a local plugin variant whose references carry the ten decision nodes' text (as an agent that bought them would hold it).
  if [ "$COND" = "paid" ]; then ARGS+=(--plugin-dir "$HERE/plugin-paid" --append-system-prompt "For any question about running a business — value, cash flow, cost of capital, growth, pricing, a specific business decision — load and follow the business-frameworks skill before answering."); fi
  if [ "$COND" = "forced" ]; then ARGS+=(--plugin-dir "$PLUGIN" --append-system-prompt "For any question about running a business — value, cash flow, cost of capital, growth, pricing, a specific business decision — load and follow the business-frameworks skill before answering."); fi
  echo "run $MODEL/$COND/$QID"
  # Scrubbed environment: only PATH/HOME, the proxy and certificate variables, and any credential variable.
  # This drops the harness-level context a parent session would inherit (attached project, extra MCP tools).
  KEEP=(); for v in HOME PATH HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy NODE_EXTRA_CA_CERTS SSL_CERT_FILE REQUESTS_CA_BUNDLE CURL_CA_BUNDLE ANTHROPIC_BASE_URL ANTHROPIC_AUTH_TOKEN ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN TERM LANG; do [ -n "${!v:-}" ] && KEEP+=("$v=${!v}"); done
  ( cd "$WD" && timeout 600 env -i "${KEEP[@]}" claude "${ARGS[@]}" > "$OUT/$QID.jsonl" 2> "$OUT/$QID.err" ) || echo "  non-zero exit for $QID (see $OUT/$QID.err)"
  rm -rf "$WD"
  python3 "$HERE/summarize_run.py" "$OUT/$QID.jsonl"
done
