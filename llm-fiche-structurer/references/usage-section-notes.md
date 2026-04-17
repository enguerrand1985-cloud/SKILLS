# Usage Section Notes

## Role
- `notes` reste une zone d'appoint structuree.
- Elle accueille les elements ambigus, contradictoires, incomplets ou en attente de confirmation.

## Structure
- `notes` doit etre une liste d'objets.
- Champs attendus: `id`, `title`, `content`, `tags`, `created_at`, `updated_at`.
- Si un legacy stocke une liste de strings, la migration vers des objets doit se faire sans perte.

## Triage
- Toute donnee entrante doit etre triee avant ecriture.
- Les bacs autorises sont `data.canonique`, `data.scope_specifique.archives`, `data.canonique.documents_index` et `notes`.
- Une donnee ambigue, contradictoire ou incomplete ne va jamais directement en canonique.
- Une cle ad hoc non modelee en canonique impose d'abord une evolution de schema.

## Ecriture canonique
- Une ecriture canonique exige instruction explicite, conformite schema, conformite regles et validation utilisateur explicite.
- Si les informations manquent, demander les champs ou garer l'element en notes.
