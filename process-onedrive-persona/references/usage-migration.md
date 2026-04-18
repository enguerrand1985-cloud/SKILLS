# Usage Migration

## Nomenclature appliquee
- Le sous-process admin est maintenant internalise dans `process-onedrive-persona`.
- `governance/router.common.regles.json` porte le tronc commun conditionnel du sous-process admin.
- `governance/caf.regles.json` porte la logique CAF.
- `governance/urssaf.regles.json` porte la logique URSSAF.
- `governance/provigis.regles.json` porte la logique Provigis.
- `governance/combined.regles.json` porte l'orchestration combinee.
- `governance/common.schema.json` reste le schema actif minimal du tronc commun partage.

## Lecture recommandee
1. Lire `SKILL.md`.
2. Lire `governance/router.common.regles.json`.
3. Lire `references/mapping-compliance-admin.md`.
4. Charger ensuite uniquement le module metier utile.
5. Lire `references/sources-externes.md` seulement si l environnement reel doit etre resolu.

## Note
- Le perimetre du process Persona est conserve.
- La modularite reelle est desormais explicite sans conserver l'ancien skill separe.
