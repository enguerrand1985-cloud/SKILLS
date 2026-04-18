# Mapping systeme-gpt-bridge

Ce skill est maintenant la source canonique locale de gouvernance GPT :

- `C:/Users/engue/.codex/skills/systeme-gpt-bridge`

Correspondances principales :

- `INDEX_GPT_SYSTEME.json` -> `governance/projects.regles.json` + `governance/common.regles.json`
- `PARAMETERS/GPT.regle.json` -> `governance/runtime.regles.json` + `governance/bridge.regles.json`
- `PARAMETERS/TODO.regle.json` -> `governance/projects.regles.json` section `TODO`
- `PARAMETERS/MEOW_PAW_PAW.regle.json` -> `governance/projects.regles.json` section `MEOW_PAW_PAW`
- `PARAMETERS/SYSTEM_IA.regle.json` -> `governance/system-ia.regles.json`
- `PARAMETERS/ASSETS_STUDIO.regle.json` -> `governance/projects.regles.json` section `ASSETS_STUDIO`
- `PARAMETERS/GPT_SCROOGE.regle.json` -> `governance/projects.regles.json` section `GPT_SCROOGE`
- `SCHEMAS & LAYERS/GPT_GLOBAL.schema.json` -> `governance/global.schema.json`
- `SCHEMAS & LAYERS/GPT_ECOSYSTEM_CONTEXT.schema.json` -> `governance/ecosystem.schema.json`
- project schemas -> `governance/project.schema.json` + `governance/system-ia.regles.json`

Recablage voulu :

- ancienne dependance `MARWAN.agent.md` -> `process-onedrive-persona`
- ancienne dependance `BEBERT.agent.md` -> `process-onedrive-meow-paw-paw`
- maintenance systeme Meow -> `systeme-meow-paw-paw`
- fiche LLM -> `llm-fiche-structurer`
- CAF / URSSAF / Provigis -> `process-onedrive-persona`

Rappel :

- le skill ne remplace pas les projets GPT reels
- il maintient la gouvernance et le routage
- le dossier `PARAMETERS/GPT maintenance` a ete retire du runtime actif
