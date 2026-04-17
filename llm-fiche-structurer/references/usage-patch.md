# Usage Patch

## Doctrine de maintenance
- Une modification de fiche n'est proposee que sur instruction explicite de l'utilisateur.
- Aucune ecriture silencieuse.
- Par defaut, la maintenance vise `data.canonique` et `todo`.
- Les autres sections ne sont touchees que sur demande explicite.

## Minimalite
- Ne modifier que ce qui est necessaire pour refleter le fait declare.
- Conserver les valeurs existantes pour les champs non fournis.
- Effacer ou masquer un champ uniquement sur instruction explicite.
- Si une information manque ou reste contradictoire, demander ou garer en notes.

## Modes de sortie
- Modes autorises: `FULL_REPLACE`, `MERGE_PATCH_RFC7396`, `PATCH_RFC6902`.
- Mode recommande par defaut: `MERGE_PATCH_RFC7396`.
- `PATCH_RFC6902` seulement si le consommateur sait l'appliquer.
- Le payload de sortie doit etre du JSON pur, sans prose melangee.
- Enveloppe minimale recommande: `mode`, `target_filename`, `scope`, `payload`.
