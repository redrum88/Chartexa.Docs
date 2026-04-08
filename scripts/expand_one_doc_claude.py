"""
Claude variant of the doc expansion script.
Same logic as expand_one_doc.py but calls Anthropic Claude API.

Environment:
    ANTHROPIC_API_KEY - Anthropic API key
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs"
GUIDELINES_PATH = Path(__file__).resolve().parent.parent / "AI_DOCS_GUIDELINES.md"
STATE_FILE = Path(__file__).resolve().parent.parent / ".ai-expansion-state-claude.json"
API_URL = "https://api.anthropic.com/v1/messages"

# Re-use helpers from the main script
sys.path.insert(0, str(Path(__file__).parent))
from expand_one_doc import (
    load_state as _load_state,
    find_placeholder_files,
    pick_next_file,
    clean_response,
)


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"expanded": [], "failed": [], "skipped": []}


def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def call_claude(system_prompt: str, user_prompt: str, api_key: str) -> str:
    import urllib.request

    payload = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 8000,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_prompt}],
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data["content"][0]["text"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Specific file to expand")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key and not args.dry_run:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    state = load_state()

    if args.file:
        target = DOCS_ROOT / args.file
    else:
        target = pick_next_file(state)
        if target is None:
            print("No placeholder files remaining.")
            sys.exit(0)

    rel = str(target.relative_to(DOCS_ROOT)).replace("\\", "/")
    print(f"Expanding: {rel}")

    guidelines = GUIDELINES_PATH.read_text(encoding="utf-8") if GUIDELINES_PATH.exists() else ""
    content = target.read_text(encoding="utf-8")

    system_prompt = f"""You are a senior technical writer producing documentation for Chartexa, a high-performance charting engine.
Expand placeholder docs into full, production-quality pages.

RULES:
{guidelines}

Output ONLY the complete markdown file. Change status to "draft". Include C# and Python examples."""

    user_prompt = f"Expand this placeholder ({rel}):\n\n```markdown\n{content}\n```"

    if args.dry_run:
        print(f"Would expand: {rel}")
        return

    try:
        result = clean_response(call_claude(system_prompt, user_prompt, api_key))
        if not result.startswith("---"):
            result = "---\n" + result
        target.write_text(result, encoding="utf-8")
        state["expanded"].append(rel)
        save_state(state)
        print(f"OK: {rel}")
    except Exception as e:
        print(f"FAILED: {rel} -- {e}", file=sys.stderr)
        state.setdefault("failed", []).append(rel)
        save_state(state)
        sys.exit(1)


if __name__ == "__main__":
    main()
