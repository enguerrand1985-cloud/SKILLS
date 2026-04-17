# Usage URSSAF

## Pre-checks
- Ouvrir Edge avec le profil personnel persistant.
- Si le profil est verrouille, fermer les processus `msedge` puis relancer une seule fois.
- Tenter l'URL de login direct, sinon passer par la page d'accueil et cliquer `Se connecter`.

## Authentification
- Sur la page `Mon compte`, utiliser la connexion pre-remplie du profil Edge.
- Stopper si le domaine attendu `autoentrepreneur.urssaf.fr` n'est pas present.
- Stopper si un prompt d'identification supplementaire ou un MFA bloque l'execution.

## Resolution des montants
- Utiliser le fichier `Micro_revenus_2025-2035.xlsx`.
- Prendre les mois cibles du trimestre traite.
- Lire `Mois` et `Total Activite`, tronquer a l'euro entier.
- Le montant `BIC prestations` vaut la somme des mois cibles.
- `BIC ventes = 0` et `BNC = 0` dans le cas de reference observe.

## Flow de declaration
- Aller sur `Gerer mon auto-entreprise`.
- Ouvrir `Mes echeances en cours` puis `Declarer et payer`.
- Selectionner la bonne periode active.
- Saisir les montants puis lancer `Calculer les cotisations et contributions`.
- Verifier que le chiffre d'affaires total correspond au total calcule.
- Enregistrer la declaration.
- Sur l'etape paiement, verifier le message `declaration enregistree` et le montant restant a charge.
- Ne cliquer `Payer` que si l'utilisateur a demande un end-to-end complet.

## Variantes UI utiles
- Certains libelles de navigation changent selon le layout.
- Le panneau de paiement peut varier mais conserve un libelle de montant a charge et un bouton principal `Payer`.

## Reference de run validee
- Date observee: `2026-04-05`.
- Periode detectee: `1er trimestre 2026`.
- Total trimestre services observe: `1804`.
- Snapshot cotisations observe: total `385`, cotisations `382`, CFP `2`, taxe `1`.
