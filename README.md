# Escape games · Lycée professionnel céramique

Escape games pédagogiques pour le **CAP Décoration sur céramique**, séparés de ceux de l'école (dépôt `escape-games-cm1-cm2`). Ils reprennent le même moteur, avec une interface propre au lycée : portail dédié, charte bleue du CAP, niveaux **Essentiel / Expert** à la place de CM1 / CM2.

| Jeu | Chapitre | Classique | Immersif |
|---|---|---|---|
| C01 · Les fiches du four | Les pâtes céramiques (CAP 1) | `pates-ceramiques/` | `immersifs/pates-ceramiques/` |
| C02 · Panne à l'usine | La préparation des pâtes céramiques (CAP) | — (immersif uniquement) | `immersifs/preparation-pates/` |
| C03 · Le bon de lancement | La préparation des matières premières (CAP) | `matieres-premieres/` | `immersifs/matieres-premieres/` |
| L01 · Le four verrouillé (version légère, un seul fichier) | Les pâtes céramiques (CAP 1) | `four-verrouille/` | — |

## Accès aux jeux

Trois façons de jouer, avec les mêmes jeux et les mêmes outils d'enseignant.

| Mode | Adresse | Suivi en direct, classement, résultats |
|---|---|---|
| **En ligne, partout** (GitHub Pages) | https://mamagir.github.io/escape-games-lycee-pro/ | non |
| **Réseau local** (classe, sans Internet) | `http://<adresse du poste>:8000/` | oui |
| **Hors connexion** | application installée, ou archive zip par jeu | non |

### En ligne (une seule mise en route)

Outil : le site github.com, connecté avec le compte **MamaGir**.

1. Ouvrir https://github.com/MamaGir/escape-games-lycee-pro.
2. **Settings** (onglet en haut à droite) → **Pages** (menu de gauche).
3. Sous **Build and deployment** → **Source** : choisir **Deploy from a branch**.
4. **Branch** : `main`, dossier `/ (root)`, puis **Save**.
5. Attendre une à deux minutes, recharger la page : l'adresse du site s'affiche en haut (https://mamagir.github.io/escape-games-lycee-pro/).
6. Après chaque modification poussée sur `main`, le site se met à jour en une minute (Ctrl + F5 pour voir la nouvelle version).

### Réseau local (classe)

Outil : l'explorateur de fichiers, puis la fenêtre noire du serveur.

1. Ouvrir le dossier du dépôt dans l'Explorateur.
2. Double-cliquer sur `lancer.bat` (Windows, Python installé) ou `lancer-mac.command` (Mac).
3. Si Windows demande d'autoriser Python : cocher **Réseaux privés**, puis **Autoriser l'accès**.
4. Le navigateur s'ouvre sur le portail. La fenêtre noire affiche **« ADRESSES À DONNER AUX ÉLÈVES »** : les élèves, sur le même Wi-Fi ou le même réseau filaire, tapent cette adresse (de la forme `http://192.168.x.x:8000/pates-ceramiques/`).
5. Sur le poste de l'enseignant : http://127.0.0.1:8000/enseignant.html (espace enseignant), http://127.0.0.1:8000/verifier.html (vérification), http://127.0.0.1:8000/classement.html (classement à projeter).
6. Fermer la fenêtre noire pour arrêter le serveur.

Les résultats des élèves sont gardés dans `resultats-classe.jsonl` sur le poste de l'enseignant ; ce fichier n'est jamais publié (`.gitignore`). Sur une adresse locale en `http://`, l'installation de l'application n'est pas proposée par les navigateurs : c'est normal.

### Hors connexion

- **Application** : ouvrir le site en ligne une fois avec Internet dans Chrome ou Edge, attendre « Prêt hors connexion » dans le bloc du portail, puis **Installer l'application**.
- **Archive zip par jeu** : https://github.com/MamaGir/escape-games-lycee-pro/releases/tag/hors-ligne (fabriquée automatiquement après chaque publication). Décompresser, double-clic sur `JOUER.html`.

### Contrôle et synthèse (espace enseignant)

| Page | Rôle |
|---|---|
| `enseignant.html` | tout au même endroit : jouer, tableau de bord, guides, leçons A4, points à vérifier, jeu par jeu |
| `<jeu>/prof.html` | tableau de bord d'un jeu, en direct (réseau local) |
| `classement.html` | classement des équipes, à projeter (réseau local) |
| `resultats.html` | bilan de la classe, énigme par énigme |
| `passeport.html` | compétences travaillées par élève |
| `trophees.html` | trophées des équipes |
| `verifier.html` | contrôle des énigmes, des données et des médias, accès direct à chaque énigme |

Ces pages se construisent à partir de `commun/donnees/catalogue.js` : un jeu ajouté au catalogue y apparaît seul.

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
matieres-premieres/             jeu classique « Le bon de lancement » (C03)
immersifs/matieres-premieres/   jeu immersif « Le bon de lancement »
outils/generer-matieres-premieres.py            contenu de « Le bon de lancement » → JSON
outils/immersif/theme-matieres-premieres.json   thème immersif de « Le bon de lancement »
outils/immersif/completer-matieres-premieres.py décors, zones et narration de « Le bon de lancement »
outils/generer-pates-ceramiques.py              contenu du jeu → JSON (ne jamais éditer les JSON à la main)
outils/immersif/theme-pates-ceramiques.json     thème immersif (mots, grades, palette)
outils/immersif/completer-pates-ceramiques.py   décors, zones et narration de la version immersive
outils/photos/deposer-photos.py                 planche photo de la leçon 3
outils/generer-preparation-pates.py             contenu de « Panne à l'usine » → JSON (preparation-pates/assets/data)
outils/immersif/theme-preparation-pates.json    thème immersif de « Panne à l'usine »
outils/immersif/completer-preparation-pates.py  décors dessinés, zones et narration de « Panne à l'usine »
outils-tests/                   moteur de test (jsdom)
serveur.py · lancer.bat · lancer-mac.command    serveur local (classe sans Internet, tableau de bord)
enseignant.html · verifier.html · resultats.html · classement.html · passeport.html · trophees.html
sw.js · sw-fichiers.js · manifest.webmanifest   application installable, hors connexion
outils-pwa/                     liste des fichiers gardés hors connexion, archives zip par jeu
outils-tests/ · commun/tests/   tests automatiques (Node + jsdom)
.github/workflows/              archives hors connexion publiées dans la release « hors-ligne »
.claude/skills/produire-escape-lycee-pro-cap/   skill de production d'un nouveau jeu
PLAN-PRODUCTION.md              chapitres du cours à transformer en escape games
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

python outils/generer-matieres-premieres.py
python matieres-premieres/tests/test_json.py
node matieres-premieres/tests/test-jeu.js
node immersifs/matieres-premieres/tests/test-immersif.js
```

Les tests Node demandent jsdom une fois : `cd outils-tests`, `npm install`, `cd ..`.

Tous les tests d'un coup : `node outils-tests/tous.js` (quelques minutes). Contrôles avant publication :

```
node outils-tests/verifier-enigmes.js
node outils-tests/verifier-liens-internes.js
python outils-pwa/maj-hors-ligne.py          (puis git add sw-fichiers.js)
```

## Ajouter un jeu

1. Écrire un générateur `outils/generer-<jeu>.py` sur le modèle de celui des pâtes céramiques, copier `pates-ceramiques/` comme squelette.
2. Version immersive : depuis le dépôt de l'école, `python vingt-mille-lieues/outils/immersif/migrer-jeu.py <jeu> --theme <thème> --vers immersifs/<jeu>`, puis copier le dossier ici.
3. Ajouter une entrée dans `commun/donnees/catalogue.js` et le nom du dossier dans `JEUX_LYCEE` (`serveur.py`).
4. `python outils-pwa/maj-hors-ligne.py`, puis les tests ci-dessus.

Pour produire un jeu de bout en bout (cours → données → version immersive → médias → publication), utiliser le skill `produire-escape-lycee-pro-cap` (dossier `.claude/skills/`, ou fichier `produire-escape-lycee-pro-cap.skill` à importer dans Claude).

### Recréer la version immersive de « Panne à l'usine »

La version immersive est produite depuis le dépôt de l'école (`escape-games-cm1-cm2`, qui contient le migrateur) :

1. `python outils/generer-preparation-pates.py` (ici) écrit les données dans `preparation-pates/assets/data/`.
2. Dans le dépôt de l'école : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py <chemin>/preparation-pates --theme <chemin>/outils/immersif/theme-preparation-pates.json --vers immersifs/preparation-pates --force`.
3. `python outils/immersif/completer-preparation-pates.py <dossier immersifs/preparation-pates du dépôt de l'école>` puis copier les photos de `preparation-pates/assets/images/cartes/` dans `immersifs/preparation-pates/assets/images/cartes/`.
4. `python immersifs/preparation-pates/outils/embarquer-donnees.py`, puis copier le dossier `immersifs/preparation-pates/` dans ce dépôt et lancer le test immersif.

