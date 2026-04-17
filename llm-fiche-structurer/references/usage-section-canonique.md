# Usage Section Canonique

## Mini-index
- `mini_index` guide la lecture et evite le fourre-tout.
- Il doit au minimum pointer vers `regles_metier.rules_engine`, `data.canonique`, `todo` et la zone d'archives si elle existe.
- Les ids d'entree doivent etre uniques et la priorite doit rester stable.

## IDs
- Toute entite referencable doit avoir un id stable si elle n'est pas deja portee par une cle d'objet.
- Convention recommandee: `<TYPE>__<SCOPE>__<SLUG>`.
- La maintenance standard fait un overwrite in-place sur le meme id.
- Un ajout dans une liste ne se fait que sur instruction explicite de l'utilisateur.

## Canonique propre
- La fiche declare les faits, pas les preuves.
- `data.canonique` reste value-only.
- `data.canonique.documents_index` doit exister.
- Les cles de provenance type `sources`, `evidence`, `source_ref`, `context_ref`, `_source_contexts`, `paths_promoted`, `sample_excerpt`, `extraction` ne doivent pas apparaitre dans la fiche.

## Schema de domaine
- Chaque domaine canonique doit avoir une structure dediee.
- Les cles ad hoc hors schema sont interdites.
- En cas de manque, garder la structure et laisser la valeur vide ou nulle.
- Les services web metier se modelisent dans `data.canonique.profils_numeriques.digital_profiles[].services[]`.
- En `SASU`, `data.canonique.entreprise` ne doit pas embarquer un sous-objet `identifiants`.

## Donnees sensibles
- Ne jamais stocker CVV, mots de passe ou codes 2FA.
- Si une valeur sensible n'est pas stockee, utiliser `null` ou une policy de masquage adaptee.
