# Usage Runtime Common

## Quand lire ce document
- Le module runtime n'est lu qu'apres selection reelle d'un workflow.
- Lire ce document seulement si un detail de supervision, navigateur, reporting, synchronisation ou securite devient necessaire.

## Supervision et navigateur
- Execution uniquement sur demande explicite de l'utilisateur.
- Mode de reference: automatisation supervisee avec supervision utilisateur vivante.
- Mot d'arret manuel supporte: `STOP`.
- Le navigateur impose est `msedge` avec profil persistant utilisateur.
- Si le profil Edge est verrouille, la relance peut necessiter l'arret des processus `msedge` avant une seule tentative de reprise.

## Dependances partagees
- Source CAF pour les montants: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/PERSONA/_DATA - MICRO_/Micro_revenus_2025-2035.xlsx`.
- Colonnes de travail attendues: `Mois` et `Total Activite`.
- Regle d'arrondi: troncature a l'euro entier, sans centimes.
- Cible de synchronisation post-run: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/PERSONA/_DATA - MICRO_/MICRO.json`.

## Reporting
- Tout run utile doit produire un rapport Markdown sur le Bureau.
- Le rapport doit signaler les periodes ou scope controles, les montants ou statuts, les variations d'UI et les blocages.
- En cas de controle Provigis, le nommage attendu est `PROVIGIS_CHECK__{YYYY-MM-DD}__{HHmm}.md`.

## Synchronisation MICRO
- La sync de `MICRO.json` est faite apres succes d'un run CAF, URSSAF ou Provigis.
- Politique: overwrite in-place par id.
- Les taches cibles sont celles mappees dans `runtime.common.regles.json`.

## Garde-fous
- Aucune execution silencieuse cachee.
- Aucun secret ni identifiant sensible ne doit etre journalise.
- Si la demande n'est pas un end-to-end explicite, confirmer avant toute soumission finale sensible.
- Stopper sur divergence critique entre mois affiches, categories requises, formats d'entree et recapitulatif final.
