# Mapping Entree Vers Fiche LLM

## Portee du skill
- Ce mapping couvre la creation, la maintenance complete, le patch cible, le rebuild `todo` et la validation finale.
- Le noyau toujours lu est `governance/router.regles.json`.
- Le detail doctrinal des modules de section est lu seulement si le module est effectivement mobilise.

## Scope
1. Identifier si la fiche cible est un master scope (`PERSONA`, `MICRO`, `SASU`, etc.).
2. Si c'est un child scope, renseigner explicitement `scope_header.parent_scope`.
3. Ne jamais faire de cross-scope implicite.
4. En cas de doute sur le scope ou le child scope, passer d'abord par `references/intake-llm-fiche-structurer.md`.
5. Lire `governance/scope.doctrine.regles.json` puis `references/usage-scope-doctrine.md` seulement si la doctrine de scope devient utile.

## Placement par section
1. Fait stable et modelisable -> `governance/section.canonique.regles.json` puis `references/usage-section-canonique.md` si besoin.
2. Historique, trace non canonique ou complement -> `governance/section.archives.regles.json` puis `references/usage-section-archives.md` si besoin.
3. Regle, procedure, policy, template ou cadre de decision -> `governance/section.regles-metier.regles.json` puis `references/usage-section-regles-metier.md` si besoin.
4. Action a executer ou occurrence projetee -> `governance/section.todo.regles.json` puis `references/usage-section-todo.md` si besoin.
5. Ambiguite, anomalie, arbitrage ou verification a faire -> `governance/section.notes.regles.json` puis `references/usage-section-notes.md` si besoin.

## Routing operationnel
1. Creation ou maintenance complete -> chemin dense `governance/full_run.regles.json`.
2. Diff minimal -> activer `governance/patch.regles.json` puis `references/usage-patch.md` si le detail de patch est utile.
3. Rebuild `todo` -> activer `governance/section.todo.regles.json`, puis `governance/rebuild.regles.json`, puis `references/usage-rebuild.md` si necessaire.
4. Validation seule -> activer `governance/validate.regles.json` et ne lire `governance/validate.schema.json` qu'en cas de mutation structurelle ou de validation lourde explicite.

## Anti-erreurs
- Ne jamais copier une logique metier dans `todo` si elle existe deja dans `regles_metier`.
- Ne jamais ajouter de cle libre hors schema.
- Ne jamais introduire de cles de provenance interdites (`sources`, `evidence`, `source_ref`, etc.).
- Ne jamais projeter des liens cross-scope sans demande explicite.
- Sur un fichier deja existant, ne pas faire de reserialisation globale si un patch cible suffit.
- Ne jamais valider un fichier avec caracteres casses: corriger l'encodage avant livraison.
