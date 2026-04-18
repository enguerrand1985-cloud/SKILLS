# Sources Externes

Ce fichier est strictement conditionnel.

Ne pas le lire par defaut.
Le lire seulement si `common.regles.json` a etabli qu'une source externe doit vraiment etre ouverte.

## Quand l'ouvrir
- write-intent sur un fichier de verite Meow
- confirmation de posture systeme ou de scope d'execution
- resolution de chemin via le process Meow et `INDEX SOURCES_MEOW_PAW_PAW.json`
- verification de frontiere entre maintenance systeme et verite business
- demande mixte impliquant une source business reelle

## Sources candidates

### Source 1
- Nom: `process-onedrive-meow-paw-paw`
- Role: posture process et frontiere business vs maintenance
- Chemin: `C:/Users/engue/.codex/skills/process-onedrive-meow-paw-paw/SKILL.md`
- Lire si: posture d'execution, write-intent ou scope Meow a confirmer

### Source 2
- Nom: `process-onedrive-meow-paw-paw/governance/routing.regles.json`
- Role: routage canonique Meow et resolution des chemins
- Chemin: `C:/Users/engue/.codex/skills/process-onedrive-meow-paw-paw/governance/routing.regles.json`
- Lire si: chemin, routage ou policy de lecture a confirmer

### Source 3
- Nom: `INDEX SOURCES_MEOW_PAW_PAW.json`
- Role: routage business visible
- Chemin: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/INDEX SOURCES_MEOW_PAW_PAW.json`
- Lire si: frontiere maintenance vs business, demande mixte ou selection d'une source metier

### Source 4
- Nom: `PARAMETERS/`
- Role: regles metier externes
- Chemin: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/MEOW PAW PAW/PARAMETERS`
- Lire si: maintenance impactant l'execution business ou besoin d'un contrat metier externe

### Source 5
- Nom: racine data business Meow
- Role: contenu metier externe
- Chemin: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/MEOW PAW PAW`
- Lire si: la demande vise explicitement une source de verite business apres qualification du sous-cas
