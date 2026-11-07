# Rapport de migration — Panne à l'usine

Données sources : `preparation-pates/assets/data/` (générées par `outils/generer-preparation-pates.py`, **non modifiées** par la migration).
Variante immersive : `immersifs/preparation-pates/`.

- 5 salles, 15 énigmes Essentiel (grade matelot) / 20 énigmes Expert (grade timonier).
- Le moteur est une copie de celui de « Vingt mille lieues » ; seuls `js/jeu-config.js`, `css/theme.css`, `js/decors-secours.js` et `assets/data/*.json` sont propres à ce jeu.

## Complété (dépôt lycée pro)

- Thème : `outils/immersif/theme-preparation-pates.json` (grades Essentiel / Expert, palette du CAP, jauge « Pression »).
- `python outils/immersif/completer-preparation-pates.py immersifs/preparation-pates` : décors dessinés 16:9 (par script, aucune image IA), 20 zones nommées, problème narratif, enjeu, réaction du décor et répliques des deux grades pour les 20 énigmes ; libellés Essentiel / Expert.
- Photos des machines dans `assets/images/cartes/` (énigmes 2-2 et 4-1), fournies par l'enseignant : licence à vérifier (voir `preparation-pates/A-VERIFIER.md`).

## Reste facultatif

- Images de décor et portraits (`medias.csv`) : à produire seulement avec l'accord de l'enseignant ; recaler les zones avec `outils/caler-effets.html` si une image est déposée.
- Grades supplémentaires (mousse, lieutenant, second).

## Vérifier

```
node immersifs/preparation-pates/tests/test-immersif.js
```
