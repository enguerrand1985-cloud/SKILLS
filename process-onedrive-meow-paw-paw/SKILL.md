---
name: process-onedrive-meow-paw-paw
description: "Route and operate Meow Paw Paw and MARQUE requests from the local SOURCE OF TRUTH perimeter with INDEX SOURCES first for business reads, explicit separation from system maintenance, append-only bridge handling, and direct handoff to systeme-meow-paw-paw when mutation or coherence work is requested."
---

# MISSION
Porter le process local Meow Paw Paw et MARQUE depuis la source locale `SOURCE OF TRUTH`, sans recharger l'ancien couple BEBERT agent plus index, avec un routeur leger, une lecture progressive, une separation stricte entre lecture business et maintenance systeme, et un handoff explicite vers `systeme-meow-paw-paw` quand une mutation ou une coherence systeme est demandee.

# PORTEE
- Domaine couvert: triage Meow/Marque/SASU cote marque, resolution d alias utilisateur, bridge MEOW, lecture business a partir de `INDEX SOURCES`, backend de taches Meow, policies domaine marque, routage vers workbooks locaux et separation `run now` vs `dev futur`.
- Hors perimetre: support generaliste Persona, maintenance systeme profonde qui doit passer par `systeme-meow-paw-paw`, et verite metier contenue dans `INDEX SOURCES.json`, workbooks ou `SKU.json`.

# CONDITIONS D'ACTIVATION
- Activer ce skill quand: la demande concerne Meow Paw Paw, MARQUE, sourcing, SKU, Amazon, Alibaba, bridge MEOW, ou une resolution de chemins / sorties dans ce perimetre.
- Ne pas l'activer quand: la demande est generaliste Persona, purement systeme sans contexte Meow business deja qualifie, ou deja prise en charge directement par un skill specialise nomme.

# ORDRE DE LECTURE
1. Toujours lire `SKILL.md`.
2. Toujours lire `governance/router.regles.json`.
3. Lire `governance/routing.regles.json` seulement si la demande implique lecture business, selection de profil, workbooks, marge, profitabilite, backend de taches ou handoff vers la couche systeme.
4. Lire `governance/paths.regles.json` seulement si la demande mentionne un alias utilisateur, un emplacement de sortie ou une cible de rapport.
5. Lire `governance/domaine-marque.regles.json` seulement si la demande touche les workbooks Meow, la synchronisation post-write, la replication ou la politique de mise a jour locale.
6. Lire `governance/taches-backend.regles.json` seulement si la demande touche le backend de taches, le flux formalise TODO ou la synchro workbook vers Todo/Outlook.
7. Lire `governance/bridge.regles.json` et `references/usage-sources-vs-system.md` seulement si la demande implique `REQUEST`, journals MEOW, mapping trigger, mutation systeme ou arbitrage business vs maintenance.

# ROUTAGE INTERNE
- Toujours lu: `SKILL.md`, puis `governance/router.regles.json`.
- Lu a la demande: `governance/routing.regles.json`, `governance/paths.regles.json`, `governance/domaine-marque.regles.json`, `governance/taches-backend.regles.json`, `governance/bridge.regles.json`, `references/mapping-process-onedrive-meow-paw-paw.md`, `references/usage-sources-vs-system.md`.
- Validation finale seulement si utile: `N/A`.
- Si aucun sous-cas n'est resolu, produire un STOP explicite et deleguer soit vers `systeme-meow-paw-paw`, soit vers `process-onedrive-persona`.

# WORKFLOWS / PROTOCOLES
1. Business run Meow: qualifier le stream, lire `INDEX SOURCES` et les regles internes utiles, resoudre le workbook ou la source cible, puis produire une sortie orientee execution sans absorber la verite dans le skill.
2. Workbook et domaine marque: charger `domaine-marque.regles.json` pour toute politique de write, replication, dated items et CSV ingestion.
3. Backend de taches: charger `taches-backend.regles.json` pour tout routage backend ou flux formalise de taches Meow.
4. Maintenance / mutation: si la demande touche coherence systeme, policy, write-intent, schema ou synchronisation technique, handoff direct vers `systeme-meow-paw-paw` apres qualification du sous-cas.

# REGLES NON NEGOCIABLES
- Ne pas embarquer de data verite externe dans le skill.
- Garder le `toujours lu` leger.
- Ne pas creer de modules decoratifs.
- Lire `INDEX SOURCES` avant toute lecture business dense; la couche systeme ne devient active qu'en maintenance.
- Ne pas faire de mutation systeme profonde depuis ce process; handoff direct vers `systeme-meow-paw-paw`.
- Garder les journaux MEOW et TODO en append-only.

# CONDITIONS DE STOP
- STOP si la demande melange business et maintenance sans sous-cas resolu.
- STOP si une source critique ou un workbook requis n'existe pas.
- STOP si une REQUEST est ambigue, sans journal_ref, ou sans fichier lie requis.
- STOP si la mutation demandee depasse la portee process et doit etre arbitree au niveau systeme.

# FORMAT DE SORTIE
- mode: `meow-process`
- status: `done` | `stop` | `handoff`
- target: stream, source ou skill cible resolu
- result: lecture business, preparation d action, ou routage maintenance decide
- blockers: blocage de source, ambiguite business/systeme, request invalide, ou `Aucun`
- next_action: prochaine action locale, workbook cible, ou skill a charger
- artifacts: `DONE__*`, `FAILED__*`, mise a jour journals MEOW/TODO, ou `Aucun`

# REFERENCES
- `references/mapping-process-onedrive-meow-paw-paw.md`
- `references/usage-sources-vs-system.md`
- `governance/domaine-marque.regles.json`
- `governance/taches-backend.regles.json`
