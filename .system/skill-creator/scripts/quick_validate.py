#!/usr/bin/env python3
"""
Quick validation script for skills.

Layer 1: standard Codex skill compatibility
Layer 2: strict NORME_SKILL checks for personal skills only
"""

import json
import re
import sys
from pathlib import Path

import yaml

MAX_SKILL_NAME_LENGTH = 64
RUNTIME_ROOT = Path(__file__).resolve().parent.parent / "references" / "norme-skill"


def load_runtime_json(filename):
    path = RUNTIME_ROOT / filename
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path):
    return path.read_text(encoding="utf-8")


def extract_frontmatter(content):
    if not content.startswith("---"):
        return None, "No YAML frontmatter found"

    match = re.match(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)
    if not match:
        return None, "Invalid frontmatter format"

    frontmatter_text = match.group(1)
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        return None, f"Invalid YAML in frontmatter: {exc}"

    if not isinstance(frontmatter, dict):
        return None, "Frontmatter must be a YAML dictionary"

    return frontmatter, None


def validate_standard(skill_path):
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found", None, None

    content = read_text(skill_md)
    frontmatter, error = extract_frontmatter(content)
    if error:
        return False, error, None, None

    allowed_properties = {"name", "description", "license", "allowed-tools", "metadata"}
    unexpected_keys = set(frontmatter.keys()) - allowed_properties
    if unexpected_keys:
        allowed = ", ".join(sorted(allowed_properties))
        unexpected = ", ".join(sorted(unexpected_keys))
        return (
            False,
            f"Unexpected key(s) in SKILL.md frontmatter: {unexpected}. Allowed properties are: {allowed}",
            None,
            None,
        )

    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter", None, None
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter", None, None

    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}", None, None
    name = name.strip()
    if name:
        if not re.match(r"^[a-z0-9-]+$", name):
            return (
                False,
                f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)",
                None,
                None,
            )
        if name.startswith("-") or name.endswith("-") or "--" in name:
            return (
                False,
                f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens",
                None,
                None,
            )
        if len(name) > MAX_SKILL_NAME_LENGTH:
            return (
                False,
                f"Name is too long ({len(name)} characters). Maximum is {MAX_SKILL_NAME_LENGTH} characters.",
                None,
                None,
            )

    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}", None, None
    description = description.strip()
    if description:
        if "<" in description or ">" in description:
            return False, "Description cannot contain angle brackets (< or >)", None, None
        if len(description) > 1024:
            return (
                False,
                f"Description is too long ({len(description)} characters). Maximum is 1024 characters.",
                None,
                None,
            )

    return True, "Skill is valid!", frontmatter, content


def normalize_path(path):
    return str(path.resolve()).replace("\\", "/").lower()


def is_strict_personal_skill(skill_path, core_schema):
    path_str = normalize_path(skill_path)
    include_markers = core_schema["strict_personal_path_markers"]
    exclude_markers = core_schema["strict_excluded_path_markers"]
    return any(marker in path_str for marker in include_markers) and not any(
        marker in path_str for marker in exclude_markers
    )


def extract_top_level_sections(content):
    return re.findall(r"^# (.+)$", content, flags=re.MULTILINE)


def extract_section_block(content, section_name, next_section_name=None):
    pattern = rf"^# {re.escape(section_name)}\r?\n(.*?)(?=^# |\Z)"
    match = re.search(pattern, content, flags=re.MULTILINE | re.DOTALL)
    if not match:
        return ""
    return match.group(1).strip()


def validate_required_directories(skill_path, core_schema):
    for directory_name in core_schema["required_directories"]:
        path = skill_path / directory_name
        if not path.exists() or not path.is_dir():
            return False, f"Missing required directory: {directory_name}/"
    return True, None


def validate_section_order(content, core_schema):
    actual_sections = extract_top_level_sections(content)
    expected_sections = core_schema["skill_md"]["required_top_level_sections"]
    if actual_sections != expected_sections:
        return (
            False,
            "Top-level sections in SKILL.md do not match the canonical fixed order. "
            f"Expected: {expected_sections} | Actual: {actual_sections}",
        )
    return True, None


def validate_routing_markers(content, validation_schema):
    order_section = extract_section_block(content, "ORDRE DE LECTURE")
    routing_section = extract_section_block(content, "ROUTAGE INTERNE")

    order_required = validation_schema["routing_markers"]["order_section_requires"]
    order_conditionals = validation_schema["routing_markers"]["conditional_markers"]
    routing_required = validation_schema["routing_markers"]["routing_always"]
    routing_any = validation_schema["routing_markers"]["routing_conditional_any"]

    if not any(marker.lower() in order_section.lower() for marker in order_required):
        return False, "ORDRE DE LECTURE must declare a 'Toujours lire' style marker."
    if not any(marker.lower() in order_section.lower() for marker in order_conditionals):
        return False, "ORDRE DE LECTURE must declare at least one conditional read marker."
    if not any(marker.lower() in routing_section.lower() for marker in routing_required):
        return False, "ROUTAGE INTERNE must declare a 'Toujours lu:' style marker."
    if not any(marker.lower() in routing_section.lower() for marker in routing_any):
        return False, "ROUTAGE INTERNE must distinguish always-read vs targeted/conditional paths."
    return True, None


def validate_governance(skill_path, validation_schema, governance_schema):
    governance_dir = skill_path / "governance"
    pattern = re.compile(validation_schema["governance_module_pattern"])
    forbidden_markers = governance_schema["forbidden_name_markers"]

    for path in governance_dir.rglob("*"):
        if "__pycache__" in path.parts:
            continue
        if path.is_dir():
            continue
        if path.suffix.lower() != ".json":
            return False, f"governance/ must contain JSON files only: {path.name}"
        if not pattern.match(path.name):
            return False, f"Invalid governance filename: {path.name}"
        lower_name = path.name.lower()
        if any(marker in lower_name for marker in forbidden_markers):
            return False, f"Forbidden governance naming marker detected: {path.name}"

    return True, None


def validate_references(skill_path, validation_schema):
    references_dir = skill_path / "references"
    pattern = re.compile(validation_schema["reference_pattern"])

    for path in references_dir.rglob("*"):
        if "__pycache__" in path.parts:
            continue
        if path.is_dir():
            continue
        if path.suffix.lower() != ".md":
            return False, f"references/ must contain Markdown files only: {path.name}"
        if not pattern.match(path.name):
            return False, f"Invalid references filename: {path.name}"

    return True, None


def validate_scripts(skill_path, validation_schema):
    scripts_dir = skill_path / "scripts"
    pattern = re.compile(validation_schema["script_pattern"])
    allowed_verbs = set(validation_schema["allowed_script_verbs"])

    for path in scripts_dir.rglob("*"):
        if "__pycache__" in path.parts:
            continue
        if path.is_dir():
            continue
        if path.suffix.lower() != ".py":
            return False, f"scripts/ must contain Python files only: {path.name}"
        match = pattern.match(path.name)
        if not match:
            return False, f"Invalid script filename: {path.name}"
        if match.group("verb") not in allowed_verbs:
            return False, f"Script verb is not allowed by NORME_SKILL: {path.name}"

    return True, None


def validate_assets(skill_path, validation_schema, assets_schema):
    assets_dir = skill_path / "assets"
    file_pattern = re.compile(validation_schema["asset_pattern"])
    dir_pattern = re.compile(validation_schema["asset_directory_pattern"])
    forbidden_suffixes = assets_schema["forbidden_suffixes"]
    forbidden_markers = assets_schema["forbidden_markers"]

    for path in assets_dir.rglob("*"):
        if "__pycache__" in path.parts:
            continue
        lower_name = path.name.lower()
        if any(lower_name.endswith(suffix) for suffix in forbidden_suffixes):
            return False, f"Forbidden asset file type detected: {path.name}"
        if any(marker in lower_name for marker in forbidden_markers):
            return False, f"Forbidden asset naming marker detected: {path.name}"
        if path.is_dir():
            if not dir_pattern.match(path.name):
                return False, f"Invalid asset directory name: {path.name}"
            continue
        if not file_pattern.match(path.name):
            return False, f"Invalid asset filename: {path.name}"

    return True, None


def validate_personal_norm(skill_path, content):
    core_schema = load_runtime_json("schema.core.json")
    validation_schema = load_runtime_json("schema.validation.json")
    governance_schema = load_runtime_json("schema.governance.json")
    assets_schema = load_runtime_json("schema.assets.json")

    checks = [
        validate_required_directories(skill_path, core_schema),
        validate_section_order(content, core_schema),
        validate_routing_markers(content, validation_schema),
        validate_governance(skill_path, validation_schema, governance_schema),
        validate_references(skill_path, validation_schema),
        validate_scripts(skill_path, validation_schema),
        validate_assets(skill_path, validation_schema, assets_schema),
    ]

    for valid, message in checks:
        if not valid:
            return False, message

    return True, "Skill is valid! (standard + norme_skill)"


def validate_skill(skill_path):
    skill_path = Path(skill_path)
    valid, message, _, content = validate_standard(skill_path)
    if not valid:
        return False, message

    core_schema = load_runtime_json("schema.core.json")
    if is_strict_personal_skill(skill_path, core_schema):
        return validate_personal_norm(skill_path, content)

    return True, "Skill is valid! (standard compatibility)"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
