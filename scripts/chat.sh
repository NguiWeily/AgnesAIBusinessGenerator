#!/usr/bin/env bash
# Simple Agnes AI chat helper. Requires `AGNES_API_KEY` in the environment.

set -euo pipefail

if [ -z "${AGNES_API_KEY:-}" ]; then
  echo "Error: AGNES_API_KEY is not set. Export it and retry."
  exit 1
fi

read -r -d '' PAYLOAD <<'JSON'
{
  "model": "agnes-2.0-flash",
  "messages": [
    {"role": "user", "content": "Hello!"}
  ]
}
JSON

curl -sS https://apihub.agnes-ai.com/v1/chat/completions \
  -H "Authorization: Bearer $AGNES_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD"
