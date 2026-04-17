# Usage Rebuild

## Role
- `rebuild` sert a reconstruire `todo` proprement apres une mutation canonique ou un besoin explicite de reprojection.

## Points d'appui
- Le rebuild s'appuie sur `regles_metier.rules_engine.rules`.
- La priorite va aux correspondances par `rule_id` et `links`.
- Les taches liees a une entite canonique modifiee doivent etre recomposees.

## Recurring
- Une occurrence recurrente documentaire peut porter `valid_until`.
- Quand elle passe `DONE`, le rebuild doit recalculer `next_run_at` et remettre l'etat a `PLANNED`.
- Une tache `one_shot` reste terminee tant qu'aucune reouverture explicite n'est demandee.

## Garde-fous
- Pas de liens cross-scope sans demande explicite.
- Pas de drift de schema.
- Pas de reserialization lourde si un rebuild borne suffit.
- Pas d'ecriture silencieuse.
