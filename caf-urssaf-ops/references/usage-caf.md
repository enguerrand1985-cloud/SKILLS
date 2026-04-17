# Usage CAF

## Pre-checks
- Ouvrir Edge avec le profil personnel persistant.
- Si le profil est verrouille, fermer les processus `msedge` puis relancer une seule fois.
- Ouvrir l'URL d'entree CAF et verifier qu'on reste dans les domaines CAF / FranceConnect / impots attendus.
- Si la session est deja authentifiee et placee sur le bon tableau de bord, ne pas rejouer l'authentification.

## Authentification
- Si necessaire, passer par `FranceConnect` puis `impots.gouv.fr`.
- Si `Continuer` reste desactive, re-cliquer dans le champ numero fiscal et choisir l'identite enregistree.
- Stopper si un MFA ou une demande manuelle bloque l'automatisation.

## Resolution des montants
- Lire d'abord les mois reellement affiches par le portail CAF.
- Lire ensuite le fichier Excel par feuille annuelle, ligne d'entete en ligne 3.
- Chercher le mois dans `Mois`, lire `Total Activite`, ignorer les lignes commencant par `Total`, puis tronquer a l'euro entier.

## Flow de declaration
- Depuis le tableau de bord CAF, ouvrir l'alerte RSA pour entrer dans le tunnel.
- Confirmer le profil si demande.
- Verifier les mois sur la page des ressources pre-remplies.
- Conserver `Revenus non salaries`.
- Cocher `Prestations commerciales ou artisanales`.
- Saisir les montants mensuels en euro entier.
- Positionner `Toujours en activite non salariee actuellement` sur `Oui`.
- Verifier le recapitulatif exact avant `Valider`.
- La fin attendue est la page `#/FIN` avec le message de succes.

## Variantes UI utiles
- Plusieurs boutons `Continuer` peuvent coexister: viser celui du formulaire principal.
- Des modales de validation peuvent interrompre le parcours et doivent etre acquittees.
- Le widget de chat peut masquer une zone sans changer le flow attendu.

## Reference de run validee
- Date observee: `2026-04-05`.
- Exemple de montants soumis: decembre 2025 = `283`, janvier 2026 = `480`, fevrier 2026 = `807`.
