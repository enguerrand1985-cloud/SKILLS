---
name: systeme-gpt-bridge
description: "Router, maintain, and validate the personal GPT ecosystem and bridge configuration from the local GPT perimeter with a light always-read core, targeted project modules, and explicit handoff to process or specialized skills when the underlying work belongs elsewhere."
---

# MISSION
Porter le skill metier `systeme-GPT_BRIDGE` comme couche canonique de maintenance, routage et validation du systeme GPT personnel depuis sa propre gouvernance interne, sans dependre d un dossier `PARAMETERS` legacy. Le skill doit garder un coeur toujours lu leger, lire les modules projets ou bridge seulement quand ils deviennent necessaires, et separer clairement la gouvernance GPT des skills process ou metier qu il peut appeler.

# PORTEE
- Domaine couvert: gouvernance globale GPT, maintenance du bridge REQUEST/DONE/FAILED, profils projets et GPTs personnels, controle des contrats de prompt et journal, pilotage cible de `System IA`, et recablage des references GPT vers `process-onedrive-persona`, `process-onedrive-meow-paw-paw`, `llm-fiche-structurer` ou `systeme-meow-paw-paw` quand c est la bonne couche.
- Hors perimetre: execution metier CAF/URSSAF/Provigis, maintenance profonde Meow, structuration interne de fiches LLM, operations navigateur reelles, et modification directe des projets GPT sans demande explicite.

# CONDITIONS D'ACTIVATION
- Activer ce skill quand: la demande porte sur la gouvernance GPT personnelle, un projet GPT personnel, le bridge, `System IA`, un index/journal/prompt GPT, un schema de gouvernance GPT, ou une refonte des references GPT apres changement d architecture locale.
- Ne pas l'activer quand: la demande est deja clairement ciblee vers `llm-fiche-structurer`, `process-onedrive-persona`, `process-onedrive-meow-paw-paw` ou `systeme-meow-paw-paw` sans besoin de maintenance GPT.

# ORDRE DE LECTURE
1. Toujours lire `SKILL.md`.
2. Toujours lire `governance/common.regles.json`.
3. Lire `governance/runtime.regles.json` seulement si la demande implique la gouvernance GPT globale, un changement structurel, un recadrage du bridge, un recablage de references ou une bascule de configuration.
4. Lire `governance/bridge.regles.json` seulement si la demande implique `BRIDGE`, `REQUEST__`, `DONE__`, `FAILED__`, journalisation ou routage par scope.
5. Lire `governance/projects.regles.json` seulement si la demande cible un projet GPT ou un GPT nomme (`TODO`, `MEOW PAW PAW`, `System IA`, `ASSETS STUDIO`, `GPT_SCROOGE`).
6. Lire `governance/system-ia.regles.json` seulement si la demande touche `System IA`, le context pack, les copies de routeur ou le recablage des dependances legacy.
7. Lire `governance/global.schema.json`, `governance/project.schema.json` et `governance/ecosystem.schema.json` seulement pour validation, migration de format ou controle de conformite.
8. Lire `references/usage-gpt-projects.md`, `references/usage-system-ia-runtime.md` ou `references/sources-externes.md` seulement si le detail operatoire devient necessaire.
9. Executer `scripts/check_gpt_paths.py` seulement si un controle deterministe des chemins et contrats actifs apporte un gain utile.

# ROUTAGE INTERNE
- Toujours lu: `SKILL.md`, puis `governance/common.regles.json`.
- Lu a la demande: `governance/runtime.regles.json`, `governance/bridge.regles.json`, `governance/projects.regles.json`, `governance/system-ia.regles.json`, `references/mapping-systeme-gpt-bridge.md`, `references/usage-gpt-projects.md`, `references/usage-system-ia-runtime.md`, `references/sources-externes.md`.
- Validation finale seulement si utile: `governance/global.schema.json`, `governance/project.schema.json`, `governance/ecosystem.schema.json`, puis `scripts/check_gpt_paths.py`.
- Si aucun sous-cas n'est resolu, produire un STOP explicite et deleguer vers le process skill ou le skill specialise qui porte reellement la demande.

# WORKFLOWS / PROTOCOLES
1. Maintenance GPT globale: charger `common`, puis `runtime`, identifier la cible GPT/projet, appliquer les garde-fous `REQUEST_ONLY` et `prompt_change_structural_only`, puis seulement ouvrir les fichiers externes necessaires.
2. Bridge: charger `common`, puis `bridge`, resoudre le scope et l intent, router vers le bon process skill ou skill specialise, et garder la logique de request lifecycle append-only.
3. Projet GPT cible: charger `common`, puis `projects`, puis le module reference le plus utile dans `references/`, sans charger tout le parc GPT si un seul projet est vise.
4. System IA: charger `common`, `projects`, puis `system-ia`, traiter le context pack et les copies d instructions comme un sous-cas de gouvernance GPT, pas comme un skill metier autonome.
5. Validation: charger les schemas seulement si la demande touche la structure, le journal, l ecosystem context ou les contrats de prompt.

# REGLES NON NEGOCIABLES
- Ne pas embarquer de data verite externe dans le skill.
- Garder le `toujours lu` leger.
- Ne pas creer de modules decoratifs.
- Ne pas laisser `MARWAN.agent.md`, `BEBERT.agent.md`, `INDEX.marwan.json` ou `INDEX.bebert.json` comme dependances actives du nouveau skill.
- Ne pas executer une action sensible sur un portail ou un classeur a partir de ce skill sans demande explicite et sans dry-run si le contexte l exige.
- Ne pas confondre gouvernance GPT et execution metier: ce skill route et maintient, il ne remplace pas les skills specialises.

# CONDITIONS DE STOP
- STOP si la cible GPT/projet reste ambigue apres le triage minimal.
- STOP si une source critique externe referencee par le module actif manque ou est cassee.
- STOP si la demande releve d un autre skill et ne necessite pas de maintenance GPT.
- STOP si une mutation structurelle importante est demandee sur GPT sans arbitrage clair sur les fichiers cibles.

# FORMAT DE SORTIE
- mode: `gpt-bridge`
- status: `done` | `stop` | `handoff`
- target: projet GPT, GPT cible, fichier de gouvernance, ou skill de destination
- result: maintenance preparee, controle realise, ecart documente, ou routage decide
- blockers: ambiguite, source manquante, conflit de scope, ou `Aucun`
- next_action: prochain module a lire, fichier a verifier, ou skill a activer
- artifacts: rapport, liste d ecarts, script de verification, ou `Aucun`

# REFERENCES
- `references/mapping-systeme-gpt-bridge.md`
- `references/usage-gpt-projects.md`
- `references/usage-system-ia-runtime.md`
- `references/sources-externes.md`
