#!/usr/bin/env python3
"""
Skill Initializer - creates a new personal skill scaffold aligned with NORME_SKILL.

Usage:
    init_skill.py <skill-name> --path <path> [--resources scripts,references,assets] [--examples] [--interface key=value]
"""

import argparse
import json
import re
import sys
from pathlib import Path

from generate_openai_yaml import write_openai_yaml

MAX_SKILL_NAME_LENGTH = 64
ALLOWED_RESOURCES = {"scripts", "references", "assets"}
RUNTIME_ROOT = Path(__file__).resolve().parent.parent / "references" / "norme-skill"

PLACEHOLDER_BY_SECTION = {
    "MISSION": "[TODO: definir la competence specialisee du skill et sa mission principale.]",
    "PORTEE": "- Domaine couvert: [TODO]\n- Hors perimetre: [TODO]",
    "CONDITIONS D'ACTIVATION": (
        "- Activer ce skill quand: [TODO]\n"
        "- Ne pas l'activer quand: [TODO]"
    ),
    "ORDRE DE LECTURE": (
        "1. Toujours lire `SKILL.md`.\n"
        "2. Toujours lire seulement le noyau minimal utile si le skill dispose d'un routeur leger.\n"
        "3. Lire les modules cibles seulement si le sous-cas l'exige.\n"
        "4. Lire les references detaillees seulement si le detail operatoire devient necessaire.\n"
        "5. Lire les schemas lourds seulement en validation finale ou sur mutation structurelle."
    ),
    "ROUTAGE INTERNE": (
        "- Toujours lu: `SKILL.md`, puis [TODO: routeur minimal ou `N/A`].\n"
        "- Lu a la demande: [TODO].\n"
        "- Validation finale seulement si utile: [TODO ou `N/A`].\n"
        "- Si aucun sous-cas n'est resolu, produire un STOP explicite."
    ),
    "WORKFLOWS / PROTOCOLES": (
        "1. [TODO: workflow principal]\n"
        "2. [TODO: workflow secondaire ou `N/A`]"
    ),
    "REGLES NON NEGOCIABLES": (
        "- Ne pas embarquer de data verite externe dans le skill.\n"
        "- Garder le `toujours lu` leger.\n"
        "- Ne pas creer de modules decoratifs."
    ),
    "CONDITIONS DE STOP": (
        "- STOP si le sous-cas reste ambigu.\n"
        "- STOP si une source critique manque.\n"
        "- STOP si la mutation demandee depasse la portee du skill."
    ),
    "FORMAT DE SORTIE": (
        "- mode: [TODO]\n"
        "- status: [TODO]\n"
        "- target: [TODO]\n"
        "- result: [TODO]\n"
        "- blockers: [TODO ou `Aucun`]\n"
        "- next_action: [TODO]\n"
        "- artifacts: [TODO ou `Aucun`]"
    ),
    "REFERENCES": (
        "- [TODO: mapping-<skill>.md si utile]\n"
        "- [TODO: usage-<module>.md si utile]\n"
        "- [TODO: sources-externes.md si utile]"
    ),
}

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Example deterministic support script for {skill_name}

Replace this placeholder or delete it if the skill does not need an executable helper.
"""


def main():
    print("Placeholder script for {skill_name}")


if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# Mapping for {skill_title}

This is a placeholder mapping file aligned with the personal skill norm.
Replace it with a real mapping, or delete it if the skill does not need one.
"""

EXAMPLE_ASSET = """Placeholder asset file aligned with the personal skill norm.

Replace or delete this file if the skill does not need a template asset.
"""


def load_runtime_core():
    runtime_path = RUNTIME_ROOT / "schema.core.json"
    try:
        return json.loads(runtime_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"[ERROR] Unable to load runtime norme file: {runtime_path} -> {exc}")
        sys.exit(1)


def normalize_skill_name(skill_name):
    normalized = skill_name.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    normalized = normalized.strip("-")
    normalized = re.sub(r"-{2,}", "-", normalized)
    return normalized


def title_case_skill_name(skill_name):
    return " ".join(word.capitalize() for word in skill_name.split("-"))


def parse_resources(raw_resources):
    if not raw_resources:
        return []
    resources = [item.strip() for item in raw_resources.split(",") if item.strip()]
    invalid = sorted({item for item in resources if item not in ALLOWED_RESOURCES})
    if invalid:
        allowed = ", ".join(sorted(ALLOWED_RESOURCES))
        print(f"[ERROR] Unknown resource type(s): {', '.join(invalid)}")
        print(f"   Allowed: {allowed}")
        sys.exit(1)
    deduped = []
    seen = set()
    for resource in resources:
        if resource not in seen:
            deduped.append(resource)
            seen.add(resource)
    return deduped


def build_skill_template(skill_name, runtime_core):
    skill_title = title_case_skill_name(skill_name)
    sections = runtime_core["skill_md"]["required_top_level_sections"]
    parts = [
        "---",
        f"name: {skill_name}",
        'description: "[TODO: Complete and informative explanation of what the skill does and when to use it. Include the exact user intents and contexts that should trigger this skill.]"',
        "---",
        "",
    ]
    for section in sections:
        parts.append(f"# {section}")
        parts.append(PLACEHOLDER_BY_SECTION.get(section, "[TODO]"))
        parts.append("")
    parts.append(f"<!-- Generated scaffold for {skill_title}. Keep only useful content. -->")
    parts.append("")
    return "\n".join(parts)


def create_canonical_dirs(skill_dir, runtime_core):
    for directory_name in runtime_core["required_directories"]:
        (skill_dir / directory_name).mkdir(exist_ok=True)
        print(f"[OK] Created {directory_name}/")


def create_example_files(skill_dir, skill_name, skill_title, resources):
    for resource in resources:
        if resource == "scripts":
            script_path = skill_dir / "scripts" / "check_example.py"
            script_path.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name), encoding="utf-8")
            script_path.chmod(0o755)
            print("[OK] Created scripts/check_example.py")
        elif resource == "references":
            reference_path = skill_dir / "references" / f"mapping-{skill_name}.md"
            reference_path.write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title), encoding="utf-8")
            print(f"[OK] Created references/mapping-{skill_name}.md")
        elif resource == "assets":
            asset_path = skill_dir / "assets" / "template_example.txt"
            asset_path.write_text(EXAMPLE_ASSET, encoding="utf-8")
            print("[OK] Created assets/template_example.txt")


def init_skill(skill_name, path, resources, include_examples, interface_overrides):
    runtime_core = load_runtime_core()
    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"[ERROR] Skill directory already exists: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"[OK] Created skill directory: {skill_dir}")
    except Exception as exc:
        print(f"[ERROR] Error creating directory: {exc}")
        return None

    create_canonical_dirs(skill_dir, runtime_core)

    skill_md_path = skill_dir / "SKILL.md"
    skill_content = build_skill_template(skill_name, runtime_core)
    try:
        skill_md_path.write_text(skill_content, encoding="utf-8")
        print("[OK] Created SKILL.md")
    except Exception as exc:
        print(f"[ERROR] Error creating SKILL.md: {exc}")
        return None

    try:
        result = write_openai_yaml(skill_dir, skill_name, interface_overrides)
        if not result:
            return None
    except Exception as exc:
        print(f"[ERROR] Error creating agents/openai.yaml: {exc}")
        return None

    if include_examples:
        skill_title = title_case_skill_name(skill_name)
        try:
            create_example_files(skill_dir, skill_name, skill_title, resources)
        except Exception as exc:
            print(f"[ERROR] Error creating example files: {exc}")
            return None

    print(f"\n[OK] Skill '{skill_name}' initialized successfully at {skill_dir}")
    print("\nNext steps:")
    print("1. Complete SKILL.md using the fixed section order from NORME_SKILL.")
    print("2. Keep governance, references, scripts, and assets light unless the skill truly needs more structure.")
    if include_examples:
        print("3. Replace or delete the seeded example files if they are not useful.")
    else:
        print("3. Add only the resource files that are genuinely useful.")
    print("4. Regenerate agents/openai.yaml if the interface metadata should change.")
    print("5. Run quick_validate.py before treating the skill as ready.")
    print("6. Forward-test complex skills on real requests once the scaffold is filled.")

    return skill_dir


def main():
    parser = argparse.ArgumentParser(
        description="Create a new personal skill scaffold aligned with NORME_SKILL.",
    )
    parser.add_argument("skill_name", help="Skill name (normalized to hyphen-case)")
    parser.add_argument("--path", required=True, help="Output directory for the skill")
    parser.add_argument(
        "--resources",
        default="",
        help="Optional seeded example resources: scripts,references,assets",
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Create example files inside the selected canonical directories",
    )
    parser.add_argument(
        "--interface",
        action="append",
        default=[],
        help="Interface override in key=value format (repeatable)",
    )
    args = parser.parse_args()

    raw_skill_name = args.skill_name
    skill_name = normalize_skill_name(raw_skill_name)
    if not skill_name:
        print("[ERROR] Skill name must include at least one letter or digit.")
        sys.exit(1)
    if len(skill_name) > MAX_SKILL_NAME_LENGTH:
        print(
            f"[ERROR] Skill name '{skill_name}' is too long ({len(skill_name)} characters). "
            f"Maximum is {MAX_SKILL_NAME_LENGTH} characters."
        )
        sys.exit(1)
    if skill_name != raw_skill_name:
        print(f"Note: Normalized skill name from '{raw_skill_name}' to '{skill_name}'.")

    resources = parse_resources(args.resources)
    if args.examples and not resources:
        print("[ERROR] --examples requires --resources to be set.")
        sys.exit(1)

    print(f"Initializing skill: {skill_name}")
    print(f"   Location: {args.path}")
    print("   Canonical scaffold: governance/, references/, scripts/, assets/, agents/")
    if resources:
        print(f"   Example resources: {', '.join(resources)}")
    else:
        print("   Example resources: none")
    if args.examples:
        print("   Examples: enabled")
    print()

    result = init_skill(skill_name, args.path, resources, args.examples, args.interface)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
