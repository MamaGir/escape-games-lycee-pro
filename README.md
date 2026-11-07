# Escape games · Lycée professionnel céramique

Escape games pédagogiques pour le **CAP Décoration sur céramique**, séparés de ceux de l'école (dépôt `escape-games-cm1-cm2`). Ils reprennent le même moteur, avec une interface propre au lycée : portail dédié, charte bleue du CAP, niveaux **Essentiel / Expert** à la place de CM1 / CM2.

| Jeu | Chapitre | Classique | Immersif |
|---|---|---|---|
| C01 · Les fiches du four | Les pâtes céramiques (CAP 1) | `pates-ceramiques/` | `immersifs/pates-ceramiques/` |
| C02 · Panne à l'usine | La préparation des pâtes céramiques (CAP) | — (immersif uniquement) | `immersifs/preparation-pates/` |

## Arborescence

```
index.html                      portail du lycée pro (lit commun/donnees/catalogue.js)
commun/                         moteur commun (copie de celui de l'école)
  donnees/catalogue.js          catalogue des jeux du LYCÉE (remplace celui de l'école)
  lycee-pro/libelles.js         affiche Essentiel / Expert à la place de CM1 / CM2
pates-ceramiques/               jeu classique
immersifs/pates-ceramiques/     jeu immersif (moteur « Vingt mille lieues »)
preparation-pates/              données sources de « Panne à l'usine » (JSON générés, leçons, évaluations, photos)
immersifs/preparation-pates/    jeu immersif « Panne à l'usine »
outils/generer-pates-ceramiques.py              contenu du jeu → JSON (ne jamais éditer les JSON à la main)
outils/immersif/theme-pates-ceramiques.json     thème immersif (mots, grades, palette)
outils/immersif/completer-pates-ceramiques.py   décors, zones et narration de la version immersive
outils/photos/deposer-photos.py                 planche photo de la leçon 3
outils/generer-preparation-pates.py             contenu de « Panne à l'usine » → JSON (preparation-pates/assets/data)
outils/immersif/theme-preparation-pates.json    thème immersif de « Panne à l'usine »
outils/immersif/completer-preparation-pates.py  décors dessinés, zones et narration de « Panne à l'usine »
outils-tests/                   moteur de test (jsdom)
serveur.py · lancer.bat         serveur local (classe sans Internet, tableau de bord)
```

## Jouer en classe sans Internet (Windows)

1. Ouvrir le dossier du dépôt dans l'Explorateur.
2. Double-cliquer sur `lancer.bat` (Python doit être installé).
3. Le navigateur s'ouvre sur le portail ; les élèves tapent l'adresse affichée dans la fenêtre noire.

## Tester après une modification

Outil : **Invite de commandes** (touches Windows + R, taper `cmd`, Entrée), puis aller dans le dossier du dépôt (`cd "<chemin du dossier>"`).

```
python outils/generer-pates-ceramiques.py
python pates-ceramiques/tests/test_json.py
node pates-ceramiques/tests/test-jeu.js
node immersifs/pates-ceramiques/tests/test-immersif.js

python outils/generer-preparation-pates.py
python preparation-pates/tests/test_json.py
node immersifs/preparation-pates/tests/test-immersif.js
```

Les tests Node demandent jsdom une fois : `npm install jsdom@24`.

## Ajouter un jeu

1. Écrire un générateur `outils/generer-<jeu>.py` sur le modèle de celui des pâtes céramiques, copier `pates-ceramiques/` comme squelette.
2. Version immersive : depuis le dépôt de l'école, `python vingt-mille-lieues/outils/immersif/migrer-jeu.py <jeu> --theme <thème> --vers immersifs/<jeu>`, puis copier le dossier ici.
3. Ajouter une entrée dans `commun/donnees/catalogue.js` et le nom du dossier dans `JEUX_LYCEE` (`serveur.py`).

### Recréer la version immersive de « Panne à l'usine »

La version immersive est produite depuis le dépôt de l'école (`escape-games-cm1-cm2`, qui contient le migrateur) :

1. `python outils/generer-preparation-pates.py` (ici) écrit les données dans `preparation-pates/assets/data/`.
2. Dans le dépôt de l'école : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py <chemin>/preparation-pates --theme <chemin>/outils/immersif/theme-preparation-pates.json --vers immersifs/preparation-pates --force`.
3. `python outils/immersif/completer-preparation-pates.py <dossier immersifs/preparation-pates du dépôt de l'école>` puis copier les photos de `preparation-pates/assets/images/cartes/` dans `immersifs/preparation-pates/assets/images/cartes/`.
4. `python immersifs/preparation-pates/outils/embarquer-donnees.py`, puis copier le dossier `immersifs/preparation-pates/` dans ce dépôt et lancer le test immersif.

