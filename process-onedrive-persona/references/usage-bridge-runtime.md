# Usage Bridge Runtime

## Quand lire ce document
- Quand la demande parle de `REQUEST`, `DONE__`, `FAILED__`, bridge, journal TODO ou mapping trigger
- Quand il faut rappeler la politique append-only ou la suppression conditionnelle des requests

## Regles operationnelles
- Priorite d entree: `direct_command > mapping_trigger > request_queue`
- Lire uniquement les requests TODO et ignorer les requests MEOW
- Ecrire dans `[ TODO ] Journal.md` en append-only uniquement
- Generer `DONE__` ou `FAILED__` dans `C:/Users/engue/OneDrive/BRIDGE`
- Supprimer une request seulement apres succes complet

## Frontiere
- La logique process reste ici
- Les fichiers metier modifies restent hors du skill
- `governance/taches-backend.regles.json` porte maintenant la doctrine backend du process skill
- `GPT.regle.json` reste externe pour cette phase
