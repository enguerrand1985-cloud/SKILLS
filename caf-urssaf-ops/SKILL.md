---
name: caf-urssaf-ops
description: "Executer un skill CAF/URSSAF/Provigis avec architecture rentable en contexte : routeur commun leger, modules metier separes, runtime commun lu seulement apres selection reelle du workflow, et references externes chargees uniquement si elles deviennent utiles. Utiliser ce skill pour declaration CAF, declaration URSSAF, controle Provigis ou execution combinee CAF+URSSAF. Ne pas l'utiliser pour une demande administrative generale hors protocoles portes par la gouvernance locale."
---

# MISSION
Executer les operations CAF, URSSAF et Provigis dans le perimetre `MICRO`, avec supervision utilisateur, tracabilite et synchronisation post-run, sans invention de donnees ni ecart silencieux.

# PORTEE
- Skill modulaire centre sur les operations `MICRO` CAF, URSSAF et Provigis.
- `governance/router.common.regles.json` est le seul tronc commun toujours lu.
- `governance/runtime.common.regles.json` porte le contrat runtime actif minimal; son detail operatoire est externalise dans `references/usage-runtime-common.md`.
- `governance/caf.regles.json`, `governance/urssaf.regles.json`, `governance/provigis.regles.json` et `governance/combined.regles.json` portent la logique metier active utile par sous-protocole.
- Le detail procedurier de chaque workflow vit dans `references/usage-<module>.md`, lu seulement apres selection du module.
- `governance/common.schema.json` reste le schema actif minimal du tronc commun partage, lu seulement si un controle structurel est requis.
- Le dossier `agents/` reste tolere pour la coherence de l'environnement, sans remplacer le point d'entree `SKILL.md`.
- Les verites externes restent hors skill et `references/sources-externes.md` demeure une reference conditionnelle.

# CONDITIONS D'ACTIVATION
- Activer quand la demande porte explicitement sur CAF, URSSAF, Provigis, ou un run combine CAF+URSSAF.
- Activer quand le besoin implique la lecture ou l'execution d'un sous-protocole declare dans `caf.regles.json`, `urssaf.regles.json`, `provigis.regles.json` ou `combined.regles.json`.
- Ne pas activer pour une demande administrative generale hors workflows portes par cette gouvernance locale.
- STOP si le scope cible n'est pas `MICRO` ou si le profil `DIGIPROF__MICRO__EDGE_PERSONNEL_ADMIN` ne peut pas etre resolu.

# ORDRE DE LECTURE
1. Toujours lire `governance/router.common.regles.json`.
2. Lire `references/mapping-caf-urssaf-ops.md` seulement si le sous-cas n'est pas immediat.
3. Lire ensuite uniquement un module metier parmi `caf.regles.json`, `urssaf.regles.json`, `provigis.regles.json` ou `combined.regles.json`.
4. Lire le `references/usage-<module>.md` correspondant seulement si le detail operatoire du module selectionne devient utile.
5. Lire `governance/runtime.common.regles.json` seulement si une execution reelle, une policy de reporting, une policy de synchronisation ou une policy de securite runtime doit etre appliquee.
6. Lire `references/usage-runtime-common.md` seulement si les details navigateur, reporting, sync ou securite runtime sont necessaires.
7. Lire `references/sources-externes.md` seulement si un chemin reel, une source externe ou une verification d'environnement devient necessaire.
8. Lire `governance/common.schema.json` seulement si la structure du tronc commun partage doit etre controlee ou modifiee.
9. Ne pas charger les autres modules metier si le sous-cas utile est deja resolu.

# ROUTAGE INTERNE
- Toujours lu: `router.common.regles.json`.
- Lu a la demande: `caf.regles.json`, `urssaf.regles.json`, `provigis.regles.json`, `combined.regles.json`.
- Detail operatoire conditionnel: `usage-caf.md`, `usage-urssaf.md`, `usage-provigis.md`, `usage-combined.md`.
- Runtime conditionnel: `runtime.common.regles.json`, puis `usage-runtime-common.md` si les policies runtime doivent etre appliquees avec precision.
- Dependances externes conditionnelles: `sources-externes.md` et `common.schema.json` seulement si le cas l'exige.
- Si la demande mentionne `caf` ou `rsa`, router vers `governance/caf.regles.json`.
- Si la demande mentionne `urssaf`, `declaration ca`, ou `declarer et payer`, router vers `governance/urssaf.regles.json`.
- Si la demande mentionne `provigis`, `documents`, `modifier` ou `statut vert`, router vers `governance/provigis.regles.json`.
- Si la demande mentionne une execution combinee, router vers `governance/combined.regles.json`, puis activer les modules `caf` et `urssaf` dans l'ordre prevu.
- Ne charger `runtime.common.regles.json` qu'apres selection reelle du workflow ou si un rapport, une sync ou une policy navigateur doit etre applique.
- Ne charger le `usage-<module>.md` correspondant qu'apres selection reelle du module.
- Ne charger `references/sources-externes.md` que si la resolution des verites externes est indispensable.
- Si aucun sous-cas n'est resolu, produire un STOP explicite.

# WORKFLOWS / PROTOCOLES
- `caf`: declaration CAF en s'appuyant sur les mois affiches, les montants issus du fichier Excel declare et les criteres de validation de la page de fin.
- `urssaf`: declaration URSSAF trimestrielle avec calcul du total services et verification avant paiement.
- `provigis`: controle en lecture seule du tableau documentaire et classification des statuts.
- `combined`: orchestration CAF puis URSSAF dans la meme session Edge persistante, avec mises a jour de taches et rapport final.
- `micro_json_sync_policy`: synchronisation post-run des taches `todo.recurring` dans `MICRO.json`.

# REGLES NON NEGOCIABLES
- Ne jamais inventer de montant, periode, statut ou resultat.
- Ne jamais reconcentrer la logique metier dans `router.common.regles.json`.
- Respecter la supervision utilisateur et la politique de securite declarees dans `runtime.common.regles.json` quand le runtime est engage.
- Traiter `MICRO.json`, le fichier Excel revenus et les portails cibles comme des verites externes.
- Stopper si les pre-requis UI, navigateur, compte ou fichiers sources ne sont pas resolus.
- Signaler toute variation d'interface ou divergence de donnees dans le rapport de run.

# CONDITIONS DE STOP
- Scope, profil ou source externe non resolus.
- Fichier Excel illisible, verrouille ou incoherent avec les mois attendus.
- Domaine, ecran ou tunnel UI inattendu pendant un workflow.
- Periode affichee, montants calcules ou recapitulatif final divergents.
- Ambiguite critique sur le protocole a executer ou sur le niveau de soumission autorise.

# FORMAT DE SORTIE
- Mode nominal: `RUN_REPORT`.
- Mode blocage: `STOP`.
- Enveloppe logique minimale: `mode`, `status`, `target`, `result`, `blockers`, `next_action`, `artifacts`.
- En sortie nominale, produire un rapport de run lisible et les artefacts markdown prevus par la gouvernance.
- En cas de STOP, produire au minimum `mode=STOP`, `status=BLOCKED`, `blockers=<cause explicite>`, `next_action=<action attendue>`.

# REFERENCES
- `governance/router.common.regles.json`
- `governance/runtime.common.regles.json`
- `governance/common.schema.json`
- `governance/caf.regles.json`
- `governance/urssaf.regles.json`
- `governance/provigis.regles.json`
- `governance/combined.regles.json`
- `references/mapping-caf-urssaf-ops.md`
- `references/usage-runtime-common.md`
- `references/usage-caf.md`
- `references/usage-urssaf.md`
- `references/usage-provigis.md`
- `references/usage-combined.md`
- `references/sources-externes.md`
- `references/usage-migration.md`
