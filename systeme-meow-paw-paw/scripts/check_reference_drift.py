import argparse
import json
import re
import sys
from pathlib import Path


FORBIDDEN_RUNTIME_PATTERNS = [
    r"SCHEMAS & LAYERS",
    r"INDEX SYSTEM\.schema\.json",
    r"PARAMETRES SYSTEME\.regles\.schema\.json",
    r"gouvernance/INDEX SYSTEM\.json",
    r"gouvernance/PARAMETRES SYSTEME\.regles\.json",
    r"gouvernance/TAXONOMIE_PARAMETERS\.json"
]


def iter_runtime_files(root: Path) -> list[Path]:
    files = []
    for relative in [Path("SKILL.md"), Path("governance"), Path("references")]:
        target = root / relative
        if target.is_file():
            files.append(target)
        elif target.is_dir():
            for child in target.rglob("*"):
                if child.is_file():
                    files.append(child)
    return files


def is_migration_only_file(path: Path) -> bool:
    return path.name == "usage-migration.md"


def check_file(file_path: Path) -> list[dict]:
    text = file_path.read_text(encoding="utf-8")
    issues = []
    for pattern in FORBIDDEN_RUNTIME_PATTERNS:
        for match in re.finditer(pattern, text):
            issues.append(
                {
                    "pattern": pattern,
                    "match": match.group(0),
                    "position": match.start()
                }
            )
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect forbidden legacy or schema-catalog references in runtime files.")
    parser.add_argument("skill_root", help="Root folder of the skill to inspect")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    root = Path(args.skill_root)
    report = []
    total_issues = 0

    for file_path in iter_runtime_files(root):
      if is_migration_only_file(file_path):
          continue
      issues = check_file(file_path)
      if issues:
          total_issues += len(issues)
          report.append({"file": str(file_path), "issues": issues})

    if args.json:
        print(json.dumps({"issues": report, "total_issues": total_issues}, ensure_ascii=True, indent=2))
    else:
        for item in report:
            print(f"FILE {item['file']}")
            for issue in item["issues"]:
                print(f"  ISSUE pattern={issue['pattern']} match={issue['match']} pos={issue['position']}")
        print(f"TOTAL_ISSUES={total_issues}")

    return 1 if total_issues else 0


if __name__ == "__main__":
    sys.exit(main())
