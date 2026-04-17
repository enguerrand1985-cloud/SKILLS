# Validation

## Niveaux

### Quick
Pour :
- `create-minimal`
- `update-light`
- `validate-quick`
- ajout isole d'asset, de script ou de reference

Controle :
- socle canonique present
- frontmatter valide
- sections `SKILL.md` dans le bon ordre
- conventions de nommage evidentes

### Structural
Pour :
- `update-structure`
- `add-governance-light`
- `migrate-partial`

Controle :
- socle canonique
- coherence de lecture
- coherence de modules
- absence de contenu interdit evident

### Full
Pour :
- `create-full`
- `refactor-full`
- `audit-full`
- `migrate-full`

Controle :
- structure
- routage
- validation logique
- schemas lourds seulement si utiles

## Scope
- skills personnels : validation stricte
- skills systeme / OpenAI / externes : compatibilite standard toleree
