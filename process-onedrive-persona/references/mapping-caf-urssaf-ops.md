# Mapping CAF URSSAF Ops

- Toujours commencer par `governance/router.common.regles.json`.
- Si le sous-cas n'est pas evident, utiliser ce mapping puis ne charger qu'un seul module metier a la fois, sauf pour `combined`.
- Charger `governance/runtime.common.regles.json` seulement apres selection reelle du workflow ou si une policy runtime doit etre appliquee.

## Routage metier
- Trigger `caf` -> lire `governance/caf.regles.json` -> lire `references/usage-caf.md` seulement si le detail d'execution est necessaire.
- Trigger `urssaf` -> lire `governance/urssaf.regles.json` -> lire `references/usage-urssaf.md` seulement si le detail d'execution est necessaire.
- Trigger `provigis` -> lire `governance/provigis.regles.json` -> lire `references/usage-provigis.md` seulement si le detail de controle est necessaire.
- Trigger `combine` -> lire `governance/combined.regles.json` -> lire `references/usage-combined.md` seulement si l'orchestration detaillee est necessaire.

## Conditionnels
- `references/usage-runtime-common.md` : seulement si navigateur, reporting, sync ou securite runtime deviennent utiles.
- `references/sources-externes.md` : seulement si un chemin reel, une source externe ou une verification d'environnement doit etre resolu.
- `governance/common.schema.json` : seulement si un controle structurel du tronc commun partage est requis.
