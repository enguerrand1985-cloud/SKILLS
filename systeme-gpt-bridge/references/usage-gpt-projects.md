# Usage gpt projects

Utiliser `governance/projects.regles.json` quand la demande cible un projet GPT ou un GPT nomme.

Ordre pratique :

1. Identifier la cible explicite.
2. Charger seulement la fiche projet ou GPT utile.
3. Ouvrir ensuite les fichiers externes exacts de cette cible.
4. Charger un schema seulement si la demande parle de structure, validation ou migration.

Guides rapides :

- `TODO`
  - utile pour journal, render, priorisation, request lifecycle transverse
  - peut coexister avec un handoff vers `process-onedrive-persona`

- `MEOW_PAW_PAW`
  - utile pour pilotage GPT business Meow
  - si la demande devient maintenance systeme Meow, handoff vers `systeme-meow-paw-paw`
  - si la demande devient business OneDrive local, handoff vers `process-onedrive-meow-paw-paw`

- `SYSTEM_IA`
  - charger ensuite `governance/system-ia.regles.json`
  - traiter le context pack et les copies legacy comme un sous-cas GPT

- `ASSETS_STUDIO`
  - utile pour image config, prompt de pack visuel et contrat de sortie
  - ne pas basculer vers un skill image si la demande reste purement gouvernance GPT

- `GPT_SCROOGE`
  - utile pour maintenance du GPT personnalise et de son contexte
  - ne pas l utiliser comme routeur metier global
