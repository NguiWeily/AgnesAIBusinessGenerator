#!/usr/bin/env python3
"""Minimal Agnes AI chat example using requests."""

import os
import sys
import json
from typing import Any

import requests


def main() -> None:
    api_key = os.getenv("AGNES_API_KEY")
    if not api_key:
        print("Error: AGNES_API_KEY not set in environment.")
        sys.exit(1)

    url = "https://apihub.agnes-ai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload: Any = {
        "model": "agnes-2.0-flash",
        "messages": [{"role": "user", "content": "Hello!"}],
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    print(json.dumps(resp.json(), indent=2))


if __name__ == "__main__":
    main()
