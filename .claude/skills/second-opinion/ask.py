#!/usr/bin/env python3
"""Ask a free OpenRouter model a question. Prompt comes from stdin.

Usage:
  ask.py --list                     list free models currently available
  echo "question" | ask.py          ask the default free model
  echo "question" | ask.py -m ID    ask a specific model (must end in ':free')
  echo "question" | ask.py -n 2     ask the first 2 working free models

Auth: uses $OPENROUTER_API_KEY if set; otherwise sends a placeholder and
relies on the environment's network proxy to inject the saved credential.
Only models whose id ends in ':free' are ever called.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://openrouter.ai/api/v1"
# Tried in order; anything missing from the live free list is skipped.
PREFERRED = [
    "google/gemma-4-31b-it:free",
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "cohere/north-mini-code:free",
    "google/gemma-4-26b-a4b-it:free",
]
SYSTEM = (
    "You are giving a second opinion to another AI assistant. Be direct and "
    "specific. Point out errors, risks and missed alternatives. If you are "
    "unsure, say so. Do not pad."
)


def call(path, body=None, timeout=120):
    key = os.environ.get("OPENROUTER_API_KEY") or "proxy-injected"
    req = urllib.request.Request(
        API + path,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def free_models():
    return [m["id"] for m in call("/models")["data"] if m["id"].endswith(":free")]


def ask(model, prompt, max_tokens):
    out = call(
        "/chat/completions",
        {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": max_tokens,
        },
    )
    if "error" in out:
        raise RuntimeError(json.dumps(out["error"])[:300])
    text = (out["choices"][0]["message"].get("content") or "").strip()
    if not text:
        raise RuntimeError("empty reply")
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("-m", "--model")
    ap.add_argument("-n", type=int, default=1, help="how many models to ask")
    ap.add_argument("--max-tokens", type=int, default=2000)
    a = ap.parse_args()

    available = free_models()
    if a.list:
        print("\n".join(available))
        return 0

    if a.model:
        if not a.model.endswith(":free"):
            sys.exit("refusing: only ':free' models are allowed")
        candidates = [a.model]
    else:
        candidates = [m for m in PREFERRED if m in available]
        candidates += [m for m in available if m not in candidates]

    prompt = sys.stdin.read().strip()
    if not prompt:
        sys.exit("no prompt on stdin")

    answered = 0
    for model in candidates:
        try:
            text = ask(model, prompt, a.max_tokens)
        except urllib.error.HTTPError as e:
            print(f"[{model}] HTTP {e.code}: {e.read()[:200].decode(errors='replace')}", file=sys.stderr)
            continue
        except Exception as e:  # network errors, empty replies, API errors
            print(f"[{model}] failed: {e}", file=sys.stderr)
            continue
        print(f"=== {model} ===\n{text}\n")
        answered += 1
        if answered >= a.n:
            break
    if not answered:
        sys.exit("no free model answered")
    return 0


if __name__ == "__main__":
    sys.exit(main())
