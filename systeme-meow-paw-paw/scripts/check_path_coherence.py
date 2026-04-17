import argparse
import json
import os
import re
import sys
from pathlib import Path


PATH_PATTERN = re.compile(r"[A-Za-z]:[\\/][^`\"'\r\n]+")


def normalize_path(raw: str) -> str:
    cleaned = raw.strip().rstrip(".,;:)")
    return os.path.normpath(cleaned.replace("/", os.sep).replace("\\", os.sep))


def extract_paths(text: str) -> list[str]:
    seen = []
    for match in PATH_PATTERN.findall(text):
        value = normalize_path(match)
        if value not in seen:
            seen.append(value)
    return seen


def check_file(file_path: Path) -> dict:
    text = file_path.read_text(encoding="utf-8")
    paths = extract_paths(text)
    results = []
    for path in paths:
        results.append(
            {
                "path": path,
                "exists": Path(path).exists()
            }
        )
    missing = [item["path"] for item in results if not item["exists"]]
    return {
        "file": str(file_path),
        "paths_found": len(results),
        "missing_count": len(missing),
        "missing_paths": missing,
        "results": results
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check explicit Windows path coherence in files.")
    parser.add_argument("files", nargs="+", help="Files to scan for explicit paths")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    report = []
    total_missing = 0
    for raw in args.files:
        file_path = Path(raw)
        item = check_file(file_path)
        total_missing += item["missing_count"]
        report.append(item)

    if args.json:
        print(json.dumps({"files": report, "total_missing": total_missing}, ensure_ascii=True, indent=2))
    else:
        for item in report:
            print(f"FILE {item['file']}")
            print(f"  paths_found={item['paths_found']}")
            print(f"  missing_count={item['missing_count']}")
            for missing in item["missing_paths"]:
                print(f"  MISSING {missing}")
        print(f"TOTAL_MISSING={total_missing}")

    return 1 if total_missing else 0


if __name__ == "__main__":
    sys.exit(main())
