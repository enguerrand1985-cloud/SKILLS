---
name: process-onedrive-persona
description: "Router and operate Persona, Micro, and SASU requests from the local Persona perimeter with progressive reading, alias resolution, TODO bridge handling, internal CAF/URSSAF/Provigis modules, and explicit handoff to llm-fiche-structurer or process-onedrive-meow-paw-paw when scope requires it."
---

# MISSION
Porter le process local Persona, Micro et SASU hors Meow sans recharger l'ancien couple MARWAN agent plus index, avec un routeur leger, une lecture progressive, une resolution d alias stable, un sous-process interne CAF/URSSAF/Provigis, et des handoffs explicites vers les skills specialises restants ou vers le process Meow quand le scope l'exige.

# PORTEE
- Domaine couvert: triage generaliste Persona/Micro/SASU, resolution d alias utilisateur, routage compte/service, bridge TODO, backend de taches Persona et mode jeu local, sorties par defaut, sous-process admin `CAF/URSSAF/Provigis`, et handoff vers `llm-fiche-structurer`.
- Hors perimetre: business Meow Paw Paw / MARQUE, maintenance systeme profonde Meow, et verite metier contenue dans `PERSONA.json`, `MICRO.json`, `SASU.json` ou `INDEX SOURCES_PERSONA.json`.

# CONDITIONS D'ACTIVATION
- Activer ce skill quand: la demande concerne le perimetre Persona/Micro/SASU hors Meow, une resolution d alias OneDrive personnel, une action via le bridge TODO, un pre-triage generaliste, une demande `CAF/URSSAF/Provigis`, ou un routage vers `llm-fiche-structurer`.
- Ne pas l'activer quand: la demande est centree Meow/Marque/SKU/Fournisseurs/Amazon/Alibaba, ou quand un skill specialise deja nomme doit prendre directement la main.

# ORDRE DE LECTURE
1. Toujours lire `SKILL.md`.
2. Toujours lire `governance/router.regles.json`.
3. Lire `governance/routing.regles.json` seulement si la demande implique scope, compte, service, source externe, backend de taches, routage specialise ou qualification admin `CAF/URSSAF/Provigis`.
4. Lire `governance/paths.regles.json` seulement si la demande mentionne un alias utilisateur, un emplacement de sortie ou une cible de copie.
5. Lire `governance/taches-backend.regles.json` seulement si la demande touche la creation, la mise a jour, le backend ou le routage d une tache Persona/Micro/SASU.
6. Lire `governance/mode-jeu.regles.json` seulement sur demande explicite de preparation ou retour en mode jeu.
7. Lire `governance/bridge.regles.json` et `references/usage-bridge-runtime.md` seulement si la demande implique `REQUEST`, `DONE__`, `FAILED__`, mapping trigger, journal TODO ou synchronisation post-update.
8. Lire `governance/router.common.regles.json` puis `references/mapping-compliance-admin.md` seulement si l intent admin `CAF/URSSAF/Provigis` est reellement confirme.
9. Lire ensuite uniquement le module utile parmi `governance/caf.regles.json`, `governance/urssaf.regles.json`, `governance/provigis.regles.json` ou `governance/combined.regles.json`.
10. Lire `governance/runtime.common.regles.json`, `references/usage-runtime-common.md` et `references/sources-externes.md` seulement si l execution admin, la policy runtime, la synchronisation ou la resolution d environnement le rendent necessaire.

# ROUTAGE INTERNE
- Toujours lu: `SKILL.md`, puis `governance/router.regles.json`.
- Lu a la demande: `governance/routing.regles.json`, `governance/paths.regles.json`, `governance/taches-backend.regles.json`, `governance/mode-jeu.regles.json`, `governance/bridge.regles.json`, `references/mapping-process-onedrive-persona.md`, `references/usage-bridge-runtime.md`, `governance/router.common.regles.json`, `governance/caf.regles.json`, `governance/urssaf.regles.json`, `governance/provigis.regles.json`, `governance/combined.regles.json`, `governance/runtime.common.regles.json`, `references/mapping-compliance-admin.md`, `references/usage-runtime-common.md`, `references/sources-externes.md`.
- Validation finale seulement si utile: `N/A`.
- Si aucun sous-cas n'est resolu, produire un STOP explicite et deleguer soit vers `process-onedrive-meow-paw-paw`, soit vers un skill specialise.

# WORKFLOWS / PROTOCOLES
1. Triage Persona: identifier le scope, charger le module minimal utile, resoudre les alias, puis soit executer localement soit handoff vers `llm-fiche-structurer` ou `process-onedrive-meow-paw-paw`.
2. Admin compliance: si la demande vise `CAF`, `URSSAF`, `Provigis` ou une execution combinee, rester dans `process-onedrive-persona`, charger le routeur `governance/router.common.regles.json`, puis n activer que le module admin necessaire.
3. Backend de taches: charger `taches-backend.regles.json` quand la demande touche Outlook Tasks, le backend de taches ou le flux TODO formalise.
4. Mode jeu: charger `mode-jeu.regles.json` seulement sur demande explicite, en execution supervisee.
5. Bridge TODO: appliquer la priorite `direct_command > mapping_trigger > request_queue`, journaliser en append-only, generer `DONE__` ou `FAILED__`, et ne supprimer une request qu'apres succes.

# REGLES NON NEGOCIABLES
- Ne pas embarquer de data verite externe dans le skill.
- Garder le `toujours lu` leger.
- Ne pas creer de modules decoratifs.
- Ne pas rehandoff `CAF/URSSAF/Provigis` vers un skill separe tant que le sous-process interne couvre le besoin.
- Ne pas piloter les internes de `llm-fiche-structurer`; handoff uniquement par intention explicite.
- Ne pas ecrire sur le perimetre Meow via ce skill; handoff direct vers `process-onedrive-meow-paw-paw` si la demande bascule en Meow.

# CONDITIONS DE STOP
- STOP si les signaux de scope, compte ou service se contredisent.
- STOP si une source critique referencee par le module actif n'existe pas.
- STOP si une mise a jour Meow est demandee depuis ce process.
- STOP si une demande `CAF/URSSAF/Provigis` ne permet pas de qualifier un workflow admin reel.
- STOP si la mutation demandee depasse la portee process et exige une refonte des regles satellites externes.

# FORMAT DE SORTIE
- mode: `persona-process`
- status: `done` | `stop` | `handoff`
- target: scope ou skill cible resolu
- result: action executee, preparation effectuee, ou routage decide
- blockers: blocage de scope, source absente, ambiguite de compte, ou `Aucun`
- next_action: prochaine action locale ou skill a charger
- artifacts: `DONE__*`, `FAILED__*`, mise a jour journal TODO, ou `Aucun`

# REFERENCES
- `references/mapping-process-onedrive-persona.md`
- `references/mapping-compliance-admin.md`
- `references/usage-bridge-runtime.md`
- `governance/taches-backend.regles.json`
- `governance/mode-jeu.regles.json`
- `governance/router.common.regles.json`
- `governance/runtime.common.regles.json`
- `governance/caf.regles.json`
- `governance/urssaf.regles.json`
- `governance/provigis.regles.json`
- `governance/combined.regles.json`
