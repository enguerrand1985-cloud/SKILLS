# Usage Migration

## Nomenclature appliquee
- L'ancien tronc `governance/common.regles.json` a ete reduit aux garde-fous transverses minimaux.
- Les regles de resolution de scope ont ete sorties dans `governance/scope.regles.json`.
- Les blocs fonctionnels de fiche sont maintenant separes en:
  - `governance/canonique.regles.json`
  - `governance/archives.regles.json`
  - `governance/regles-metier.regles.json`
  - `governance/todo.regles.json`
  - `governance/notes.regles.json`
- Les mecanismes d'edition sont separes en `governance/patch.regles.json` et `governance/rebuild.regles.json`.
- `governance/validate.schema.json` reste le seul schema actif minimal conserve dans le skill.
- `governance/common.schema.json` a ete retire car il n'etait pas utile a l'execution.

## Lecture recommandee
1. Lire `SKILL.md`.
2. Lire `governance/common.regles.json`.
3. Lire `governance/scope.regles.json`.
4. Lire `governance/validate.regles.json` puis `governance/validate.schema.json`.
5. Completer avec `references/mapping-llm-fiche-structurer.md`.
6. Charger ensuite seulement les modules de section utiles.

## Note
- Le contenu utile observe lors de l'audit est conserve.
- L'architecture est maintenant alignee sur un decoupage par sections fonctionnelles de fiche LLM.
