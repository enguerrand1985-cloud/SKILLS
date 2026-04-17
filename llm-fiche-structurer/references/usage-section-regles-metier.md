# Usage Section Regles Metier

## Role
- `regles_metier` centralise regles stables, procedures, checklists et templates.
- Les faits n'y sont pas dupliques.

## Rules engine
- Les regles moteur vivent dans `regles_metier.rules_engine.rules`.
- Chaque regle porte au minimum `title`, `category`, `scope_binding`, `cadence`, `inputs`, `stop_conditions`, `outputs`, `status`.
- Les details longs peuvent vivre dans `regles_metier.procedures` et `regles_metier.templates_prompts`.

## Projection vers todo
- Une regle peut projeter des taches dans `todo`.
- Les taches projetees doivent porter `rule_id` et des `links` vers les entites canoniques pertinentes.
- La maintenance de `todo` doit privilegier un rebuild controle par `rule_id` et `links`.

## References internes
- Preferer une source unique plus des references internes plutot que de dupliquer le contenu.
- `regles_metier.references` peut servir de table `id -> {type, path, description}`.
