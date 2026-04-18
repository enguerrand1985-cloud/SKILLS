#!/usr/bin/env python3
"""
Deterministic path checker for the active systeme-gpt-bridge skill runtime.
"""

from __future__ import annotations

import json
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_FILE = SKILL_ROOT / "governance" / "runtime.regles.json"
PROJECTS_FILE = SKILL_ROOT / "governance" / "projects.regles.json"


def as_path(value: str) -> Path:
    return Path(value.replace("/", "\\"))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def record(result: list[dict], label: str, value: str, expected: str) -> None:
    path = as_path(value)
    exists = path.exists()
    entry = {
        "label": label,
        "path": str(path),
        "expected": expected,
        "exists": exists,
        "type": "dir" if exists and path.is_dir() else "file"
    }
    result.append(entry)


def main() -> int:
    results: list[dict] = []
    missing = 0

    if not RUNTIME_FILE.exists() or not PROJECTS_FILE.exists():
        print(json.dumps({
            "status": "missing_governance",
            "runtime_file": str(RUNTIME_FILE),
            "projects_file": str(PROJECTS_FILE)
        }, ensure_ascii=True, indent=2))
        return 1

    runtime_data = load_json(RUNTIME_FILE)
    projects_data = load_json(PROJECTS_FILE)

    for key, value in runtime_data.get("rules", {}).get("roots", {}).items():
        record(results, f"root:{key}", value, "dir")

    for scope, item in projects_data.get("rules", {}).get("projects", {}).items():
        prefix = f"project:{scope}"
        for field in (
            "prompt_file",
            "project_dir",
            "attachments_dir",
            "index_file",
            "journal_file",
            "ecosystem_context",
            "image_config_file"
        ):
            value = item.get(field)
            if value:
                expected = "dir" if field in {"project_dir", "attachments_dir"} else "file"
                record(results, f"{prefix}:{field}", value, expected)

    for scope, item in projects_data.get("rules", {}).get("gpts", {}).items():
        prefix = f"gpt:{scope}"
        for field in (
            "prompt_file",
            "attachments_dir",
            "journal_file",
            "ecosystem_context"
        ):
            value = item.get(field)
            if value:
                expected = "dir" if field == "attachments_dir" else "file"
                record(results, f"{prefix}:{field}", value, expected)

    for entry in results:
        if not entry["exists"]:
            missing += 1

    summary = {
        "status": "ok" if missing == 0 else "missing_paths",
        "checked": len(results),
        "missing": missing,
        "results": results
    }
    print(json.dumps(summary, ensure_ascii=True, indent=2))
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
