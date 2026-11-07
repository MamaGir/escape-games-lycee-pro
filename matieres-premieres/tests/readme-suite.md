## Régénérer les données et la documentation

1. Modifier le contenu dans `outils/generer-matieres-premieres.py` (à la racine du dépôt), jamais dans les JSON.
2. `python outils/generer-matieres-premieres.py`
3. `python matieres-premieres/tests/test_json.py` puis `node matieres-premieres/tests/test-jeu.js` (jsdom requis).
4. `python matieres-premieres/tests/generer-readme.py` (ce fichier).

## Médias

Aucun média n'est nécessaire : décors et personnages sont dessinés (`js/decors.js`, `js/personnages.js`).
Photos facultatives : voir A-VERIFIER.md (licences à vérifier avant tout dépôt).
