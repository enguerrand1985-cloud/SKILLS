# Full Creation

Utiliser ce chemin pour :
- creation complete d'un skill modulaire ou hybride
- refactor complet d'un skill existant
- migration lourde vers `NORME_SKILL`
- audit complet avec correction structurelle

## Lecture attendue
- `schema.core.json`
- `schema.validation.json`
- `schema.governance.json`
- `schema.assets.json`
- `governance.regle.md`
- `references.regle.md`
- `assets.regle.md`

## Regles
- garder un `toujours lu` leger
- expliciter les chemins court, intermediaire et complet si le skill les supporte
- ne pas cacher un monolithe lourd sous un faux module
- ne conserver dans `governance/` que le declaratif actif minimal
- deplacer la doctrine detaillee vers `references/` quand cela reduit la lecture utile

## Resultat vise
- skill complet
- structure rentable
- validation lourde reservee aux vrais cas lourds
