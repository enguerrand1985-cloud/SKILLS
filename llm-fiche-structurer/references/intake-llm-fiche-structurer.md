# Intake Fiche LLM (Questionnaire d'amorcage)

Utiliser ce questionnaire quand l'utilisateur dit "fais-moi une fiche LLM" a partir d'un lot de documents, OU quand il demande une maintenance complete d'une fiche existante.
Objectif: capturer rapidement les arbitrages de placement par section.

## 1) Scope
- Scope cible: master (`PERSONA`/`MICRO`/`SASU`/autre) ?
- Si child scope: quel `scope_header.scope` et quel `scope_header.parent_scope` ?

## 2) Finalite
- A quoi servira la fiche en priorite (pilotage quotidien, dossier administratif, suivi technique, etc.) ?

## 3) Placement par section
- `data.canonique`: quels faits stables doivent etre presents en priorite ?
- `data.scope_specifique.archives`: quels historiques/details doivent rester en archive ?
- `regles_metier`: quelles regles/procedures doivent etre explicites ?
- `todo`: quelles prochaines occurrences/actions doivent etre projetees ?
- `notes`: quels incidents/points de vigilance doivent etre traces ?

## 4) Priorites de sortie
- Souhaites-tu une v1 minimale (noyau) ou une v1 complete (plus remplie) ?
- Y a-t-il des sections a laisser volontairement vides pour plus tard ?

## 5) Regles de fallback (si reponses partielles)
- Ne pas inventer.
- Placer l'incertain en `notes`.
- Mettre l'historique detaille en `archives`.
- Projeter un `todo` minimal uniquement si les donnees sont suffisantes.
