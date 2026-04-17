import argparse
import json
import re
import sys
from pathlib import Path


ALLOWED_PATTERNS = [
    re.compile(r"^skeleton_[a-z0-9_]+\.json$"),
    re.compile(r"^template_[a-z0-9_]+\.[a-z0-9]+$"),
    re.compile(r"^snippet_[a-z0-9_]+\.[a-z0-9]+$"),
    re.compile(r"^payload_[a-z0-9_]+\.[a-z0-9]+$"),
    re.compile(r"^base_[a-z0-9_]+\.[a-z0-9]+$")
]


def is_allowed(name: str) -> bool:
    return any(pattern.match(name) for pattern in ALLOWED_PATTERNS)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check naming and JSON validity of passive assets.")
    parser.add_argument("assets_dir", help="Assets directory to inspect")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    assets_dir = Path(args.assets_dir)
    issues = []
    checked = 0

    for asset in sorted(assets_dir.iterdir()):
        if not asset.is_file():
            continue
        checked += 1
        if not is_allowed(asset.name):
            issues.append({"file": str(asset), "issue": "forbidden_name_pattern"})
        if asset.suffix == ".json":
            try:
                json.loads(asset.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                issues.append({"file": str(asset), "issue": "invalid_json", "detail": str(exc)})
        if asset.name.endswith(".schema.json"):
            issues.append({"file": str(asset), "issue": "schema_catalog_forbidden_in_assets"})

    payload = {"checked_files": checked, "issue_count": len(issues), "issues": issues}

    if args.json:
        print(json.dumps(payload, ensure_ascii=True, indent=2))
    else:
        print(f"CHECKED_FILES={checked}")
        print(f"ISSUE_COUNT={len(issues)}")
        for issue in issues:
            detail = issue.get("detail", "")
            print(f"ISSUE file={issue['file']} type={issue['issue']} detail={detail}")

    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
