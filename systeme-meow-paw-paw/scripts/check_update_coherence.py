import argparse
import json
import os
import sys
from pathlib import Path


TEXT_SUFFIXES = {".json", ".md", ".txt", ".yaml", ".yml", ".csv", ".py"}
SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".playwright-cli"
}


def normalize_path(raw: str) -> str:
    return os.path.normcase(os.path.normpath(raw.replace("/", os.sep).replace("\\", os.sep)))


def resolve_rooted_path(index_data: dict, source: dict) -> Path:
    root_key = source.get("path_root")
    relative_path = source.get("path", "")
    root_paths = index_data.get("root_paths", {})
    if not root_key or root_key not in root_paths:
        return Path(relative_path)
    return Path(root_paths[root_key]) / relative_path


def load_index_sources(index_path: Path) -> dict:
    return json.loads(index_path.read_text(encoding="utf-8-sig"))


def resolve_source(index_data: dict, target: Path) -> dict | None:
    target_norm = normalize_path(str(target.resolve()))
    for source in index_data.get("sources", []):
        candidate = resolve_rooted_path(index_data, source)
        if normalize_path(str(candidate)) == target_norm:
            return source
    return None


def collect_reverse_dependencies(index_data: dict, source_id: str) -> list[dict]:
    results = []
    for source in index_data.get("sources", []):
        depends_on = source.get("depends_on", [])
        if source_id in depends_on:
            results.append(source)
    return results


def iter_text_files(root: Path) -> list[Path]:
    files = []
    for current_root, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS]
        for filename in filenames:
            path = Path(current_root) / filename
            if path.suffix.lower() in TEXT_SUFFIXES:
                files.append(path)
    return files


def find_matches(root: Path, patterns: list[str], exclude: Path | None = None) -> list[dict]:
    hits = []
    lowered_patterns = [pattern for pattern in patterns if pattern]
    for file_path in iter_text_files(root):
        if exclude is not None and normalize_path(str(file_path)) == normalize_path(str(exclude)):
            continue
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        matched = []
        for pattern in lowered_patterns:
            if pattern in text:
                matched.append(pattern)
        if matched:
            hits.append({"file": str(file_path), "matched_patterns": matched})
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Check update coherence around a Meow truth-file patch.")
    parser.add_argument("target_file", help="Target file being updated")
    parser.add_argument("--index-sources", help="Path to INDEX SOURCES.json")
    parser.add_argument("--workspace-root", help="Workspace root used for explicit reference scans")
    parser.add_argument("--needle", action="append", default=[], help="Literal values to scan in text files")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    target_file = Path(args.target_file).resolve()
    workspace_root = Path(args.workspace_root).resolve() if args.workspace_root else target_file.parent

    report = {
        "target_file": str(target_file),
        "index_source_match": None,
        "declared_dependencies": [],
        "reverse_dependencies": [],
        "explicit_reference_hits": [],
        "needle_hits": []
    }

    search_patterns = [target_file.name]

    if args.index_sources:
        index_path = Path(args.index_sources).resolve()
        index_data = load_index_sources(index_path)
        source = resolve_source(index_data, target_file)
        if source is not None:
            report["index_source_match"] = {
                "id": source.get("id"),
                "path": source.get("path"),
                "support_layer": source.get("support_layer"),
                "truth_status": source.get("truth_status")
            }
            report["declared_dependencies"] = source.get("depends_on", [])
            reverse_dependencies = collect_reverse_dependencies(index_data, source.get("id"))
            report["reverse_dependencies"] = [
                {
                    "id": item.get("id"),
                    "path": item.get("path"),
                    "truth_status": item.get("truth_status")
                }
                for item in reverse_dependencies
            ]
            search_patterns.append(source.get("id", ""))
            search_patterns.append(source.get("path", ""))

    report["explicit_reference_hits"] = find_matches(workspace_root, search_patterns, exclude=target_file)
    report["needle_hits"] = find_matches(workspace_root, args.needle, exclude=target_file) if args.needle else []

    if args.json:
        print(json.dumps(report, ensure_ascii=True, indent=2))
    else:
        print(f"TARGET_FILE={report['target_file']}")
        if report["index_source_match"] is None:
            print("INDEX_SOURCE_MATCH=NONE")
        else:
            print(f"INDEX_SOURCE_MATCH={report['index_source_match']['id']}")
            print(f"DECLARED_DEPENDENCIES={','.join(report['declared_dependencies'])}")
            print(f"REVERSE_DEPENDENCIES={','.join(item['id'] for item in report['reverse_dependencies'])}")
        print(f"EXPLICIT_REFERENCE_HITS={len(report['explicit_reference_hits'])}")
        for item in report["explicit_reference_hits"]:
            print(f"  REF file={item['file']} matched={','.join(item['matched_patterns'])}")
        print(f"NEEDLE_HITS={len(report['needle_hits'])}")
        for item in report["needle_hits"]:
            print(f"  NEEDLE file={item['file']} matched={','.join(item['matched_patterns'])}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
