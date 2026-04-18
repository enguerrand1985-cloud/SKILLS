# Usage Provigis

## Perimetre
- Le workflow est strictement en lecture seule.
- Actions autorisees: lire, classifier, rapporter.
- Actions interdites: upload, edition, soumission.

## Pre-checks
- Ouvrir Edge avec le profil personnel persistant.
- Si le profil est verrouille, fermer les processus `msedge` puis relancer une seule fois.
- Ouvrir directement le tableau de bord Provigis.

## Recuperation en cas de boucle
- Symptome de reference: spinner qui boucle et tableau de bord absent.
- Recuperation: cliquer l'icone de sortie, attendre la page de login, choisir l'identite email enregistree, puis se reconnecter.
- Stopper si le domaine Provigis attendu n'est pas respecte ou si la connexion ne peut pas repartir avec le profil enregistre.

## Lecture et classement
- Lire uniquement la liste des documents et leur colonne de statut.
- Signaux verts: `Valide`, `valide jusqu au`.
- Signaux d'attention: statut orange, `A modifier`, `Modifier`.
- Si tout est vert, conclure `ALL_GREEN`.
- Si un document demande action ou est orange, conclure `ACTION_REQUIRED`.

## Rapport
- Produire un fichier Markdown sur le Bureau.
- Sections attendues: `PROVIGIS RESULTAT`, `DOCUMENTS VERTS`, `DOCUMENTS A MODIFIER`, `HORODATAGE`, `NOTES_UI`.
- Si utile, la sync des taches Provigis de `MICRO.json` peut etre enchainee via la policy runtime.

## Variantes UI utiles
- Le dashboard mobile peut boucler avant le handoff de login.
- La connexion peut proposer `Suivant` puis `Se connecter`, ou directement `Se connecter`.
- Les liens d'action peuvent etre `Consulter` ou `Modifier` selon la ligne.
