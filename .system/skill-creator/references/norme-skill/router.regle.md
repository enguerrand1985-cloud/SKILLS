# Router NORME_SKILL

Projection runtime derivee des sources canoniques :
- `C:/Users/engue/__SYSTEME - GITHUB__/GOUVERNANCE/NORME_SKILL.regle.md`
- `C:/Users/engue/__SYSTEME - GITHUB__/GOUVERNANCE/NORME_SKILL.schema.json`

## Toujours lire
1. `router.regle.md`
2. `schema.core.json`

## Chemin court
Utiliser pour :
- `create-minimal`
- `update-light`
- `validate-quick`
- `add-asset`
- `add-script`
- `add-reference`

Lire seulement :
- `create-minimal.regle.md` ou `update-light.regle.md`
- `validation.regle.md` seulement si une verification rapide est utile
- le module cible parmi `governance.regle.md`, `references.regle.md`, `assets.regle.md`

## Chemin intermediaire
Utiliser pour :
- `update-structure`
- `add-governance-light`
- `migrate-partial`

Lire :
- `update-light.regle.md`
- le module cible
- `validation.regle.md`
- `schema.validation.json`
- `schema.governance.json` ou `schema.assets.json` si le cas l'exige

## Chemin complet
Utiliser pour :
- `create-full`
- `refactor-full`
- `audit-full`
- `migrate-full`

Lire :
- `full-creation.regle.md`
- les modules cibles
- `validation.regle.md`
- les schemas runtime utiles

## Regle d'escalade
- ne pas charger le chemin complet pour une micro-demande
- escalader seulement si la structure, le schema ou la migration l'exige
- revenir aux sources canoniques seulement si la projection runtime ne suffit pas
