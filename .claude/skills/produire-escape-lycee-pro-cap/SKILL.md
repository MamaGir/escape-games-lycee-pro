---
name: "produire-escape-lycee-pro-cap"
description: "Produire ou transformer les escape games du lycée professionnel (CAP Décoration sur céramique, niveaux Essentiel / Expert) du dépôt MamaGir/escape-games-lycee-pro : choisir le mode (migrer un jeu au modèle immersif, créer un nouveau jeu à partir d'un chapitre du cours, produire ou ajouter des images et vidéos), puis appliquer la procédure complète (faits, données, leçons, intégration, tests, commit, publication)."
---

# Produire ou transformer un escape game du lycée pro (CAP)

Dépôt : GitHub `MamaGir/escape-games-lycee-pro` (branche `main`). Publié sur https://mamagir.github.io/escape-games-lycee-pro/ (GitHub Pages). Dépôt de référence de l'école, source du moteur immersif et des outils : `IdGir/escape-games-cm1-cm2` (en lecture seule).
Répondre en français, de façon concise. **Ne jamais faire `git push`** : c'est l'enseignant qui publie (hors session cloud, où la consigne de la session l'emporte). **Ne jamais fusionner une PR sans accord explicite.**

Trois façons de jouer, à rappeler en fin de session : **en ligne** (GitHub Pages, partout), **en réseau local** (`lancer.bat`, sans Internet, tableau de bord en direct), **hors connexion** (application installable ou archive zip par jeu).

## 0. Démarrage

1. Demander l'accès au dossier du dépôt (s'il n'est pas déjà connecté), puis travailler avec le shell de l'ordinateur. Le chemin du dossier n'est pas supposé : le demander.
2. Lire `README.md` (racine), le `README.md`, `GUIDE-PEDAGOGIQUE.md` et `A-VERIFIER.md` du jeu le plus proche (`pates-ceramiques/` est le modèle), `outils/generer-pates-ceramiques.py` (modèle de générateur), `outils/immersif/completer-pates-ceramiques.py` et `theme-pates-ceramiques.json` (modèle de version immersive), `commun/README.md` (moteur).
3. Lire `PLAN-PRODUCTION.md` (colonne « Fait »), `git log --oneline -5`, `git status -sb` : repérer les chapitres non faits et un éventuel commit non poussé (le signaler).
4. **Choisir le mode** (AskUserQuestion, une seule réponse) si l'utilisateur ne l'a pas donné :
   - **A. Migrer un jeu classique au modèle immersif** (§ 2) ;
   - **B. Créer un nouveau jeu à partir d'un chapitre du cours** (§ 3) ;
   - **C. Produire ou ajouter des images et des vidéos** (§ 4) ;
   - **D. Autre** : correction, leçons A4, intégration, pages de contrôle (§ 5-6).
5. **Choix des chapitres (cases à cocher)** : si l'utilisateur n'a pas donné les numéros ou les noms, AskUserQuestion en `multiSelect: true` (4 jeux par question ; libellé « C02 · titre du chapitre (CAP 1) », d'après `PLAN-PRODUCTION.md`). L'option « Autre » permet de taper un chapitre.
6. **Un seul jeu par conversation**. Pour les autres, dire à la fin d'ouvrir une nouvelle conversation et de relancer ce skill avec les chapitres restants.
7. Si un fichier `RECAP-<slug>.md` existe à la racine pour ce jeu, reprendre là où il s'arrête.

## 1. Règles de contenu (tous les modes)

**Le cours de l'enseignant fait foi** : fichier `.docx` ou `.pdf` du chapitre (ex. « Les pâtes céramiques », CAP 1), à demander s'il n'est pas fourni. Le contenu du chapitre doit être couvert intégralement ; titres et scénarios sont des propositions améliorables.

- **Public** : élèves de CAP (adolescents et jeunes adultes). Ton professionnel d'atelier, tutoiement, aucun ton enfantin, pas d'emoji dans les contenus élèves. Pas de vocabulaire de l'école primaire (CM1, cycle 3, BO) : les libellés visibles sont **Essentiel** et **Expert** ; les clés internes du moteur restent `cm1` (Essentiel) et `cm2` (Expert) (voir `commun/lycee-pro/libelles.js`), de même `niveau=CM1` / `niveau=CM2` dans les adresses.
- 5 salles ; **3 énigmes par salle en Essentiel (15), 4 en Expert (20)** : l'énigme 4 de chaque salle a `"niveaux": ["CM2"]` et un bloc `commun`. Types : qcm, vraifaux, association, ordre, tri, trous, lettres, code, intrus, plan, instrument (le pyromètre du jeu C01 en est un exemple) ; jamais deux types identiques consécutifs dans une salle, au moins une manipulation `ordre`, `plan` ou `tri` par salle et par niveau.
- Chaque énigme : consigne (cm1/cm2), 3 indices par niveau, correction (jamais affichée après réussite ; elle ne doit pas commencer comme le texte de l'énigme), source (le chapitre et la partie), champ `lecon`.
- Un mot-clé par salle ; les mots forment une phrase-bilan (coffre final). Différenciation réelle : repères et valeurs affichés en Essentiel ; sans repères, usages précis, calculs en Expert.
- **Contexte** : entreprise ou atelier **inventé** (comme la « Manufacture des Trois Fours »), personnages **inventés** (apprentis, collègues, responsable ; filles et garçons) ; jamais d'entreprise, de marque, de fournisseur ni de personne réelle, jamais de nom d'élève. Aucune violence gratuite ; les consignes de **sécurité** (poussières, fours, produits) doivent être exactes.
- **Compétences** : rattacher le jeu aux compétences du référentiel du CAP Décoration sur céramique (champ `competences` du catalogue), citées d'après le cours ou le document officiel ; ne jamais inventer un code ou un intitulé.
- **Faits** : d'abord le cours ; compléter ou vérifier sur des sources officielles ou de référence. Ne jamais inventer un chiffre (températures, proportions, durées). Les valeurs qui varient selon les sources ou les fournisseurs vont dans `A-VERIFIER.md`.
- **Dépôt public** : ne jamais y pousser de photo ou de document dont la licence est inconnue (photos tirées du cours comprises : les garder hors du dépôt tant que la licence n'est pas vérifiée) ; jamais de résultats d'élèves (`resultats/`, `resultats-classe.jsonl`, `dossier-donnees.txt`, `difficulte-classe.json` sont ignorés par git : ne pas les forcer).
- **Médias** : ne **jamais** produire d'image ou de vidéo sans l'accord de l'enseignant ; respecter les plafonds de coût ; **ne jamais montrer ni écrire une clé d'API** ; matériaux, outils et lieux réels = vraies photos libres (Wikimedia Commons) ; personnages jamais réels ; **cartes, schémas, courbes jamais générés par IA** (SVG dessinés par script). Le jeu doit toujours fonctionner sans média (décors dessinés, cinématiques en direct).
- Cohérence narrative (jeux immersifs) : lieu, problème, personnage émetteur, lien avec l'histoire, raison du savoir ici, réaction du décor, liberté assumée ; pas de morale plaquée ; relecture sceptique avant livraison.

## 2. Mode A — Migrer un jeu classique au modèle immersif

Le modèle immersif est celui de « Vingt mille lieues sous les mers » (dépôt de l'école) : décor image + effets, objets cliquables, personnage qui parle, cinématiques, grades, journal, coffre. **Non destructif** : la variante est écrite dans `immersifs/<jeu>/`, le jeu classique n'est pas touché. Le migrateur vit dans le dépôt de l'école ; **ne jamais modifier ce dépôt** : travailler dans une copie temporaire.

1. Cloner `IdGir/escape-games-cm1-cm2` dans un dossier temporaire (en lecture) et y copier le jeu classique du lycée (`<jeu>/`) à la racine.
2. Copier `outils/immersif/theme-pates-ceramiques.json` en `outils/immersif/theme-<slug>.json` et l'adapter : titres, mot « salle », palette bleue du CAP (`#0F4C81`, `#2F75B5`, `#DCEEFF`), `style_visuel` (atelier de céramique, lumière naturelle froide, lueur orange du four), noms des grades (`matelot` → Essentiel, `timonier` → Expert).
3. Dans la copie : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py <jeu> --theme <theme.json> --vers <sortie>` ; lire `MIGRATION-RAPPORT.md`. Copier la sortie dans `immersifs/<jeu>/` du dépôt du lycée, puis jeter la copie temporaire.
4. Adapter `outils/immersif/completer-<slug>.py` (copie de `completer-pates-ceramiques.py`) : décors dessinés de secours, zones cliquables nommées, et pour chaque énigme personnage émetteur, problème narratif, enjeu, raison du savoir ici, réaction du décor, réplique par grade. Le lancer : `python outils/immersif/completer-<slug>.py immersifs/<slug>`, puis `python immersifs/<slug>/outils/embarquer-donnees.py`.
5. `node immersifs/<slug>/tests/test-immersif.js` : joue toutes les énigmes de tous les grades (doit être vert avant d'aller plus loin).
6. Médias : mode C (le `medias.csv` de la variante contient déjà les prompts). Zones à recaler avec `immersifs/<slug>/outils/caler-effets.html` après dépôt des décors.
7. Faire évoluer le moteur plus tard sans perdre le travail : `migrer-jeu.py --maj-moteur immersifs/<slug>` (depuis une copie du dépôt de l'école).
8. Garder les deux versions (classique et immersive) : c'est la règle du dépôt.

## 3. Mode B — Créer un nouveau jeu à partir d'un chapitre

Écrire les données au **format des jeux existants** puis migrer (mode A) :

1. Copier `pates-ceramiques/` comme squelette (`index.html`, `prof.html`, `lecons-imprimables.html`, `js/`, `css/`, `tests/`). Copier `outils/generer-pates-ceramiques.py` en `outils/generer-<slug>.py` : toutes les données sont **générées par ce script Python** (jamais à la main dans les JSON) :
   - `assets/data/enigmes.json` (métadonnées + 5 salles ; schémas SVG des énigmes `plan` ou `instrument` produits par des fonctions) ;
   - `dialogues.json` (personnages, introduction, 5 salles avec lieu, description, dialogue d'entrée, dialogue de réussite ou de fin, mot-clé) ;
   - `lecons.json` et `lecons-a4.json` (5 leçons : objectifs, contenu Essentiel/Expert, lexique, document, sources) ;
   - `evaluations.json` (quizz final, QCM, questions fermées, études de documents ; mélanger la place de la bonne réponse).
2. Adapter `js/jeu.js`, `js/app.js` (clés localStorage `escape_<slug>…`), `js/reglages.js`, `js/lecons.js`, `js/decors.js` (5 décors SVG), `js/personnages.js`, la palette CSS (charte bleue du CAP, Calibri pour les documents). Contrôler la syntaxe (`node --check`), puis `python <slug>/tests/test_json.py` et `node <slug>/tests/test-jeu.js`.
3. Documents du jeu : `README.md` (solutions repliées, liens de test), `GUIDE-PEDAGOGIQUE.md` (objectifs du chapitre, salles, déroulé), `A-VERIFIER.md`, `CHANGELOG.md`, `assets/medias/CREDITS-medias.md`.
4. Photos libres (planche d'un document) : `python scripts/images.py commons "mot-clé" -n 5` ; afficher les résultats, **vérifier la licence**, puis `outils/photos/deposer-photos.py` (crédits automatiques).
5. **Version immersive** : mode A sur le nouveau jeu, puis mode C pour les médias.

## 4. Mode C — Produire ou ajouter des images et des vidéos

Détails : outils de `immersifs/<jeu>/outils/medias/` (`produire.py`, `importer-image.py`, `sources-medias.json`) et guides du dépôt de l'école (`vingt-mille-lieues/GUIDE-MEDIAS.md`, `claude/medias-agnes-pipeline.md`). **Canal par défaut : Agnes** (API, quotas documentés), complété par Wikimedia Commons (photos réelles) et par le zoom ffmpeg (gratuit). Flow et Vids n'ont pas d'API : repli manuel.

### 4.1 Règles

1. **Accord et plafonds** : demander à l'enseignant ce qu'il autorise (quels médias, quel canal, quel budget). Ne jamais lancer une génération sans accord. Plafond Agnes : celui du compte de l'enseignant (quota à relever dans la console Agnes ; ne pas supposer un tarif non confirmé). Avec `produire.py`, plafonds par défaut 4 images et 0 vidéo (`--max-images`, `--max-videos`), toujours commencer par `--essai`.
2. **Clé d'API** : seulement dans `cle-agnes.txt` (ou `cles-api.local`, ou variable d'environnement) ; ces fichiers sont dans `.gitignore`. **Ne jamais l'afficher, l'écrire dans un fichier commité, un journal, un message ou un commit.** Si elle manque, le dire et s'arrêter.
3. **Réseau** : Agnes et Commons sont injoignables depuis le cloud et la VM de Claude. La génération se lance sur le PC de l'enseignant (invite de commandes ou double-clic), jamais depuis la session ; le dire plutôt que de simuler.
4. **Contenu** : atelier, matières, outils, fours et lieux réels = photos Wikimedia Commons (crédits automatiques) ; reconstitutions ou ambiances = image IA créditée « généré par IA » ; schémas, courbes, cartes jamais par IA ; aucune personne réelle, aucun logo, aucune marque lisible. Style visuel : celui du thème (`style_visuel`, `negatif`).

### 4.2 Chaîne par défaut (un jeu à la fois)

1. **Manifeste** : `immersifs/<jeu>/medias.csv` (une entrée par média : décor, portrait, transition, introduction, fin ; recherche Commons ou prompt, canal).
2. **Photos Commons et images IA** : `python immersifs/<jeu>/outils/medias/produire.py --essai`, puis sans `--essai` après accord ; reprise automatique (fichiers présents sautés), pauses sur refus, arrêt après 2 refus définitifs.
3. **Zoom ffmpeg en boucle** (transitions gratuites, sans quota) : zoom jusqu'à +12 % puis retour à l'image de départ (lecture en boucle sans saut, rien d'inventé hors de la photo). Commande validée (200 images, 25 i/s, 8 s, 1344×768) :
   `ffmpeg -y -loop 1 -framerate 25 -i decor.png -vf "scale=5376:-2,zoompan=z='1+0.12*(1-cos(2*PI*on/200))/2':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=200:s=1344x768:fps=25,format=yuv420p" -frames:v 200 -c:v libx264 -crf 20 -movflags +faststart video-transition-eN.mp4`
   Portrait : `s=768x1024` avec `scale=3072:-2`.
4. **Repli** : si le canal refuse 2 fois ou si le quota du jour est atteint, ne pas bloquer : lister le média dans un fichier « reste à faire » et le produire à la main avec Flow ou Vids.
5. **Import** : fichiers nommés `decor-<id>.png`, `portrait-<id>.jpg`, `video-<nom>.mp4` dans `assets/medias-a-importer/`, puis `python immersifs/<jeu>/outils/medias/importer-image.py --dossier --source "<canal>" --licence "<licence>"` (crédits automatiques). Puis `outils/caler-effets.html` pour les zones et `python immersifs/<jeu>/outils/embarquer-donnees.py`.
6. **Contrôle humain** : regarder chaque média (personnages, cadres inventés, texte parasite) ; l'enseignant choisit (`outils/choisir-medias.html`). Mettre à jour `medias.csv` et `CREDITS-medias.md` ; « généré par IA » dans les crédits ; une photo dérivée d'une image Creative Commons garde l'attribution (BY-SA).
7. Ne jamais commiter : clés, `diag.txt`, journaux, `*.avant-*`, `RECAP-*.md`.

## 5. Intégration au dépôt (nouveau jeu, remplacement)

- `commun/donnees/catalogue.js` : une entrée dans `jeux` (num `C0N`, id, titre, matière, classe, compétences, dossier, immersif, icône, couleurs, résumé). Les pages du portail, l'espace enseignant, la vérification, les résultats, le classement, le passeport et les trophées s'en alimentent : rien d'autre à modifier pour elles.
- `serveur.py` : ajouter le dossier dans `JEUX_LYCEE`.
- `PLAN-PRODUCTION.md` (cocher), `README.md` racine (tableau des jeux, arborescence).
- Hors connexion : `python outils-pwa/maj-hors-ligne.py` puis `git add sw-fichiers.js` (version du cache) ; `python outils-pwa/archives-hors-ligne.py <jeu>` pour tester l'archive zip.
- Le portail `index.html` ne change pas.

## 6. Tests et commit

1. Tests jsdom : `npm install jsdom@24` (dossier `outils-tests`, une fois), puis `node outils-tests/tous.js <slug>` et les tests communs (`node commun/tests/test-coherence.js`, `test-pages-lycee.js`, `test-hors-ligne.js`, `test-archives.js`) ; un appel shell dure 180 s au plus : découper. Pour le modèle immersif : `immersifs/<slug>/tests/test-immersif.js`. Contrôles complémentaires : `node outils-tests/verifier-liens-internes.js`, `verifier-enigmes.js`.
2. `git branch --show-current` = `main` (ou la branche de la session). `git add` **par chemins nommés** (jamais `-A` hors du dossier du jeu), **puis** `python outils-pwa/maj-hors-ligne.py` et `git add sw-fichiers.js`, relancer `test-hors-ligne`.
3. Si `.git/index.lock` reste bloqué : demander l'autorisation de suppression du dossier.
4. Un commit en français, message détaillé, terminé par les lignes d'attribution demandées par la session.
5. Cocher le chapitre dans `PLAN-PRODUCTION.md` ; mettre à jour le `README.md` racine.

## 7. Fin de session

- Si le contexte approche 80 % : commit d'un état cohérent, puis `RECAP-<slug>.md` à la racine (ignoré par git) : avancement, décisions, fichiers, reste à faire, pièges, phrase pour reprendre, **rédigé pour qu'une autre IA puisse reprendre le travail**.
- Réponse finale courte : ce qui est fait, résultats des tests, points à relire (`A-VERIFIER.md`), chapitres restants à lancer dans une nouvelle conversation, puis la publication pas à pas. Outil : Invite de commandes Windows (touches Windows + R, taper `cmd`, Entrée) ; `cd "<dossier du dépôt>"` ; `git status` ; `git push origin main` ; une minute plus tard, ouvrir https://mamagir.github.io/escape-games-lycee-pro/ (Ctrl + F5).
- Si le push est refusé (erreur 403) : le PC est connecté au compte `IdGir` ; ce compte doit être **collaborateur** du dépôt (GitHub, compte MamaGir → dépôt → Settings → Collaborators → Add people → `IdGir`, puis accepter l'invitation reçue par `IdGir`).
