# Mapping Process Onedrive Meow Paw Paw

## Remplacement direct
- Ancien couple source: `BEBERT.agent.md` + `INDEX.bebert.json`
- Nouveau porteur de premier rang: `process-onedrive-meow-paw-paw`
- Objectif: garder le process Meow leger, proteger la frontiere business vs systeme, et deleguer la maintenance lourde au skill `systeme-meow-paw-paw`

## Capacites preservees dans le process skill
- Perimetre Meow Paw Paw / MARQUE / SASU cote marque
- Resolution d alias utilisateur
- Politique `INDEX SOURCES first`
- Handoff vers `systeme-meow-paw-paw` pour mutation, coherence et maintenance
- Routage compte/service et workbook principal
- Regle marge / profitabilite avec fichiers obligatoires
- Bridge MEOW `direct_command > mapping_trigger > request_queue`
- Journaux append-only MEOW + TODO
- Generation de `DONE__` / `FAILED__` sur le Bureau
- Separation `RUN_NOW` / `RUN_POST_GO_LIVE` / `DEV_FUTUR`

## Capacites explicitement deleguees
- Maintenance systeme, policy, write-intent, schema, synchronisation technique -> `C:/Users/engue/.codex/skills/systeme-meow-paw-paw/SKILL.md`
- Demande generaliste Persona, n8n, support hors Meow -> `C:/Users/engue/.codex/skills/process-onedrive-persona/SKILL.md`

## Capacites laissees dans les satellites externes
- `INDEX SOURCES.json` reste l index business de verite
- `SKU.json`, `COMPTA_PARAMETERS.json`, `MARKETPLACE RULES.json` restent des sources consultees

## Regles basculees dans le skill
- `domaine_marque.regle.json` devient `governance/domaine-marque.regles.json`
- `taches_backend.regle.json` devient `governance/taches-backend.regles.json`
- les references actives du process skill et du bridge pointent maintenant vers les modules internes

## Non repris volontairement
- Aucun vieux chemin legacy `INDEX SYSTEM` ou catalogue schema embarque
- Aucune verite business recopiee dans `governance/`
- Aucune maintenance systeme lourde executee depuis ce process
