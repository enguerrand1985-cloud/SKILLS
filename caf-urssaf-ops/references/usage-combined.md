# Usage Combined CAF URSSAF

## Objectif
- Executer `CAF` puis `URSSAF` dans une meme session supervisee.
- Reutiliser le meme profil Edge persistant, sans ouvrir un nouveau contexte navigateur entre les deux flux.

## Ordre d'execution
- Commencer par le workflow `caf_trimestrielle`.
- Une fois la page de succes CAF atteinte, enchainer avec `urssaf_ca_trimestrielle`.
- Ne pas lancer les deux modules en parallele.

## Actions post-run
- Mettre a jour la tache Microsoft To Do ciblee si l'orchestration complete le prevoit.
- Liste attendue: `M.I.C.R.O`.
- Tache attendue: contient `URSSAF / CAF`.
- Si la tache est recurrente, une nouvelle occurrence immediate peut reapparaitre: c'est attendu.
- En parallele, mettre a jour les taches CAF et URSSAF de `MICRO.json` selon la policy runtime.

## Artefact final
- Produire un rapport Markdown sur le Bureau.
- Nom attendu: `AUTOMATISATION_CAF_URSSAF__DONE__{YYYY-MM-DD}.md`.
- Sections attendues: `CAF RESULTAT`, `URSSAF RESULTAT`, `MONTANTS SAISIS`, `HORODATAGE`, `ANOMALIES_UI_ET_ADAPTATIONS`, `MICROSOFT TODO UPDATE`.

## Reference de run validee
- Date observee: `2026-04-05`.
- Liste To Do observee: `M.I.C.R.O`.
- Comportement recurrent observe apres completion: oui.
