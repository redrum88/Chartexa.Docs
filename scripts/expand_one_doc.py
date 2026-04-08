"""
Chartexa Docs AI Expansion Script

Picks the next placeholder doc, sends it to a GitHub-hosted model for expansion,
writes the result back, and updates the frontmatter status.

Usage:
    python scripts/expand_one_doc.py [--file docs/path/to/file.md]

Environment:
    GITHUB_TOKEN   - GitHub token with models:read scope
    MODEL_ID       - Model to use (default: openai/gpt-4.1)
"""

import os
import sys
import re
import json
import glob
import random
import argparse
from pathlib import Path
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs"
GUIDELINES_PATH = Path(__file__).resolve().parent.parent / "AI_DOCS_GUIDELINES.md"
STATE_FILE = Path(__file__).resolve().parent.parent / ".ai-expansion-state.json"
DEFAULT_MODEL = "openai/gpt-4.1"
API_URL = "https://models.github.ai/inference/chat/completions"


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"expanded": [], "failed": [], "skipped": []}


def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def find_placeholder_files() -> list[Path]:
    """Find all .md files with status: placeholder in frontmatter."""
    placeholders = []
    for md in DOCS_ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        # Match YAML frontmatter
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if m:
            frontmatter = m.group(1)
            if re.search(r"^status:\s*placeholder\s*$", frontmatter, re.MULTILINE):
                placeholders.append(md)
    return sorted(placeholders)


def pick_next_file(state: dict) -> Path | None:
    """Pick the next file to expand, prioritizing by section order."""
    PRIORITY_ORDER = [
        "getting-started",
        "chart-types/2d",
        "axes",
        "interaction",
        "rendering",
        "data/data-series",
        "theming",
        "layout",
        "python",
        "performance",
        "examples",
        "chart-types/3d",
        "chart-types/gauges",
        "chart-types/instruments",
        "data/data-sources",
        "api-reference",
        "architecture",
    ]
    already = set(state.get("expanded", []) + state.get("failed", []))
    candidates = [f for f in find_placeholder_files() if str(f.relative_to(DOCS_ROOT)) not in already]

    if not candidates:
        return None

    # Sort by priority
    def sort_key(p: Path) -> tuple:
        rel = str(p.relative_to(DOCS_ROOT)).replace("\\", "/")
        for i, prefix in enumerate(PRIORITY_ORDER):
            if rel.startswith(prefix):
                return (i, rel)
        return (len(PRIORITY_ORDER), rel)

    candidates.sort(key=sort_key)
    return candidates[0]


def build_prompt(file_path: Path, guidelines: str) -> list[dict]:
    """Build the chat messages for the model."""
    content = file_path.read_text(encoding="utf-8")
    rel_path = str(file_path.relative_to(DOCS_ROOT)).replace("\\", "/")

    system_msg = f"""You are a senior technical writer producing documentation for Chartexa, a high-performance charting engine.

Your task: expand a placeholder documentation page into a full, production-quality page.

RULES (from the project's AI documentation guidelines):
{guidelines}

CRITICAL RULES:
- Output ONLY the complete markdown file content, including the YAML frontmatter
- Change the frontmatter status from "placeholder" to "draft"
- Update the last_updated timestamp to the current UTC time
- Include BOTH C# and Python code examples (use tabbed format with === "C#" and === "Python")
- Every code example must be copy-pasteable with all using/import statements
- Use real-world data values, not placeholder 1,2,3
- Use Material for MkDocs admonitions (!!!  tip, !!! warning, !!! note, !!! example)
- Do NOT include any preamble, explanation, or wrapping -- just the raw markdown
- Write for END USERS, not engine developers
- Be concise but thorough -- aim for 150-300 lines per page"""

    user_msg = f"""Expand this placeholder doc into a full documentation page.

File: {rel_path}

Current content:
```markdown
{content}
```

Write the complete expanded markdown file. Output ONLY the markdown, nothing else."""

    return [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg},
    ]


def call_model(messages: list[dict], token: str, model: str) -> str:
    """Call the GitHub Models API."""
    import urllib.request

    payload = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 8000,
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"API error {e.code}: {body}", file=sys.stderr)
        raise


def clean_response(text: str) -> str:
    """Strip markdown code fences if the model wrapped the output."""
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[len("```markdown"):].strip()
    if text.startswith("```md"):
        text = text[len("```md"):].strip()
    if text.startswith("```"):
        text = text[3:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text


def main():
    parser = argparse.ArgumentParser(description="Expand one placeholder doc")
    parser.add_argument("--file", help="Specific file to expand (relative to docs/)")
    parser.add_argument("--dry-run", action="store_true", help="Print prompt without calling API")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token and not args.dry_run:
        print("ERROR: GITHUB_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    model = os.environ.get("MODEL_ID", DEFAULT_MODEL)
    state = load_state()

    # Pick the file
    if args.file:
        target = DOCS_ROOT / args.file
        if not target.exists():
            print(f"ERROR: {target} does not exist", file=sys.stderr)
            sys.exit(1)
    else:
        target = pick_next_file(state)
        if target is None:
            print("No placeholder files remaining. Nothing to do.")
            sys.exit(0)

    rel = str(target.relative_to(DOCS_ROOT)).replace("\\", "/")
    print(f"Expanding: {rel}")

    # Load guidelines
    guidelines = ""
    if GUIDELINES_PATH.exists():
        guidelines = GUIDELINES_PATH.read_text(encoding="utf-8")

    messages = build_prompt(target, guidelines)

    if args.dry_run:
        print("\n--- SYSTEM ---")
        print(messages[0]["content"][:500] + "...")
        print("\n--- USER ---")
        print(messages[1]["content"][:500] + "...")
        print(f"\nWould expand: {rel}")
        return

    # Call the model
    try:
        result = call_model(messages, token, model)
        result = clean_response(result)

        # Validate: must have frontmatter
        if not result.startswith("---"):
            print("WARNING: Response missing frontmatter, prepending original", file=sys.stderr)
            result = "---\n" + result

        # Write
        target.write_text(result, encoding="utf-8")
        state["expanded"].append(rel)
        save_state(state)
        print(f"OK: {rel} expanded successfully")

    except Exception as e:
        print(f"FAILED: {rel} -- {e}", file=sys.stderr)
        state.setdefault("failed", []).append(rel)
        save_state(state)
        sys.exit(1)


if __name__ == "__main__":
    main()
