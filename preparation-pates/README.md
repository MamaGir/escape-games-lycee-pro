# Panne à l'usine — données sources

Jeu **immersif uniquement** (C02) : le jeu se joue dans `../immersifs/preparation-pates/`.
Ce dossier contient les **données sources**, générées par `outils/generer-preparation-pates.py` (ne jamais modifier les JSON à la main) :

| Fichier | Contenu |
|---|---|
| `assets/data/enigmes.json` | 5 salles, 15 énigmes Essentiel / 20 énigmes Expert |
| `assets/data/dialogues.json` | personnages inventés, présentations, mots-clés du coffre |
| `assets/data/lecons.json` | 5 leçons (bibliothèque du jeu) |
| `assets/data/evaluations.json` | quiz final, QCM, questions fermées, études de documents |
| `assets/data/lecons-a4.json` | leçons imprimables (schémas dessinés par script) |
| `assets/images/cartes/q-*.jpg` | photos des machines utilisées dans les énigmes 2-2 et 4-1 |

Source du contenu : cours « La préparation des pâtes céramiques » (CAP, version V9). Points à confirmer : `A-VERIFIER.md`.

## Contrôler

```
python outils/generer-preparation-pates.py
python preparation-pates/tests/test_json.py
node immersifs/preparation-pates/tests/test-immersif.js
```

## Parcours

| Salle | Mot du coffre | Contenu |
|---|---|---|
| 1 · Le laboratoire | BARBOTINE | les deux méthodes, le vocabulaire |
| 2 · La salle de broyage | DÉLAYAGE | étapes communes 1 à 5 et leurs machines |
| 3 · Le hall de production | PRODUITS | pâtes plastiques, barbotine de coulage, poudres atomisées |
| 4 · La tour d'atomisation | ATOMISEUR | atomisation, machines du hall, entreprises |
| 5 · L'atelier voie sèche | EXTRUSION | voie sèche, comparaison, sécurité avec les poudres |
