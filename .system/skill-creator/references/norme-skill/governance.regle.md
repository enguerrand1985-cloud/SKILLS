# Governance

`governance/` est obligatoire par structure, mais son contenu peut rester leger pour un skill simple.

## Autorise
- `common.regles.json`
- `common.schema.json`
- `[module].regles.json`
- `[module].schema.json`

## Regles
- ne conserver que le declaratif actif minimal
- n'ajouter un `common` que si un vrai tronc commun existe
- alleger ou scinder un `common` trop lourd
- garder les schemas lourds hors lecture par defaut

## Interdit
- data verite externe
- documentation de support
- scripts executables
- catalogues figes
- ponts legacy caches
