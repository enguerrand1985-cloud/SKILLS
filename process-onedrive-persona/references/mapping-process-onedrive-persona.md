# Mapping Process Onedrive Persona

## Remplacement direct
- Ancien couple source: `MARWAN.agent.md` + `INDEX.marwan.json`
- Nouveau porteur de premier rang: `process-onedrive-persona`
- Objectif: garder la logique process legere, deleguer la verite metier et les skills specialises, et laisser les regles satellites externes inchangees pour cette phase

## Capacites preservees dans le process skill
- Perimetre Persona/Micro/SASU hors Meow
- Resolution d alias utilisateur (`Bureau`, `Documents`, `Downloads`, `Scripts`)
- Routage compte/service par signaux de scope, domaine et compte
- Sous-process interne `CAF/URSSAF/Provigis`
- Handoff par intention vers `llm-fiche-structurer`
- Bridge TODO `direct_command > mapping_trigger > request_queue`
- Journal TODO append-only
- Generation de `DONE__` / `FAILED__`
- Copie post-update vers `GPT/TODO/TODO ATTACHEMENTS`
- Regles de stop sur ambiguite et source critique manquante

## Sous-process interne admin
- `governance/router.common.regles.json` est le routeur admin conditionnel
- `governance/caf.regles.json`, `governance/urssaf.regles.json`, `governance/provigis.regles.json` et `governance/combined.regles.json` restent conditionnels
- `governance/runtime.common.regles.json` ne doit etre lu qu apres selection reelle d un workflow admin
- `references/mapping-compliance-admin.md` conserve la cartographie du sous-process admin sans repasser par un skill externe

## Capacites explicitement deleguees
- Structuration et maintenance de fiche LLM -> `C:/Users/engue/.codex/skills/llm-fiche-structurer/SKILL.md`
- Meow / Marque / SKU / Amazon / Alibaba -> `C:/Users/engue/.codex/skills/process-onedrive-meow-paw-paw/SKILL.md`

## Capacites laissees dans les satellites externes
- `PERSONA.json`, `MICRO.json`, `SASU.json`, `Cb 500X.json` restent des sources consultees
- `INDEX SOURCES_PERSONA.json` reste l index de verite externe du perimetre Persona
- les anciennes regles `cb500x.regle.json` et `GPT.regle.json` ont ete sorties du runtime actif

## Regles basculees dans le skill
- `taches_backend.regle.json` devient `governance/taches-backend.regles.json`
- `mode_jeu.regle.json` devient `governance/mode-jeu.regles.json`
- les references actives du process skill pointent maintenant vers les modules internes

## Non repris volontairement
- Aucun acces direct aux internes du skill `llm-fiche-structurer`
- Aucune ecriture Meow depuis ce process
- Aucune absorption de la verite metier dans `governance/`
