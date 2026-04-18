# Usage Sources Vs System

## Quand lire ce document
- Quand la demande hesite entre lecture business et maintenance systeme
- Quand il faut justifier pourquoi `INDEX SOURCES` doit etre lu avant la couche systeme
- Quand un write-intent Meow apparait

## Regle centrale
- Lecture business: partir de `INDEX SOURCES.json`, des workbooks et des regles de domaine
- Maintenance systeme: handoff vers `C:/Users/engue/.codex/skills/systeme-meow-paw-paw/SKILL.md`
- Ne pas confondre un besoin de run business avec un besoin de patch systeme

## Garde-fous
- STOP si le sous-cas business vs systeme reste ambigu
- STOP si un write-intent apparait sans cadre de maintenance explicite
- Garder les journaux en append-only meme quand la demande finit en handoff systeme
