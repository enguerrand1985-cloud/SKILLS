# Usage Section Todo

## Role
- `todo` contient une projection d'execution.
- `todo` n'est pas une source de verite pour les faits stables ni pour la logique stable.

## Regles
- Si une tache derive d'une regle existante, renseigner `rule_id`.
- Si une tache depend d'une entite canonique, renseigner `links`.
- Pour une occurrence documentaire recurrente avec date de validite explicite, stocker la date dans `valid_until`.
- `valid_until` et `status.next_run_at` ne servent pas la meme chose et ne doivent pas etre confondus.
- Lors d'un changement canonique impactant, rebuild les taches liees.
- Une tache recurrente marquee `DONE` doit etre reprojetee en `PLANNED` avec recalcul de `next_run_at`.
- Une tache `one_shot` ne reapparait pas automatiquement.

## Pointeurs
- Les dependances entre data, regles metier et todo passent par des ids stables.
- Les liens cross-scope sont interdits sans demande explicite.
- `LinkRef` doit contenir `type` et `ref_id`; `path` reste optionnel.
