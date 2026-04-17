# Usage Migration

Ce fichier sert uniquement pour migration, historique ou arbitrage de refactor.

Il ne fait pas partie du runtime courant.

## Nomenclature appliquee
- `gouvernance/` -> `governance/`
- `gouvernance/INDEX SYSTEM.json` -> `governance/common.regles.json`
- `gouvernance/PARAMETRES SYSTEME.regles.json` -> `governance/update.regles.json`
- `gouvernance/TAXONOMIE_PARAMETERS.json` -> `governance/sync.regles.json`
- Les anciens `.schema.json` de gouvernance ne sont plus pris en compte dans le runtime du skill test.
- Aucun catalogue legacy externe n'est reference par defaut.

## Assets conserves localement
- `assets/skeleton_compta_parameters.json`
- `assets/skeleton_etiquettes.json`
- `assets/skeleton_fournisseurs.json`
- `assets/skeleton_marketplace.json`
- `assets/skeleton_profil_sasu.json`
- `assets/skeleton_sku.json`
- `assets/skeleton_vision.json`
- `assets/template_task.csv`

## Lecture recommandee pour un audit historique
1. Lire `SKILL.md`.
2. Lire `governance/common.regles.json`.
3. Lire ce fichier seulement si la demande porte sur l'historique ou les arbitrages du refactor.
