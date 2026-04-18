# Sources Externes

## Source 1
- Nom: `C:/Users/engue/.codex/AGENTS.md`
- Role: routage canonique de l'environnement utilisateur
- Chemin / emplacement: `C:/Users/engue/.codex/AGENTS.md`
- Statut de verite: routeur de priorite externe
- Mode d'usage: lire avant toute ecriture si le scope ou l'agent applicable sont ambigus

## Source 2
- Nom: `INDEX SOURCES_PERSONA.json`
- Role: index de routage des sources visibles PERSONA/MICRO/SASU
- Chemin / emplacement: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/INDEX SOURCES_PERSONA.json`
- Statut de verite: index de navigation externe
- Mode d'usage: lire quand la demande implique des fichiers de scope ou des dependances visibles

## Source 3
- Nom: fichiers de scope
- Role: sources metier cibles pour creation, maintenance ou patch
- Chemin / emplacement: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/PERSONA/_DATA - PERSONA_/PERSONA.json`, `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/PERSONA/_DATA - MICRO_/MICRO.json`, `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/PERSONA/_DATA - SASU_/SASU.json`
- Statut de verite: sources de verite metier externes
- Mode d'usage: lire uniquement la cible utile et rester ferme au scope

## Source 4
- Nom: fichier cible utilisateur
- Role: support d'entree heterogene ou fiche existante a maintenir
- Chemin / emplacement: variable selon la demande
- Statut de verite: source d'entree externe
- Mode d'usage: extraire uniquement les faits explicites et ne jamais inventer le reste
