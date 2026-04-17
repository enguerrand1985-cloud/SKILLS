---
name: skill-creator
description: Create, update, migrate, or validate skills in this Codex environment. Use when Codex needs to scaffold a new personal skill, refactor a personal skill to the local NORME_SKILL standard, add or reorganize governance/references/scripts/assets, or verify whether a skill is structurally compliant without breaking system or external skills.
metadata:
  short-description: Create or normalize skills
---

# Skill Creator

This skill is the canonical creator and validator for personal skills in this environment.

## Environment Policy

In this environment:
- personal skills must follow the canonical `NORME_SKILL`
- the canonical sources remain:
  - `C:/Users/engue/__SYSTEME - GITHUB__/GOUVERNANCE/NORME_SKILL.regle.md`
  - `C:/Users/engue/__SYSTEME - GITHUB__/GOUVERNANCE/NORME_SKILL.schema.json`
- the files under `references/norme-skill/` are runtime projections derived from those canonical sources
- the runtime projection optimizes reading order but does not replace the canonical norm

System/OpenAI/external skills remain tolerated by validation. Strict norm enforcement targets personal skills.

## Read Order

Always start with:
1. `references/norme-skill/router.regle.md`
2. `references/norme-skill/schema.core.json`

Then route by intent:

### Small requests
Use this path for:
- create-minimal
- update-light
- validate-quick
- add-asset
- add-script
- add-reference

Read only:
- `references/norme-skill/create-minimal.regle.md` for scaffold or tiny creation work
- `references/norme-skill/update-light.regle.md` for small updates
- `references/norme-skill/validation.regle.md` only if a quick validation is needed
- one targeted module among:
  - `references/norme-skill/governance.regle.md`
  - `references/norme-skill/references.regle.md`
  - `references/norme-skill/assets.regle.md`

### Intermediate requests
Use this path for:
- update-structure
- add-governance-light
- migrate-partial

Read:
- `references/norme-skill/update-light.regle.md`
- the targeted domain module(s)
- `references/norme-skill/validation.regle.md`
- `references/norme-skill/schema.validation.json`
- `references/norme-skill/schema.governance.json` or `schema.assets.json` only if the change touches that area

### Full requests
Use this path for:
- create-full
- refactor-full
- audit-full
- migrate-full

Read:
- `references/norme-skill/full-creation.regle.md`
- the targeted domain module(s)
- `references/norme-skill/validation.regle.md`
- all runtime schema modules needed by the case

Only fall back to the canonical monoliths if the runtime projection is insufficient for the decision at hand.

## Creation Workflow

1. Clarify the competency, scope, and whether the skill is simple, modular, or hybrid.
2. Use `scripts/init_skill.py` for new skills instead of hand-building the folder.
3. Generate the canonical personal scaffold:
   - `SKILL.md`
   - `governance/`
   - `references/`
   - `scripts/`
   - `assets/`
   - `agents/openai.yaml`
4. Keep the scaffold light:
   - do not create decorative governance modules
   - do not create decorative schemas
   - do not embed external truth
5. Fill `SKILL.md` using the exact fixed section order from the norm.

## Update Workflow

For an existing skill:
- do not reload the full norm for a micro-change if a short path is sufficient
- modify only the impacted area unless the request explicitly becomes structural
- escalate from short to intermediate to full only when structure, schema, or migration depth justifies it

Examples:
- add one reference file -> short path
- rename or split governance modules -> intermediate path
- convert a legacy skill to hybrid architecture -> full path

## Validation Workflow

Use `scripts/quick_validate.py <path/to/skill>` after structural work.

The validator now works in two layers:
- standard skill compatibility for any skill
- strict `NORME_SKILL` checks for personal skills

Validation levels:
- quick: scaffold and obvious naming/order checks
- structural: routing and folder/module coherence
- full: only when the task genuinely touches heavy structure

## Runtime Modules

- `references/norme-skill/router.regle.md`: intent router and read-depth selector
- `references/norme-skill/create-minimal.regle.md`: minimal creation path
- `references/norme-skill/update-light.regle.md`: light update path
- `references/norme-skill/full-creation.regle.md`: full creation/refactor path
- `references/norme-skill/validation.regle.md`: quick vs structural vs full validation guidance
- `references/norme-skill/governance.regle.md`: active declarative layer rules
- `references/norme-skill/references.regle.md`: support/documentation layer rules
- `references/norme-skill/assets.regle.md`: passive materials and skeleton rules
- `references/norme-skill/schema.core.json`: canonical scaffold and section order
- `references/norme-skill/schema.validation.json`: validator rules and naming patterns
- `references/norme-skill/schema.governance.json`: governance-specific checks
- `references/norme-skill/schema.assets.json`: assets-specific checks

## Scripts

- `scripts/init_skill.py`
  - creates the canonical personal scaffold
  - keeps example resources optional
  - avoids decorative files by default

- `scripts/quick_validate.py`
  - validates standard skill compatibility everywhere
  - enforces strict norm checks only for personal skills

- `scripts/generate_openai_yaml.py`
  - regenerates `agents/openai.yaml` metadata

## References

- Read `references/openai_yaml.md` before generating or regenerating `agents/openai.yaml`.
- Use the canonical norm files only when the runtime projection is not enough.
- Keep the projection and the canonical sources aligned whenever the norm changes.
