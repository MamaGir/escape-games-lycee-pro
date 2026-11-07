/* ============================================================
   CATALOGUE DES JEUX — LYCÉE PROFESSIONNEL (CAP Décoration sur céramique)
   ------------------------------------------------------------
   Remplace, dans ce dépôt, le catalogue des escape games de l'école :
   seuls les jeux du lycée y figurent. Utilisé par le portail (index.html)
   et les liens « jeu suivant ». Ajouter un jeu : une entrée dans « jeux ».
   « immersif » : adresse de la variante immersive ; « dossier » : version classique.
   Fichier .js (et non .json) pour fonctionner aussi en double-clic.
   ============================================================ */
var CATALOGUE = {
 "genere": "2026-11-07",
 "source": "README.md du dépôt escape-games-lycee-pro",
 "public": "CAP Décoration sur céramique",
 "niveaux": { "CM1": "Essentiel", "CM2": "Expert" },
 "periodes": {},
 "jeux": [
  {
   "num": "C01",
   "id": "pates-ceramiques",
   "titre": "Les fiches du four",
   "matiere": "Technologie céramique",
   "classe": "CAP 1",
   "periodes": [],
   "competences": "Les pâtes céramiques : matières premières, minéraux argileux, argiles primaires et secondaires, principales argiles, dégraissants, sécurité, familles de pâtes, cuisson, recettes.",
   "dossier": "pates-ceramiques",
   "immersif": "immersifs/pates-ceramiques",
   "icone": "🏺",
   "couleurs": ["#0F4C81", "#C2410C"],
   "resume": "À la manufacture des Trois Fours, les cinq fiches du cahier de fabrication sont restées chez cinq collègues : l'équipe doit les récupérer avant la cuisson du soir.",
   "programme": []
  }
 ]
};

/* Adresses d'un jeu : la variante immersive par défaut, la version classique en option */
var CATALOGUE_JEU = {
  adresse: function(j){ return j && (j.immersif || j.dossier) || ""; },
  classique: function(j){ return j && j.dossier || ""; },
  aImmersif: function(j){ return !!(j && j.immersif); }
};
