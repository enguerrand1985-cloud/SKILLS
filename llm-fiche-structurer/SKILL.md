---
name: llm-fiche-structurer
description: "Creer ou maintenir une fiche LLM JSON structuree a partir d'un contenu heterogene, avec architecture hybride rentable en contexte : routeur minimal, chemin dense pour create/full replace, modules de section pour patch cible, et validation lourde seulement si necessaire. Utiliser ce skill uniquement pour une demande explicite de structuration, maintenance, patch, alignement au schema, validation ou rebuild todo d'une fiche LLM. Ne pas l'utiliser pour une simple lecture de scope, une analyse business pure ou un support generaliste."
---

# MISSION
Produire ou maintenir une fiche LLM exploitable, conforme au schema actif, stable pour un usage multi-IA et sans invention de donnees.

# PORTEE
- Skill hybride par sections fonctionnelles de fiche LLM.
- `governance/router.regles.json` est le seul noyau toujours lu.
- `governance/full_run.regles.json` porte le chemin dense pour create / full replace.
- `governance/section.canonique.regles.json`, `governance/section.archives.regles.json`, `governance/section.regles-metier.regles.json`, `governance/section.todo.regles.json` et `governance/section.notes.regles.json` portent les contrats actifs minimaux des modules cibles.
- Le detail doctrinal de ces modules vit dans `references/usage-*.md`, lu seulement apres selection du module utile.
- `governance/scope.router.regles.json` et `governance/scope.doctrine.regles.json` portent la resolution de scope et la doctrine `sasuprofile`; le detail de doctrine est externalise dans `references/usage-scope-doctrine.md`.
- `governance/patch.regles.json` et `governance/rebuild.regles.json` portent les mecanismes actifs de patch et de reconstruction; leur detail de procedure vit dans `references/usage-patch.md` et `references/usage-rebuild.md`.
- `governance/validate.regles.json` porte la validation logique finale.
- `governance/validate.schema.json` reste le schema complet, lu seulement en cas de mutation structurelle, de doute de conformite ou de validation lourde explicite.
- `assets/skeleton_fiche_llm.json` reste un materiau passif de depart, et non un schema actif.
- Le dossier `agents/` reste tolere pour la coherence de l'environnement, sans remplacer le point d'entree `SKILL.md`.

# CONDITIONS D'ACTIVATION
- Activer uniquement sur demande explicite de structuration ou maintenance de fiche LLM.
- Activer quand l'utilisateur demande `structurer`, `normaliser`, `mettre en fiche LLM`, `aligner au schema`, `mettre a jour`, `maintenance complete`, `patch cible`, `validate` ou `rebuild todo`.
- Ne pas activer pour une simple lecture de source, une analyse metier generale ou une question hors fiche LLM.
- STOP si le scope cible, le parent scope, la section a modifier ou la nature de la sortie attendue restent structurellement ambigus.

# ORDRE DE LECTURE
1. Toujours lire `governance/router.regles.json`.
2. Si la demande est un full-run (`creation complete`, `full replace`, `maintenance complete`), lire `governance/full_run.regles.json`.
3. Si la demande est ciblee, lire `references/mapping-llm-fiche-structurer.md` seulement si l'aiguillage n'est pas evident, puis lire uniquement le module utile parmi `section.canonique`, `section.archives`, `section.regles-metier`, `section.todo`, `section.notes`, `patch` et `rebuild`.
4. Lire le `references/usage-<module>.md` correspondant seulement si le detail doctrinal ou procedurier du module selectionne devient utile.
5. Lire `governance/scope.router.regles.json` seulement si le scope, le `parent_scope` ou le type master/child n'est pas trivial.
6. Lire `governance/scope.doctrine.regles.json` seulement si la demande touche un child scope, un cas `SASU`, ou une doctrine de scope sensible.
7. Lire `references/usage-scope-doctrine.md` seulement si le detail de doctrine de scope est necessaire.
8. Lire `references/intake-llm-fiche-structurer.md` seulement si des informations de placement restent manquantes.
9. Lire `governance/validate.regles.json` seulement avant livraison, sur cas sensible, ou si la logique doit etre revalidee.
10. Lire `governance/validate.schema.json` seulement en cas d'ajout de cle, mutation structurelle, doute de conformite, ou validation lourde explicite.

# ROUTAGE INTERNE
- Toujours lu: `router.regles.json`.
- Lu en chemin dense: `full_run.regles.json`, puis `scope.router.regles.json` / `scope.doctrine.regles.json` seulement si requis par le scope.
- Lu a la demande: `section.canonique.regles.json`, `section.archives.regles.json`, `section.regles-metier.regles.json`, `section.todo.regles.json`, `section.notes.regles.json`, `patch.regles.json`, `rebuild.regles.json`.
- Detail doctrinal conditionnel: `usage-scope-doctrine.md`, `usage-section-canonique.md`, `usage-section-archives.md`, `usage-section-regles-metier.md`, `usage-section-todo.md`, `usage-section-notes.md`, `usage-patch.md`, `usage-rebuild.md`.
- Validation finale seulement si utile: `validate.regles.json`.
- Validation schema lourde seulement si structure touchee: `validate.schema.json`.
- Si la demande cible des faits stables ou des objets modelisables, router vers `governance/section.canonique.regles.json`.
- Si la demande cible de l'historique, du non-canonique ou des complements de trace, router vers `governance/section.archives.regles.json`.
- Si la demande cible des regles, procedures, policies ou templates, router vers `governance/section.regles-metier.regles.json`.
- Si la demande cible des actions a executer, router vers `governance/section.todo.regles.json`.
- Si la demande cible des anomalies, ambiguities ou points a verifier, router vers `governance/section.notes.regles.json`.
- Si la demande cible un diff minimal, activer en plus `governance/patch.regles.json`.
- Si la demande cible explicitement la reconstruction de `todo`, activer `governance/section.todo.regles.json` puis `governance/rebuild.regles.json`.
- Si aucun sous-cas n'est resolu, produire un STOP explicite.

# WORKFLOWS / PROTOCOLES
- `full_run_dense`: creer ou remplacer une fiche complete via `full_run.regles.json`, sans lecture en cascade de toutes les sections.
- `create_or_update`: maintenir une fiche complete en lisant uniquement les sections utiles puis en revalidant la sortie.
- `patch_targeted`: produire une sortie `MERGE_PATCH_RFC7396` ou `PATCH_RFC6902` quand un diff minimal suffit.
- `rebuild_todo`: reconstruire `todo` a partir des ids canoniques, `rule_id` et `links`.
- `validate_only`: controler regles non negociables, encodage UTF-8 et absence de mojibake, puis charger le schema complet seulement si la structure doit etre controlee.
- `sectional_routing`: choisir les bons modules de section avant toute ecriture.

# REGLES NON NEGOCIABLES
- Ne jamais inventer de valeurs absentes.
- Ne jamais faire d'inference cross-scope implicite.
- Ne jamais utiliser les archives comme source canonique.
- Ne jamais ajouter de cle hors schema.
- Ne jamais supprimer silencieusement des donnees canoniques.
- Ne jamais reconcentrer toute l'architecture de fiche dans un faux `common`.
- Preserver l'encodage et eviter toute corruption de caracteres lisibles.
- Sur une fiche existante, preferer un patch cible a une reserialisation complete si cela suffit.
- Garder explicitement la doctrine `sasuprofile` quand `scope = SASU` ou `parent_scope = SASU`.

# CONDITIONS DE STOP
- Scope, parent scope ou fichier cible non resolus.
- Schema actif, regle de conformite ou source externe necessaire non resolus.
- Contradiction structurelle entre les faits fournis et la cible.
- Demande d'ecriture sans instruction explicite ou sans niveau de sortie clair.
- Apparition de mojibake, corruption d'encodage ou divergence non resolue entre schema et contenu.

# FORMAT DE SORTIE
- Modes autorises: `FULL_REPLACE`, `MERGE_PATCH_RFC7396`, `PATCH_RFC6902`, `STOP`.
- Enveloppe logique minimale: `mode`, `status`, `target`, `result`, `blockers`, `next_action`, `artifacts`.
- En creation: produire un JSON complet exploitable.
- En maintenance: preferer un payload de patch si cela limite le bruit de diff.
- En STOP: produire au minimum `mode=STOP`, `status=BLOCKED`, `blockers=<cause explicite>`, `next_action=<action attendue>`.

# REFERENCES
- `governance/router.regles.json`
- `governance/full_run.regles.json`
- `governance/scope.router.regles.json`
- `governance/scope.doctrine.regles.json`
- `governance/section.canonique.regles.json`
- `governance/section.archives.regles.json`
- `governance/section.regles-metier.regles.json`
- `governance/section.todo.regles.json`
- `governance/section.notes.regles.json`
- `governance/validate.regles.json`
- `governance/validate.schema.json`
- `governance/patch.regles.json`
- `governance/rebuild.regles.json`
- `references/mapping-llm-fiche-structurer.md`
- `references/intake-llm-fiche-structurer.md`
- `references/usage-scope-doctrine.md`
- `references/usage-section-canonique.md`
- `references/usage-section-archives.md`
- `references/usage-section-regles-metier.md`
- `references/usage-section-todo.md`
- `references/usage-section-notes.md`
- `references/usage-patch.md`
- `references/usage-rebuild.md`
- `references/sources-externes.md`
- `references/usage-migration.md`
