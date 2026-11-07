/* Tests automatiques — Le bon de lancement (Node + jsdom)
   Depuis la racine du dépôt :  node matieres-premieres/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node matieres-premieres/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "Le bon de lancement",
  scoresMax: { CM1: 185, CM2: 235 },
});
