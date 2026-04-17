---
name: systeme-meow-paw-paw
description: Skill unique hybride de maintenance systeme Meow Paw Paw. Utiliser ce skill pour router une demande de maintenance systeme, choisir entre runtime dense de maintenance et module cible de synchronisation, verifier des references explicites, ou controler la coherence locale sans recharger inutilement tout le socle externe.
---

# MISSION
Maintenir, auditer et patcher la gouvernance technique Meow Paw Paw sans perte de garde-fous, avec un routeur minimal toujours lu, un runtime dense differe pour la maintenance lourde, un module cible pour la synchronisation technique, des references externes strictement conditionnelles et des controles deterministes dans `scripts/`.

# PORTEE
- Skill unique hybride organise autour de `common`, `update` et `sync`.
- `governance/common.regles.json` sert uniquement de routeur minimal.
- `governance/update.regles.json` sert de runtime dense differe pour la maintenance lourde.
- Le detail de doctrine, de lecture de couches de verite et de formatting runtime est externalise dans `references/usage-update-runtime.md`.
- `governance/sync.regles.json` sert de module cible pour nommage, ids, conventions et alignement technique.
- `references/` ne fournit que du support conditionnel.
- `assets/` contient les seules bases structurelles locales passives du skill.
- `scripts/` porte les verifications deterministes repetables, y compris le controle de coherence d update avant ecriture.
- `agents/` reste tolere pour l'environnement, sans remplacer `SKILL.md`.

# CONDITIONS D'ACTIVATION
- Activer quand la demande porte sur la maintenance systeme Meow, son routage, ses contrats de lecture, ses garde-fous de write-intent, ses conventions techniques ou ses dependances explicites.
- Activer avant toute ecriture sur un fichier de verite du perimetre Meow ou sur un fichier cite comme gouvernance systeme.
- Ne pas activer pour une simple lecture business sans maintenance systeme.
- STOP si le perimetre, la cible ou le niveau d'intervention ne sont pas resolus.

# ORDRE DE LECTURE
1. Toujours lire `governance/common.regles.json`.
2. Lire `governance/update.regles.json` seulement pour un full-run systeme, un write-intent, un changement de policy, un changement structurel ou un audit lourd de coherence.
3. Lire `references/usage-update-runtime.md` seulement si la doctrine detaillee de maintenance, de couches de verite ou de rendu runtime devient necessaire.
4. Lire `governance/sync.regles.json` seulement si la demande touche la nomenclature, les ids, les conventions de fichiers ou la synchronisation technique.
5. Lire `references/sources-externes.md` seulement si une source externe doit effectivement etre ouverte.
6. Lire `references/mapping-systeme-meow-paw-paw.md` seulement si un rappel rapide de routage interne aide l'analyse.
7. Lire `references/usage-migration.md` seulement pour migration, historique ou arbitrage de refactor.
8. Lire un fichier de `assets/` seulement si une base structurelle locale est necessaire.
9. Executer un script de `scripts/` seulement si une verification deterministe apporte un vrai gain.

# ROUTAGE INTERNE
- Toujours lu: `common.regles.json`.
- Full-run / write-intent / policy / structure: `common` -> `update` -> `usage-update-runtime` si utile -> `sources-externes` -> source externe cible -> `check_update_coherence.py` si la modification injecte une information de verite -> autre script de verification si utile.
- Sync / nomenclature / ids / conventions: `common` -> `sync` -> asset utile si necessaire -> script de verification si utile.
- Controle local / drift / chemin / asset: `common` -> script cible -> `update` ou `sync` seulement si le controle revele un besoin de contexte supplementaire.
- `references/sources-externes.md` n'est jamais lu par defaut.
- `usage-migration.md` n'entre jamais dans le runtime courant.
- Si aucun sous-cas n'est resolu, produire un STOP explicite.

# WORKFLOWS / PROTOCOLES
- `router`: qualifier la demande et choisir le chemin court ou dense.
- `update-runtime`: appliquer les regles systeme, contrats, garde-fous write-intent et change management.
- `update-coherence`: identifier la source primaire, les dependances inverses, les duplications candidates et le scope coherent a patcher avant validation.
- `sync-targeted`: appliquer les conventions de nommage, ids et synchronisation technique.
- `path-coherence`: verifier les chemins explicites avant correction.
- `reference-drift`: reperer une reference legacy ou une dependance runtime qui ne devrait plus etre la.
- `asset-consistency`: verifier la coherence locale des assets passifs.

# REGLES NON NEGOCIABLES
- Ne jamais exposer la maintenance-only governance comme verite business.
- Ne jamais inventer de chemin, de dependance, de schema ou de scope.
- Ne jamais lire une reference externe par defaut si le routeur n'en a pas etabli le besoin.
- Ne jamais reintroduire de catalogue legacy `.schema.json` dans le runtime du skill.
- Ne jamais confondre lecture business (`INDEX SOURCES`) et lecture maintenance (`common` / `update` / `sync`).
- Les seules bases structurelles locales admises sont les fichiers passifs de `assets/`.

# CONDITIONS DE STOP
- Perimetre ou cible non resolus.
- Write-intent sans niveau de validation suffisant.
- Divergence structurelle non arbitree entre gouvernance systeme et sources business.
- Reference explicite cassee ou hors perimetre apres audit.
- Sous-cas non qualifiable par le routeur minimal.

# FORMAT DE SORTIE
- Modes autorises: `ANALYZE`, `PATCH_PLAN`, `STOP`.
- Enveloppe logique minimale: `mode`, `status`, `target`, `result`, `blockers`, `next_action`, `artifacts`.
- Pour une analyse, signaler les modules et references reellement lus.
- Pour un plan de patch, expliciter le sous-cas, les fichiers touches et les verifications a lancer.
- En STOP, produire au minimum `mode=STOP`, `status=BLOCKED`, `blockers=<cause explicite>`, `next_action=<action attendue>`.

# REFERENCES
- `governance/common.regles.json`
- `governance/update.regles.json`
- `governance/sync.regles.json`
- `references/mapping-systeme-meow-paw-paw.md`
- `references/usage-update-runtime.md`
- `references/sources-externes.md`
- `references/usage-migration.md`
- `scripts/check_path_coherence.py`
- `scripts/check_update_coherence.py`
- `scripts/check_reference_drift.py`
- `scripts/check_asset_consistency.py`
