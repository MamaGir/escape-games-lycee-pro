/* ============================================================
   JEU — ce qui est propre à « Les fiches du four »
   (Les pâtes céramiques · CAP Décoration sur céramique)
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/) ne contiennent aucun
   texte propre à un jeu : ils lisent cet objet.
   Niveaux : clés internes « CM1 » / « CM2 » (format du moteur),
   affichées « Essentiel » / « Expert » (../commun/lycee-pro/libelles.js).
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "pates-ceramiques",
  titre: "Les fiches du four",
  motSalle: "Salle",

  voix: {
      maelle:  {rate:1.02, pitch:1.15},  // apprentie, voix vive
      ines:    {rate:1.00, pitch:1.10},  // magasinière
      theo:    {rate:0.98, pitch:0.95},  // technicien de laboratoire
      awa:     {rate:0.98, pitch:1.05},  // responsable de la réserve
      lucas:   {rate:1.02, pitch:0.90},  // préparateur
      ferrand: {rate:0.92, pitch:0.95}   // cheffe du four, voix posée
    },
  voixFeminines: ["maelle", "ines", "awa", "ferrand"],

  /* Ambiance sonore de chaque décor (audio.js) */
  ambiances: {
    "magasin": ["Imprimerie"],
    "laboratoire": ["Accueil"],
    "reserve": ["Pluie"],
    "preparation": ["Imprimerie"],
    "four": ["Vent"],
    "accueil": ["Accueil"]
  },

  ia: {
    personnages: {
      maelle: "Tu es Maëlle (personnage inventé), apprentie en 2e année de CAP Décoration sur céramique dans une manufacture de faïence. Tu tutoies les joueurs, tu les encourages et tu renvoies au chapitre « Les pâtes céramiques ». Réponses de 2 à 4 phrases.",
      ines: "Tu es Inès (personnage inventé), magasinière d'une manufacture. Tu expliques de quoi est faite une pâte céramique : argile et dégraissants pesés avec précision. Réponses de 2 à 4 phrases.",
      theo: "Tu es Théo (personnage inventé), technicien de laboratoire. Tu expliques les minéraux argileux (kaolinite, illite, smectite) et la différence entre argile primaire et secondaire. Réponses de 2 à 4 phrases.",
      awa: "Tu es Awa (personnage inventé), responsable d'une réserve d'argiles. Tu décris le kaolin, la ball clay, la terre à feu, la terre à grès, les argiles communes et la bentonite. Réponses de 2 à 4 phrases.",
      lucas: "Tu es Lucas (personnage inventé), préparateur de pâtes. Tu expliques les quatre types de dégraissants et les règles de sécurité avec les fondants (plomb toxique : gants, masque, lavage des mains). Réponses de 2 à 4 phrases.",
      ferrand: "Tu es Madame Ferrand (personnage inventé), cheffe du four. Tu expliques les familles de pâtes, leurs températures de cuisson et les recettes en pourcentages. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "maelle",
    presentation: false,
    contexte: "Escape game de technologie céramique : les pâtes céramiques (CAP Décoration sur céramique, 1re année)",
    regles: [
      "N'invente aucune température, aucune recette ni aucun pourcentage : reprends ceux du chapitre.",
      "Rappelle les règles de sécurité dès qu'il est question de matières fondantes."
    ],
    systeme: "Tu es un assistant pédagogique en technologie céramique, destiné à des élèves de lycée professionnel (CAP) en France. Tu restes factuel, bienveillant et clair."
  },

  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  impression: {
    mentions: ["🏆 Cheffe ou chef de fabrication", "🥈 Compagnon de l'atelier", "🥉 Apprentie ou apprenti confirmé", "📜 Nouvelle recrue"],
    sousTitre: "Escape game de technologie céramique · Les pâtes céramiques · CAP Décoration sur céramique",
    libelleMotsCles: "📜 Fiches du cahier",
    logo: "🏺",
    pied: "Les fiches du four · Les pâtes céramiques · CAP",
    motSalle: "Salle",
    contexte: "📜 Contexte",
    titreQcm: "Les pâtes céramiques",
    theme: "les pâtes céramiques"
  }
};
