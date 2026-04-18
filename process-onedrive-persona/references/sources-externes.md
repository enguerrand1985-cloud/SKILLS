# Sources Externes

## Source 1
- Nom: `INDEX SOURCES_PERSONA.json`
- Role: routage principal du perimetre PERSONA/MICRO/SASU
- Chemin / emplacement: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/INDEX SOURCES_PERSONA.json`
- Statut de verite: routage canonique externe
- Mode d'usage: lire avant toute execution pour resoudre scope, profil et politiques associees

## Source 2
- Nom: `MICRO.json`
- Role: source metier cible pour les mises a jour de `todo.recurring`
- Chemin / emplacement: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/PERSONA/_DATA - MICRO_/MICRO.json`
- Statut de verite: source de verite metier externe
- Mode d'usage: lire avant synchronisation et mettre a jour uniquement selon la policy declaree

## Source 3
- Nom: `Micro_revenus_2025-2035.xlsx`
- Role: source des montants CAF et URSSAF
- Chemin / emplacement: `C:/Users/engue/__SYSTEME - GITHUB__/SOURCE OF TRUTH/PERSONA/_DATA - MICRO_/Micro_revenus_2025-2035.xlsx`
- Statut de verite: source de verite operationnelle externe
- Mode d'usage: lire les feuilles et colonnes attendues sans inventer de valeurs

## Source 4
- Nom: portails CAF, URSSAF et Provigis
- Role: interfaces d'execution et de verification
- Chemin / emplacement: URLs declarees dans `governance/common.regles.json`
- Statut de verite: source UI externe
- Mode d'usage: executer le protocole demande en respectant les domaines attendus et les criteres de stop
