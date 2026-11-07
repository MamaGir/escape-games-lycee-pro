## Régénérer les données et la documentation

1. Modifier le contenu dans `outils/generer-pates-ceramiques.py` (à la racine du dépôt), jamais dans les JSON.
2. `python outils/generer-pates-ceramiques.py`
3. `python pates-ceramiques/tests/test_json.py` puis `node pates-ceramiques/tests/test-jeu.js` (jsdom requis).
4. `python pates-ceramiques/tests/generer-readme.py` (ce fichier).

## Médias

Aucun média n'est nécessaire : décors et personnages sont dessinés (`js/decors.js`, `js/personnages.js`).
Planche photo facultative de la leçon 3 : `outils/photos/deposer-photos.py` (photos libres ou photos du cours, voir A-VERIFIER.md).
