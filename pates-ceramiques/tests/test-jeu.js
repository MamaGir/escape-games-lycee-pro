/* Tests automatiques — Les fiches du four (Node + jsdom)
   Depuis la racine du dépôt :  node pates-ceramiques/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node pates-ceramiques/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "Les fiches du four",
  scoresMax: { CM1: 185, CM2: 235 },
});
