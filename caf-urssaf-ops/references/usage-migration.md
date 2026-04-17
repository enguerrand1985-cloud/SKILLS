# Usage Migration

## Nomenclature appliquee
- L'ancien bloc metier concentre dans `governance/common.regles.json` a ete eclate par sous-protocole utile.
- `governance/common.regles.json` conserve uniquement le tronc commun partage.
- `governance/caf.regles.json` porte la logique CAF.
- `governance/urssaf.regles.json` porte la logique URSSAF.
- `governance/provigis.regles.json` porte la logique Provigis.
- `governance/combined.regles.json` porte l'orchestration combinee.
- `governance/common.schema.json` reste le schema actif minimal du tronc commun.

## Lecture recommandee
1. Lire `SKILL.md`.
2. Lire `governance/common.regles.json`.
3. Lire `references/sources-externes.md`.
4. Router via `references/mapping-caf-urssaf-ops.md`.
5. Charger ensuite uniquement le module metier utile.

## Note
- Le perimetre du skill est conserve.
- La modularite reelle est desormais explicite sans recreer le skill source.
