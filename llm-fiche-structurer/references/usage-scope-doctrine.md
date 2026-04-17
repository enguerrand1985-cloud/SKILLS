# Usage Scope Doctrine

## Role
- Ce document detaille la doctrine de scope apres activation de `governance/scope.doctrine.regles.json`.
- Il ne doit pas etre lu par defaut.

## Doctrine generale
- Lire `meta` puis `scope_header` pour qualifier le perimetre.
- Le scope reste ferme par defaut tant qu'aucune agregation explicite n'est demandee.
- `data` porte le factuel, `regles_metier` la logique stable, `todo` la projection, `notes` l'attente ou l'ambigu.

## Baseline runtime
- Les policies minimales attendues sont celles listees dans `scope.doctrine.regles.json`.
- Les playbooks minimaux attendus couvrent onboarding, lookup, maintenance, sortie JSON et rebuild `todo`.

## Scope par famille
- `PERSONA` doit au minimum couvrir `identite`, `personnes`, `documents_index`.
- `MICRO` doit au minimum couvrir `activite`, `fiscalite`, `documents_index`.
- `SASU` doit au minimum couvrir `entreprise`, `documents_index`.

## SASU et child scopes
- Un fichier SASU peut servir de point d'entree sans absorber ses sous-scopes.
- Tout child scope SASU doit porter `scope_header.parent_scope = "SASU"`.
- Une fiche SASU ou child scope SASU doit conserver explicitement la couche entreprise utile en canonique.
- Une convention de nom de fichier n'est jamais un fait tant que le fichier reel n'est pas fourni comme source.
