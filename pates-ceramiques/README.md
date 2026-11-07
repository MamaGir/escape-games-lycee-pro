# Les fiches du four

**Escape game de technologie céramique — CAP Décoration sur céramique, 1re année — Les pâtes céramiques**  
45 à 60 minutes · équipes de 3-4 élèves · **15 énigmes au niveau Essentiel, 20 au niveau Expert**.

> *Manufacture des Trois Fours (inventée), lundi matin.* Le grand four doit cuire ce soir la vaisselle d'un restaurant. Le cahier de
> fabrication a été démonté pour être recopié : ses cinq fiches sont restées chez cinq collègues. Maëlle, apprentie de 2e année,
> guide l'équipe du magasin au four. Chaque collègue rend sa fiche si l'équipe maîtrise la matière ; les cinq mots ouvrent le coffre.

Contenu : le chapitre « Les pâtes céramiques » (CAP 1) de l'enseignant, couvert intégralement.

| | |
|---|---|
| ▶ **Jouer** | version classique : `pates-ceramiques/` · version immersive : `immersifs/pates-ceramiques/` · en local avec `lancer.bat` |
| 📖 **Leçons A4** | `lecons-imprimables.html` (Essentiel ou Expert) |
| 👨‍🏫 **Tableau de bord** | http://127.0.0.1:8000/pates-ceramiques/prof.html — mode local |
| 📖 **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) |
| ⚠️ **Points à contrôler** | [A-VERIFIER.md](A-VERIFIER.md) |

---

## Les 5 salles

| # | Lieu | Notion | Personnage | Mot-clé | Énigmes | Tester |
|---|---|---|---|---|---|---|
| 1 | Le magasin des matières | Matières premières et vocabulaire | Inès | **ARGILE** | 3 Essentiel · 4 Expert | [Essentiel](pates-ceramiques/?salle=1&niveau=CM1) · [Expert](pates-ceramiques/?salle=1&niveau=CM2) |
| 2 | Le laboratoire | Minéraux argileux, argiles primaires et secondaires | Théo | **PLASTICITÉ** | 3 Essentiel · 4 Expert | [Essentiel](pates-ceramiques/?salle=2&niveau=CM1) · [Expert](pates-ceramiques/?salle=2&niveau=CM2) |
| 3 | La réserve des argiles | Les principales argiles et leurs usages | Awa | **KAOLIN** | 3 Essentiel · 4 Expert | [Essentiel](pates-ceramiques/?salle=3&niveau=CM1) · [Expert](pates-ceramiques/?salle=3&niveau=CM2) |
| 4 | La salle de préparation | Dégraissants et sécurité | Lucas | **DÉGRAISSANT** | 3 Essentiel · 4 Expert | [Essentiel](pates-ceramiques/?salle=4&niveau=CM1) · [Expert](pates-ceramiques/?salle=4&niveau=CM2) |
| 5 | Le four | Familles de pâtes, cuisson, recettes | Madame Ferrand | **CUISSON** | 3 Essentiel · 4 Expert | [Essentiel](pates-ceramiques/?salle=5&niveau=CM1) · [Expert](pates-ceramiques/?salle=5&niveau=CM2) |
| 🏁 | Fin : coffre, cahier complet, quizz | | Maëlle | | 5 questions | [Essentiel](pates-ceramiques/?salle=6&niveau=CM1) · [Expert](pates-ceramiques/?salle=6&niveau=CM2) |

Phrase-bilan du coffre : **« L'ARGILE doit sa PLASTICITÉ à ses minéraux ; le KAOLIN donne la porcelaine ; le DÉGRAISSANT rend la pâte moins collante ; la CUISSON la rend dure et étanche. »**

Dans les adresses, `niveau=CM1` correspond au niveau Essentiel et `niveau=CM2` au niveau Expert (clés internes du moteur).

---

## Énigmes et solutions

<details>
<summary>⚠️ Solutions — à ne pas projeter en classe</summary>

### Salle 1 — Le magasin des matières — Les matières premières des pâtes

#### 1-1 · Les étiquettes du magasin — type `association` — Essentiel et Expert

**Essentiel**

- Plastique → **Se modèle facilement sans se casser**
- Pâte grasse → **Pâte très plastique et collante**
- Dégraissant → **Matière ajoutée pour rendre la pâte moins collante**
- Chamotte → **Argile déjà cuite, puis broyée**

**Expert**

- Plastique → **Se modèle facilement sans se casser**
- Pâte grasse → **Pâte très plastique et collante**
- Dégraissant → **Matière ajoutée pour rendre la pâte moins collante**
- Chamotte → **Argile déjà cuite, puis broyée**
- Émail → **Poudre de verre délayée dans l'eau, brillante après cuisson**
- Vitrifié → **Devenu dur et étanche, comme du verre**

*Correction :* Une pâte plastique se modèle sans casser ; trop plastique et collante, elle est « grasse ». Le dégraissant la rend moins collante ; la chamotte en est un exemple (argile cuite puis broyée). L'émail est une poudre de verre délayée dans l'eau ; ce qui est vitrifié est devenu dur et étanche comme du verre.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, encadré « Mots à connaître » · *Leçon :* `pate-composition`

#### 1-2 · Les deux rayons — type `tri` — Essentiel et Expert

**Essentiel**

- **Matières plastiques** : Kaolin ; Ball clay ; Terre à grès
- **Matières non plastiques** : Sable ; Chamotte ; Paille

**Expert**

- **Matières plastiques** : Kaolin ; Ball clay ; Terre à feu ; Bentonite ; Argile commune
- **Matières non plastiques** : Chamotte ; Quartz ; Sciure de bois ; Feldspath ; Sable

*Correction :* Les matières plastiques sont les argiles : elles permettent de modeler la pièce. Les matières non plastiques sont les dégraissants (chamotte, sable, quartz, paille, sciure, feldspath) : on les ajoute pour que la pâte colle moins.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I · *Leçon :* `pate-composition`

#### 1-3 · Le carnet d'Inès — type `vraifaux` — Essentiel et Expert

**Essentiel**

- Dans une pâte, les quantités de chaque matière sont pesées avec précision. → **Vrai**
- Si la pâte est trop collante, on ajoute de l'argile. → **Faux**
- La plasticité, c'est la capacité de l'argile à être modelée sans se casser. → **Vrai**
- Le sable est une matière plastique. → **Faux**

**Expert**

- Une pâte céramique contient des matières plastiques et des matières non plastiques. → **Vrai**
- Une pâte grasse est une pâte très peu plastique. → **Faux**
- Une argile est faite d'un seul minéral argileux. → **Faux**
- Une pièce vitrifiée est dure et étanche. → **Vrai**
- La couleur d'une argile dépend de l'endroit où on l'extrait. → **Vrai**

*Correction :* Dans une pâte, les quantités sont pesées avec précision. Une pâte trop collante (grasse) reçoit un dégraissant, pas davantage d'argile. La plasticité est la capacité à être modelée sans casser.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I · *Leçon :* `pate-composition`

#### 1-4 · La fiche de fabrication — type `trous` — Expert

Mots attendus, dans l'ordre : **argile**, **pesées**, **plasticité**, **collante**, **dégraissant**
Étiquettes en trop : émail, vitrifiée

*Correction :* Une pâte céramique mélange de l'argile et d'autres matières pesées avec précision. L'argile apporte la plasticité ; le dégraissant (chamotte, sable…) rend la pâte moins collante.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I · *Leçon :* `pate-composition`

### Salle 2 — Le laboratoire — Minéraux argileux, argile primaire et secondaire

#### 2-1 · Sous le microscope — type `ordre` — Essentiel et Expert

**Essentiel**

1. Kaolinite (le minéral du kaolin)
2. Illite (plasticité moyenne)
3. Smectite (exemple : la montmorillonite)

**Expert**

1. Kaolinite
2. Illite
3. Smectite (montmorillonite)

*Correction :* La kaolinite a une plasticité faible, l'illite une plasticité moyenne, la smectite (par exemple la montmorillonite) une plasticité haute.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.1 · *Leçon :* `mineraux-argiles`

#### 2-2 · Les questions de Théo — type `qcm` — Essentiel et Expert

**Essentiel**

- Les minéraux argileux sont… → **des particules microscopiques**
- Combien y a-t-il de minéraux argileux principaux ? → **3**
- Une argile est… → **une matière naturelle**

**Expert**

- Une argile contient… → **plusieurs minéraux argileux et d'autres matières (sable, quartz, restes de plantes)**
- Pourquoi deux argiles n'ont-elles pas la même couleur ? → **Elles viennent d'endroits différents**
- Que désigne la plasticité ? → **La capacité à être modelée sans casser**

*Correction :* Les minéraux argileux sont des particules microscopiques. Une argile est une matière naturelle qui mélange plusieurs minéraux argileux et d'autres matières ; sa couleur et ses propriétés dépendent du lieu d'extraction.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.1 · *Leçon :* `mineraux-argiles`

#### 2-3 · Restée sur place ou voyageuse ? — type `tri` — Essentiel et Expert

**Essentiel**

- **Argile primaire** : Restée sur place, là où la roche s'est transformée ; Le kaolin
- **Argile secondaire** : Transportée par l'eau ou le vent ; La ball clay ; Les argiles communes (terre rouge)

**Expert**

- **Argile primaire** : Restée sur place, là où la roche s'est transformée ; Le kaolin ; Moins plastique que l'autre type
- **Argile secondaire** : Transportée loin de son origine ; Mélangée à d'autres matières pendant le voyage ; La terre à feu ; La terre à grès ; La ball clay

*Correction :* Une argile primaire est restée sur place, là où la roche s'est transformée : c'est le cas du kaolin. Une argile secondaire a été transportée par l'eau ou le vent, s'est mélangée à d'autres matières et est plus plastique : ball clay, terre à feu, terre à grès, argiles communes.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, encadré « Argile primaire ou argile secondaire ? » · *Leçon :* `mineraux-argiles`

#### 2-4 · L'échantillon mal rangé — type `intrus` — Expert

Intrus : **Kaolin**

*Correction :* Le kaolin est une argile primaire : il est resté sur place. Ball clay, terre à feu, terre à grès et argiles communes ont été transportées : ce sont des argiles secondaires.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.1 · *Leçon :* `mineraux-argiles`

### Salle 3 — La réserve des argiles — Les principales argiles et leurs usages

#### 3-1 · Les sacs sans étiquette — type `association` — Essentiel et Expert

**Essentiel**

- Kaolin → **Blanche**
- Ball clay → **Blanc crème à gris clair**
- Terre à feu → **Beige à brun clair**
- Argiles communes → **Rouge**

**Expert**

- Kaolin → **Blanche, argile primaire**
- Ball clay → **Très plastique, blanc crème à gris clair**
- Terre à feu → **Résiste à environ 1500 °C**
- Terre à grès → **Résiste au gel**
- Argiles communes → **Riches en fer, rouges**
- Bentonite → **Extrêmement plastique**

*Correction :* Kaolin : blanc. Ball clay : blanc crème à gris clair, très plastique. Terre à feu : beige à brun clair, résiste à environ 1500 °C. Terre à grès : beige à brun, résiste au gel. Argiles communes : rouges, riches en fer. Bentonite : extrêmement plastique.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.1, « Les principales argiles » · *Leçon :* `principales-argiles`

#### 3-2 · Le rayonnage de la réserve — type `plan` — Essentiel et Expert

**Essentiel**

- Étagère 1 : porcelaine et vaisselle fine → **Kaolin**
- Étagère 2 : briques de four et creusets → **Terre à feu**
- Étagère 3 : briques et tuiles → **Argiles communes**
- Étagère 4 : vaisselle, poteries de jardin, carreaux → **Terre à grès**

**Expert**

- Étagère 1 : porcelaine et vaisselle fine (argile primaire) → **Kaolin**
- Étagère 2 : plaques et supports d'enfournement → **Terre à feu**
- Étagère 3 : tuiles, riche en fer → **Argiles communes**
- Étagère 4 : carreaux qui résistent au gel → **Terre à grès**
- Étagère 5 : un peu dans l'émail, pour que la poudre ne tombe pas au fond du seau → **Bentonite**
- Étagère 6 : pâtes fines et faïence, très plastique → **Ball clay**

*Correction :* Porcelaine et vaisselle fine : kaolin. Briques de four, supports d'enfournement, creusets : terre à feu. Briques et tuiles : argiles communes. Vaisselle, poteries de jardin et carreaux qui résistent au gel : terre à grès. Un peu dans une pâte ou dans un émail : bentonite. Pâtes fines, porcelaine, faïence : ball clay.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.1, « Les principales argiles » · *Leçon :* `principales-argiles`

#### 3-3 · Le bon choix — type `qcm` — Essentiel et Expert

**Essentiel**

- Pour rendre une pâte plus plastique, on ajoute un peu de… → **bentonite**
- Une argile rouge foncé contient beaucoup de… → **fer**
- Pour la porcelaine, on choisit… → **le kaolin**

**Expert**

- Pourquoi met-on un peu de bentonite dans un émail ? → **Pour que la poudre ne tombe pas au fond du seau**
- Le kaolin est fait surtout de… → **kaolinite, de plasticité faible**
- La terre à grès convient aux poteries de jardin car… → **devenue dure et étanche, elle résiste au gel**

*Correction :* Pour une pâte plus plastique, on ajoute un peu de bentonite. Une argile commune rouge foncé contient beaucoup de fer. Le kaolin est fait surtout de kaolinite, peu plastique.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.1 · *Leçon :* `principales-argiles`

#### 3-4 · Le cadenas de la réserve — type `code` — Expert

- Température (°C) que supporte la terre à feu → **1500**
- Nombre de minéraux argileux principaux → **3**

*Correction :* La terre à feu résiste à environ 1500 °C sans fondre ni se déformer. Il y a 3 minéraux argileux principaux : kaolinite, illite, smectite.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.1 · *Leçon :* `principales-argiles`

### Salle 4 — La salle de préparation — Les dégraissants et la sécurité

#### 4-1 · Les quatre bacs — type `tri` — Essentiel et Expert

**Essentiel**

- **Simples** : Chamotte
- **Siliceux** : Sable ; Quartz
- **Combustibles** : Paille ; Sciure de bois
- **Fondants** : Feldspath

**Expert**

- **Simples** : Chamotte ; Tessons broyés
- **Siliceux** : Sable ; Quartz en poudre ; Galets de mer broyés
- **Combustibles** : Paille ; Papier ; Sciure de bois
- **Fondants** : Feldspath

*Correction :* Dégraissants simples : chamotte, tessons broyés. Siliceux : sable, quartz, galets de mer broyés. Combustibles : paille, papier, sciure de bois. Fondants : feldspath.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.2 · *Leçon :* `degraissants-securite`

#### 4-2 · Les effets du dégraissant — type `vraifaux` — Essentiel et Expert

**Essentiel**

- Un dégraissant rend la pâte moins collante. → **Vrai**
- Avec un dégraissant, la pâte se fissure davantage. → **Faux**
- Avec un dégraissant, la pâte sèche mieux. → **Vrai**
- Un dégraissant rend la pâte plus plastique. → **Faux**

**Expert**

- Un dégraissant réduit la plasticité de l'argile. → **Vrai**
- Une pâte dégraissée se déforme moins à la cuisson. → **Vrai**
- Les dégraissants combustibles rendent la pièce plus lourde. → **Faux**
- Les dégraissants fondants rendent la pièce dure et vitrifiée. → **Vrai**
- Les dégraissants siliceux fragilisent la pièce cuite. → **Faux**

*Correction :* Un dégraissant réduit la plasticité : la pâte est moins collante, sèche mieux, se fissure et se déforme moins. Les combustibles laissent de petits trous qui allègent la pièce ; les fondants la rendent dure et vitrifiée.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.2 · *Leçon :* `degraissants-securite`

#### 4-3 · L'armoire des fondants — type `intrus` — Essentiel et Expert

**Essentiel**

Intrus : **Goûter la poudre**

**Expert**

Intrus : **Prendre son goûter à son poste**

*Correction :* Le plomb est toxique : on manipule les matières fondantes avec des gants, un masque, et on se lave les mains. Manger ou boire à son poste de travail est dangereux.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, encadré « Sécurité » · *Leçon :* `degraissants-securite`

#### 4-4 · Un rôle pour chaque bac — type `association` — Expert

- Simple (chamotte) → **Rend la pâte moins collante, tout en la gardant solide**
- Siliceux (sable, quartz) → **Résiste à la chaleur et renforce la pièce cuite**
- Combustible (paille, sciure) → **Brûle et laisse de petits trous : la pièce est plus légère**
- Fondant (feldspath) → **Aide la pâte à fondre : la pièce devient dure et vitrifiée**

*Correction :* Simple : moins collante tout en restant solide. Siliceux : résiste à la chaleur et renforce la pièce cuite. Combustible : brûle et laisse de petits trous, la pièce est plus légère. Fondant : aide la pâte à fondre, la pièce devient dure et vitrifiée.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie I.2 · *Leçon :* `degraissants-securite`

### Salle 5 — Le four — Familles de pâtes, cuisson et recettes

#### 5-1 · La montée en température — type `ordre` — Essentiel et Expert

**Essentiel**

1. Terre cuite (briques, tuiles)
2. Faïence (vaisselle émaillée)
3. Grès (dur et étanche)
4. Porcelaine dure (blanche, translucide)

**Expert**

1. Terre cuite
2. Faïence
3. Grès
4. Porcelaine dure

*Correction :* Terre cuite : 1000 °C. Faïence : 1050 °C. Grès : 1280 °C. Porcelaine dure : jusqu'à 1400 °C. Plus la cuisson est chaude, plus la pâte est dure et étanche.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie II · *Leçon :* `familles-recettes`

#### 5-2 · Le pyromètre du four — type `instrument` — Essentiel et Expert

**Essentiel**

- Cuisson de la terre cuite (lire) → **1000 °C**
- Cuisson de la faïence (lire) → **1050 °C**
- Cuisson du grès (lire) → **1280 °C**

**Expert**

- Pendant une cuisson de faïence (lire) → **1050 °C**
- Grès (régler) → **1280 °C**
- Raku (régler) → **1000 °C**

*Correction :* Le pyromètre mesure la température du four. Faïence : 1050 °C. Grès : 1280 °C. Terre cuite et raku : 1000 °C.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie II · *Leçon :* `familles-recettes`

#### 5-3 · Qui suis-je ? — type `qcm` — Essentiel et Expert

**Essentiel**

- Plus la cuisson est chaude, plus la pâte devient… → **dure et étanche**
- « J'ai beaucoup de chamotte et je supporte les chocs de chaleur. » → **le raku**
- « Je suis blanche et translucide quand je suis fine. » → **la porcelaine**

**Expert**

- « Je suis blanche, vitrifiée, toujours émaillée, mais non translucide. » → **le vitreous**
- « Je suis rouge, riche en fer, souvent sans émail. » → **la terre cuite**
- « Ma pâte est faite d'argile commune ou blanche, toujours recouverte d'émail, cuite vers 1050 °C. » → **la faïence**

*Correction :* Plus la cuisson est chaude, plus la pâte devient dure et étanche. Le raku contient beaucoup de chamotte et supporte les chocs de chaleur. La porcelaine est blanche et translucide quand elle est fine ; le vitreous est blanc, vitrifié, émaillé mais non translucide.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie II · *Leçon :* `familles-recettes`

#### 5-4 · Le cahier de recettes — type `code` — Expert

- Porcelaine : part de silice (%) → **25**
- Raku : part de chamotte (%) → **20**
- Masse de terre à feu (kg) pour 20 kg de pâte à grès (50 %) → **10**

*Correction :* Porcelaine : kaolin 25 + ball clay 25 + feldspath 25 + silice 25 = 100 %. Raku : terre à feu 55 + ball clay 25 + chamotte 20 = 100 %. Pour 20 kg de grès : 50 % de terre à feu, soit 10 kg.  
*Source :* Chapitre « Les pâtes céramiques », CAP 1, partie III · *Leçon :* `familles-recettes`

</details>

---

## Types d'énigmes utilisés

| Type | Énigmes |
|---|---|
| `qcm` | 2-2, 3-3, 5-3 |
| `vraifaux` | 1-3, 4-2 |
| `association` | 1-1, 3-1, 4-4* |
| `ordre` | 2-1, 5-1 |
| `tri` | 1-2, 2-3, 4-1 |
| `trous` | 1-4* |
| `code` | 3-4*, 5-4* |
| `intrus` | 2-4*, 4-3 |
| `plan` | 3-2 |
| `instrument` | 5-2 |

\* énigme réservée au niveau Expert.

---

## Régénérer les données et la documentation

1. Modifier le contenu dans `outils/generer-pates-ceramiques.py` (à la racine du dépôt), jamais dans les JSON.
2. `python outils/generer-pates-ceramiques.py`
3. `python pates-ceramiques/tests/test_json.py` puis `node pates-ceramiques/tests/test-jeu.js` (jsdom requis).
4. `python pates-ceramiques/tests/generer-readme.py` (ce fichier).

## Médias

Aucun média n'est nécessaire : décors et personnages sont dessinés (`js/decors.js`, `js/personnages.js`).
Planche photo facultative de la leçon 3 : `outils/photos/deposer-photos.py` (photos libres ou photos du cours, voir A-VERIFIER.md).

