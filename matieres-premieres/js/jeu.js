/* ============================================================
   JEU — ce qui est propre à « Le bon de lancement »
   (La préparation des matières premières · CAP Décoration sur céramique)
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/) ne contiennent aucun
   texte propre à un jeu : ils lisent cet objet.
   Niveaux : clés internes « CM1 » / « CM2 » (format du moteur),
   affichées « Essentiel » / « Expert » (../commun/lycee-pro/libelles.js).
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "matieres-premieres",
  titre: "Le bon de lancement",
  motSalle: "Salle",

  voix: {
      maelle:  {rate:1.02, pitch:1.15},  // apprentie, voix vive
      odile:   {rate:1.00, pitch:1.05},  // cheffe de carrière
      malik:   {rate:0.98, pitch:0.95},  // responsable du parc et des silos
      karim:   {rate:1.02, pitch:0.90},  // technicien du broyage
      jade:    {rate:1.00, pitch:1.10},  // technicienne d'épuration
      aubry:   {rate:0.92, pitch:0.95}   // cheffe du laboratoire, voix posée
    },
  voixFeminines: ["maelle", "odile", "jade", "aubry"],

  /* Ambiance sonore de chaque décor (audio.js) */
  ambiances: {
    "carriere": ["Vent"],
    "parc": ["Pluie"],
    "broyage": ["Imprimerie"],
    "epuration": ["Imprimerie"],
    "dures": ["Accueil"],
    "accueil": ["Accueil"]
  },

  ia: {
    personnages: {
      maelle: "Tu es Maëlle (personnage inventé), apprentie en 2e année de CAP Décoration sur céramique dans une manufacture. Tu tutoies les joueurs, tu les encourages et tu renvoies au cours « La préparation des matières premières ». Réponses de 2 à 4 phrases.",
      odile: "Tu es Odile (personnage inventé), cheffe d'une carrière d'argile. Tu expliques pourquoi on prépare les matières premières, comment on analyse un terrain (grille, un échantillon par carré) et comment on extrait l'argile. Réponses de 2 à 4 phrases.",
      malik: "Tu es Malik (personnage inventé), responsable du parc d'argile et des silos. Tu expliques le pourrissement (dehors, 3 à 24 mois) et la maturation (silo humide et sombre, au moins 2 semaines, humidité de 18-22 % à 13-18 %). Réponses de 2 à 4 phrases.",
      karim: "Tu es Karim (personnage inventé), technicien d'un atelier de broyage. Tu expliques les machines à broyer l'argile : meule, brise-mottes, désagrégateur, marteaux, billes. Réponses de 2 à 4 phrases.",
      jade: "Tu es Jade (personnage inventé), technicienne d'une station d'épuration. Tu expliques le tamis vibrant, le déferrage, la flottation et les règles de sécurité face aux poussières (masque, aspiration ou humide, jamais de balayage à sec). Réponses de 2 à 4 phrases.",
      aubry: "Tu es Madame Aubry (personnage inventé), cheffe d'un laboratoire des matières dures. Tu expliques comment on obtient le feldspath, le sable de silice et la chamotte, et la différence entre concasseurs à mâchoires et à percussion. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "maelle",
    presentation: false,
    contexte: "Escape game de technologie céramique : la préparation des matières premières des pâtes céramiques (CAP Décoration sur céramique)",
    regles: [
      "N'invente aucune durée, aucun pourcentage ni aucune température : reprends ceux du cours.",
      "Rappelle les règles de sécurité dès qu'il est question de poussières."
    ],
    systeme: "Tu es un assistant pédagogique en technologie céramique, destiné à des élèves de lycée professionnel (CAP) en France. Tu restes factuel, bienveillant et clair."
  },

  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  impression: {
    mentions: ["🏆 Cheffe ou chef de fabrication", "🥈 Compagnon de l'atelier", "🥉 Apprentie ou apprenti confirmé", "📜 Nouvelle recrue"],
    sousTitre: "Escape game de technologie céramique · La préparation des matières premières · CAP Décoration sur céramique",
    libelleMotsCles: "📜 Tampons du bon de lancement",
    logo: "🏺",
    pied: "Le bon de lancement · La préparation des matières premières · CAP",
    motSalle: "Salle",
    contexte: "📜 Contexte",
    titreQcm: "La préparation des matières premières",
    theme: "la préparation des matières premières"
  }
};
