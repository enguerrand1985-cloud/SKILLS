# Usage Update Runtime

## Quand lire ce document
- Lire ce document seulement apres activation de `governance/update.regles.json`.
- Il sert pour les full-runs systeme, write-intents, changements de policy, changements structurels et audits lourds.

## Separation des couches
- Le prompt garde le role agent, les objectifs, le ton, le format de reponse et la posture de maintenance.
- `common` garde l'activation, le tri du sous-cas, la matrice de lecture et le STOP de premier niveau.
- `update` porte ensuite les contraintes de maintenance, de lecture des couches de verite, de schema et de changement.

## Lecture des couches de verite
- Priorite de lecture: `INDEX SOURCES.json`, puis la couche de verite la plus adaptee au besoin.
- Couches disponibles: `final_truth`, `operational_truth`, `working_truth`, `notes_only`, `stabilized_snapshot`.
- Les chemins detaillees et catalogues de sources vivent dans `references/sources-externes.md`.

## Routage par intention
- Audit final ou etat valide: privilegier `final_truth` puis `stabilized_snapshot`.
- Etat operationnel courant: privilegier `operational_truth` puis `final_truth`.
- Preparation ou brouillon: privilegier `working_truth` puis `operational_truth`.
- Capture de notes ou ideation: privilegier `notes_only` puis `working_truth`.

## Navigation
- Les index sont des artefacts de routage, pas la verite business.
- Toute proposition doit citer la source primaire et ses dependances.
- Si index et realite physique divergent, signaler la divergence avant correction.
- `sync.regles.json` ne se lit pas pour un simple update si la nomenclature n'est pas en jeu.

## Garde-fous reader
- Ne jamais filtrer implicitement les SKU par `role`.
- Un filtre par role n'est admis que s'il est explicitement demande par l'utilisateur ou impose par une regle identifiee.

## Schema et write-intent
- Le contenu JSON et la structure schema sont tous deux verite.
- Lire le schema avant une modification JSON.
- Signaler toute divergence JSON vs schema avant correction.
- Avant patch, confirmer fichier cible, couche de verite, scope d'impact et dependances de coherence.
- Interdits: invention de chemin, bascule silencieuse de source de verite, reintroduction d'un catalogue legacy, ecriture sans cadre de validation.

## Protocole update d information
- Si l utilisateur donne une nouvelle information factuelle a injecter dans le systeme, traiter cela comme un `write-intent` avec scan de coherence obligatoire.
- Identifier la source primaire a modifier puis resoudre ses dependances et dependances inverses via `INDEX SOURCES.json`.
- Si la cible est un JSON, lire le schema avant patch; si la modification touche un scalaire, un total ou un statut confirme, lancer aussi un scan de duplications candidates.
- Rechercher les references explicites au fichier cible et aux valeurs modifiees quand elles peuvent etre recopiees ailleurs.
- Ne pas fermer la tache avec un patch mono-fichier si des dependances inverses ou des duplications candidates restent non verifiees.
- Utiliser `scripts/check_update_coherence.py` quand un controle deterministe peut accelerer la verification inter-fichiers.

## Change management
- Une nouvelle source de verite demande validation.
- Un changement structurel demande mise a jour du schema, puis du prompt et de l'index si necessaire.
- L'application JSON doit passer par un cadre de diff ou de patch borne.

## Rendu
- Sections attendues: `RESUME EXECUTIF`, `PRIORITE MAINTENANT`, `BLOQUEURS`, `AUTOMATISATION`, `RUN VS FUTUR`, `LECTURE PAR STREAM`, `LECTURE PAR CATEGORIE`, `LECTURE PAR TIMELINE`, `PROCHAINES ACTIONS`, `REQUEST BRIDGE`.
- Maximum 7 lignes par bloc.
- Statuts autorises: `URGENT`, `CETTE_SEMAINE`, `A_PREPARER`, `BLOQUE`.
- `REQUEST BRIDGE` seulement sur demande explicite.
- Si un schema est implique, preciser si cela touche le contenu JSON, la structure schema, ou les deux.
