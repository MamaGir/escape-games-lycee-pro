/* ============================================================
   APP — Moteur principal du jeu « Le bon de lancement »
   Coordonne : écrans, salles, décors, dialogues, énigmes,
               pages du carnet, carnet final, score, minuteur,
               leçons, réglages
   ------------------------------------------------------------
   Les énigmes ne sont PAS écrites ici : elles sont décrites dans
   assets/data/enigmes.json et rendues par js/enigmes.js.
   ============================================================ */

const NB_SALLES = 5;

const ETAT = {
  equipe: "",
  niveau: "CM2",
  salle: 1,
  enigme: 0,                 // index de l'énigme en cours dans la salle
  score: 0,
  motsCles: [],              // mots des pages du carnet déjà retrouvées
  enigmesPremierCoup: 0, erreursTotal: 0, coffreOuvert: false, coffrePremierCoup: false,
  badges: {vitesse:false, mecene:false, plans:false, atelier:false},
  debut: null,
  msEcoules: 0,
  enPause: false,
  tempsParSalle: {},
  salleDebut: null,
  indicesSalle: 0,
  indicesTotal: 0,
  enigmesReussies: 0,
  quiz: {repondu:false, score:0},
  fini: false,
  reglages: {
    narrationActive: true,
    volume: 1,
    tailleTexte: 1,
    dureeMin: 60,
    leconsAutorisees: true,
    apiActive: false,
    sonsActifs: true,
    volumeSons: 0.55,
    animationsReduites: false,
    decorsVideo: true,
    sonVideo: false,
    cinematiques: true,
  }
};

const PTS_PREMIER_COUP   = 10;   // énigme juste du premier coup
const PTS_APRES_ERREUR   = 3;    // énigme résolue après une ou plusieurs erreurs
const PTS_COFFRE_PREMIER = 10;   // coffre final ouvert du premier coup
const PTS_COFFRE_APRES   = 3;    // coffre final ouvert après erreur
const PTS_ENIGME = PTS_PREMIER_COUP;   // (compatibilité)
const PTS_RAPIDITE = 3;    // bonus par salle bouclée rapidement
const PTS_QUIZ     = 2;    // par bonne réponse au quizz final
const NB_QUIZ      = 5;
const MALUS_INDICE = 2;    // retiré du score à chaque indice consulté

/** Nombre d'énigmes du niveau courant (15 en CM1, 20 en CM2). */
function nbEnigmesTotal(){
  if(!ENIGMES) return 0;
  return ENIGMES.salles.reduce((t,s)=>t + enigmesDe(s).length, 0);
}
/** Énigmes d'une salle filtrées selon le niveau. */
function enigmesDe(salle){
  const n = ETAT.niveau || "CM2";
  return (salle.enigmes||[]).filter(e=>!e.niveaux || e.niveaux.includes(n));
}
/** Score maximal atteignable, pour le barème affiché et imprimé. */
function scoreMax(){
  return nbEnigmesTotal()*PTS_PREMIER_COUP + PTS_COFFRE_PREMIER + NB_SALLES*PTS_RAPIDITE + NB_QUIZ*PTS_QUIZ;
}

const CLE_SAUVEGARDE = "escape_matieres_premieres_v1";
const VERSION_APP = "v2";   // v2 : barème du premier coup, coffre final
let DONNEES = null;   // dialogues.json
let ENIGMES = null;   // enigmes.json
let CONCOURS = null;  // pas de concours dans ce jeu

function resetEtatJeu(){
  Object.assign(ETAT, {
    equipe:"", niveau:"CM2", salle:1, enigme:0, score:0, motsCles:[],
    enigmesPremierCoup:0, erreursTotal:0, coffreOuvert:false, coffrePremierCoup:false,
    badges:{vitesse:false, mecene:false, plans:false, atelier:false},
    debut:null, msEcoules:0, enPause:false, tempsParSalle:{}, salleDebut:null,
    indicesSalle:0, indicesTotal:0, enigmesReussies:0,
    quiz:{repondu:false, score:0}, fini:false
  });
}

/* ============================================================
   CHARGEMENT DES DONNÉES
   Robuste : si fetch échoue (ouverture en file://), on bascule
   sur les données embarquées.
   ============================================================ */
async function chargerJSON(chemin){
  try{
    const r = await fetch(chemin, {cache:"no-store"});
    if(r.ok) return await r.json();
  }catch(e){
    console.warn("Fetch impossible ("+chemin+") — mode file:// ? Bascule sur les données embarquées.");
  }
  return null;
}

async function chargerDonnees(){
  // Les évaluations alimentent aussi le quizz final : on les charge dès le départ.
  if(typeof chargerEvaluations === "function") chargerEvaluations();
  DONNEES  = await chargerJSON("assets/data/dialogues.json");
  ENIGMES  = await chargerJSON("assets/data/enigmes.json");
  if(!DONNEES || !DONNEES.salles) DONNEES = JSON.parse(JSON.stringify(DONNEES_FALLBACK));
  if(!ENIGMES || !ENIGMES.salles){
    ENIGMES = JSON.parse(JSON.stringify(ENIGMES_FALLBACK));
    console.warn("enigmes.json introuvable : jeu réduit aux énigmes de secours. "
      + "Lancez le jeu via lancer.bat ou en ligne pour disposer des 20 énigmes.");
  }
  try{
    const r = localStorage.getItem("escape_reglages_matieres_premieres");
    if(r) Object.assign(ETAT.reglages, JSON.parse(r));
  }catch(e){}
  appliquerReglages();
}

/* ---- Données de secours minimales (file:// sans serveur) ---- */
const DONNEES_FALLBACK = {
  personnages: {
    maelle:{nom:"Maëlle"}, odile:{nom:"Odile"}, malik:{nom:"Malik"}, karim:{nom:"Karim"}, jade:{nom:"Jade"}, aubry:{nom:"Madame Aubry"}
  },
  salles:[
    {num:1, titre:"La carrière", decor:"carriere", motCle:"ANALYSER",
     lieu:"La carrière d'argile, à ciel ouvert", description:"Tampon n°1 du bon de lancement.",
     dialogue_intro:{perso:"odile", nom:"Odile", texte:"Bienvenue. Le tampon n°1 est ici."},
     dialogue_reussite:{perso:"odile", nom:"Odile", texte:"Tampon n°1 obtenu."}},
    {num:2, titre:"Le parc d'argile et le silo", decor:"parc", motCle:"REPOSER",
     lieu:"Le parc d'argile et le silo, derrière la carrière", description:"Tampon n°2 du bon de lancement.",
     dialogue_intro:{perso:"malik", nom:"Malik", texte:"Bienvenue. Le tampon n°2 est ici."},
     dialogue_reussite:{perso:"malik", nom:"Malik", texte:"Tampon n°2 obtenu."}},
    {num:3, titre:"L'atelier de broyage", decor:"broyage", motCle:"BROYER",
     lieu:"L'atelier de broyage", description:"Tampon n°3 du bon de lancement.",
     dialogue_intro:{perso:"karim", nom:"Karim", texte:"Bienvenue. Le tampon n°3 est ici."},
     dialogue_reussite:{perso:"karim", nom:"Karim", texte:"Tampon n°3 obtenu."}},
    {num:4, titre:"La station d'épuration", decor:"epuration", motCle:"ÉPURER",
     lieu:"La station d'épuration", description:"Tampon n°4 du bon de lancement.",
     dialogue_intro:{perso:"jade", nom:"Jade", texte:"Bienvenue. Le tampon n°4 est ici."},
     dialogue_reussite:{perso:"jade", nom:"Jade", texte:"Tampon n°4 obtenu."}},
    {num:5, titre:"Le laboratoire des matières dures", decor:"dures", motCle:"CONCASSER",
     lieu:"Le laboratoire des matières dures", description:"Tampon n°5 du bon de lancement.",
     dialogue_intro:{perso:"aubry", nom:"Madame Aubry", texte:"Bienvenue. Le tampon n°5 est ici."},
     dialogue_fin:{perso:"maelle", nom:"Maëlle", texte:"Tampon n°5 obtenu."}}
  ]
};

const ENIGMES_FALLBACK = { salles:[
  {num:1, enigmes:[{id:"secours-1", titre:"La préparation des matières premières", type:"qcm", lecon:"gisement-extraction",
    consigne:"Choisis la bonne réponse.", commun:{questions:[{q:"Quelle est la première étape de préparation de l'argile ?",
      options:["le broyage","l'analyse du terrain","la maturation"], bonne:1}]}}]},
  {num:2, enigmes:[]},{num:3, enigmes:[]},{num:4, enigmes:[]},{num:5, enigmes:[]}
]};

/* ---- Mode vérification (enseignant) ----
   index.html?salle=3&niveau=CM1 ouvre la salle 3 (salle=6 : écran de fin).
   Rien n'est sauvegardé : une partie en cours sur le poste reste intacte. */
const VERIF = (()=>{
  const p = new URLSearchParams(location.search);
  const n = parseInt(p.get("salle"), 10);
  if(!(n >= 1 && n <= NB_SALLES+1)) return null;
  return {
    salle:n,
    niveau: p.get("niveau") === "CM1" ? "CM1" : "CM2",
    enigme: Math.max(0, (parseInt(p.get("enigme"),10)||1) - 1)
  };
})();

/* ---- Sauvegarde ---- */
function sauvegarder(){
  if(VERIF) return;
  try{ localStorage.setItem(CLE_SAUVEGARDE, JSON.stringify(ETAT)); }catch(e){}
}

/* ---- Navigation ---- */
function aller(ecranId){
  document.querySelectorAll(".ecran").forEach(e=>e.classList.remove("actif"));
  document.getElementById(ecranId).classList.add("actif");
  window.scrollTo({top:0, behavior:"smooth"});
}

/* ---- HUD ---- */
function majHUD(){
  document.getElementById("hud").style.display = (ETAT.salle>=1 && ETAT.debut) ? "flex" : "none";
  document.getElementById("hud-eq-nom").textContent = ETAT.equipe || "—";
  document.getElementById("hud-score-val").textContent = ETAT.score;
  document.getElementById("hud-cle-val").textContent = ETAT.motsCles.length;
  const m = Math.floor(ETAT.msEcoules/60000);
  const s = Math.floor((ETAT.msEcoules%60000)/1000);
  document.getElementById("hud-min").textContent = String(m).padStart(2,"0");
  document.getElementById("hud-sec").textContent = String(s).padStart(2,"0");
  const limite = ETAT.reglages.dureeMin || 60;
  document.getElementById("hud-temps").classList.toggle("alerte", m >= limite-5);
  const btnL = document.getElementById("btn-lecons");
  if(btnL) btnL.style.display = ETAT.reglages.leconsAutorisees ? "inline-flex" : "none";
}

/* ---- Minuteur ---- */
let timerId = null, dernierTick = null;
function demarrerTimer(){
  if(timerId) return;
  dernierTick = Date.now();
  timerId = setInterval(()=>{
    if(ETAT.enPause || ETAT.fini){ dernierTick = Date.now(); return; }
    const now = Date.now();
    ETAT.msEcoules += now - dernierTick;
    dernierTick = now;
    majHUD();
    if(ETAT.salle >= 1) sauvegarder();
  }, 1000);
}

/* ---- Score, toast, confettis ---- */
function ajouterScore(pts, raison){
  ETAT.score += pts;
  majHUD();
  if(pts>0) toast("+"+pts+" pts"+(raison?" · "+raison:""));
}
function penaliserIndice(){
  ETAT.indicesSalle++; ETAT.indicesTotal++;
  ETAT.score = Math.max(0, ETAT.score - MALUS_INDICE);
  majHUD(); sauvegarder();
}
function toast(msg){
  const t = document.createElement("div");
  t.className = "toast"; t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(()=>{ t.style.transition="opacity .4s"; t.style.opacity="0"; setTimeout(()=>t.remove(),400); }, 1800);
}
function confettis(n=60){
  const couleurs=["#1d3a8a","#b22222","#c9a227","#2e7d32","#fff"];
  for(let i=0;i<n;i++){
    const c=document.createElement("div");
    c.className="confetti";
    c.style.left=Math.random()*100+"vw";
    c.style.background=couleurs[i%couleurs.length];
    c.style.animationDuration=(0.8+Math.random()*1.2)+"s";
    c.style.animationDelay=(Math.random()*0.3)+"s";
    c.style.transform="rotate("+Math.random()*360+"deg)";
    document.body.appendChild(c);
    setTimeout(()=>c.remove(),2200);
  }
}

/* ---- Barres de progression ---- */
function barreProgression(){
  let html = '<div class="progression" aria-label="Progression dans les salles">';
  for(let i=1;i<=NB_SALLES;i++){
    const cls = i < ETAT.salle ? "fait" : (i===ETAT.salle ? "actuel" : "");
    html += `<div class="prog-point ${cls}">${i}</div>`;
  }
  return html + "</div>";
}
function filEnigmes(total){
  let html = '<div class="fil-enigmes" aria-label="Énigmes de la salle">';
  for(let i=0;i<total;i++){
    const cls = i < ETAT.enigme ? "fait" : (i===ETAT.enigme ? "actuel" : "");
    html += `<div class="fil-point ${cls}">${i+1}</div>`;
  }
  return html + "</div>";
}
/** Les cinq tampons du bon de lancement, tels qu'ils sont à l'instant t. */
function serruresHTML(){
  return `<div class="coffre-serrures" aria-label="Les cinq tampons du bon de lancement">${DONNEES.salles.map((s,i)=>{
    const ouverte = ETAT.motsCles.includes(s.motCle);
    const lisible = ouverte && ETAT.coffreOuvert;
    return `<div class="serrure ${ouverte?"ouverte":""}">
      <span class="icone" aria-hidden="true">${ouverte?"📜":"▫️"}</span>
      <span class="mot">${lisible?s.motCle:ouverte?"🔓 trouvé":"Tampon "+(i+1)+" : à trouver"}</span>
    </div>`;
  }).join("")}</div>`;
}

/* ============================================================
   DÉMARRAGE
   ============================================================ */
document.addEventListener("DOMContentLoaded", async ()=>{
  await chargerDonnees();
  initVoix();

  // Nettoyage d'une sauvegarde d'une version antérieure ou incohérente
  try{
    const vStockee = localStorage.getItem("escape_app_version_matieres_premieres");
    const brut = localStorage.getItem(CLE_SAUVEGARDE);
    if(brut){
      const etat = JSON.parse(brut);
      if(vStockee !== VERSION_APP || (etat.salle && etat.salle > NB_SALLES) || etat.fini){
        localStorage.removeItem(CLE_SAUVEGARDE);
      }
    }
    localStorage.setItem("escape_app_version_matieres_premieres", VERSION_APP);
  }catch(e){}

  const reglagesSauves = ETAT.reglages;
  resetEtatJeu();
  ETAT.reglages = reglagesSauves;

  // Sélection du niveau
  document.querySelectorAll(".opt-niveau").forEach(o=>{
    if(o.dataset.niveau === ETAT.niveau) o.classList.add("choisi");
    o.addEventListener("click", ()=>{
      document.querySelectorAll(".opt-niveau").forEach(x=>x.classList.remove("choisi"));
      o.classList.add("choisi");
      ETAT.niveau = o.dataset.niveau;
      majApercuNiveau();
      verifierPret();
    });
  });
  majApercuNiveau();

  const inp = document.getElementById("input-equipe");
  inp.addEventListener("input", e=>{ ETAT.equipe = e.target.value.trim(); verifierPret(); });

  document.getElementById("btn-demarrer").addEventListener("click", ()=>{
    const niveau = ETAT.niveau, equipe = ETAT.equipe, reglages = ETAT.reglages;
    resetEtatJeu();
    Object.assign(ETAT, {reglages, niveau, equipe, debut:Date.now(), salleDebut:Date.now(), msEcoules:0});
    lancerCine("intro", "Manufacture des Trois Fours, lundi matin", ()=>entrerDansLeJeu(false));
  });

  document.getElementById("btn-pause").addEventListener("click", ()=>{
    ETAT.enPause = true;
    if(typeof setFigerVideos === "function") setFigerVideos(true);
    aller("ecran-pause");
  });
  document.getElementById("btn-reprendre").addEventListener("click", ()=>{
    ETAT.enPause = false;
    dernierTick = Date.now();
    if(typeof setFigerVideos === "function") setFigerVideos(!!ETAT.reglages.animationsReduites);
    aller("ecran-salle");
  });
  document.getElementById("btn-lecons").addEventListener("click", ouvrirBiblioLecons);
  document.getElementById("btn-reglages").addEventListener("click", ouvrirReglages);
  verifierPret();

  if(VERIF){
    ETAT.equipe = "Vérification";
    ETAT.niveau = VERIF.niveau;
    ETAT.salle = Math.min(VERIF.salle, NB_SALLES);
    ETAT.enigme = VERIF.enigme;
    ETAT.debut = ETAT.salleDebut = Date.now();
    ETAT.msEcoules = 0;
    if(VERIF.salle > NB_SALLES){
      // Écran de fin : on simule une partie complète
      ETAT.motsCles = DONNEES.salles.map(s=>s.motCle);
      ETAT.coffreOuvert = true;
      ETAT.enigmesReussies = nbEnigmesTotal();
      ETAT.score = Math.round(scoreMax()*0.8);
      appliquerReglages(); demarrerTimer(); finDuJeu();
    }else{
      entrerDansLeJeu(false);
    }
    toast("🔍 Mode vérification · " + VERIF.niveau + " · rien n'est sauvegardé");
    return;
  }

  // Reprise d'une partie en cours
  let partie = null;
  try{ const s = localStorage.getItem(CLE_SAUVEGARDE); if(s) partie = JSON.parse(s); }catch(e){}
  if(partie && partie.equipe && partie.debut && !partie.fini && partie.salle>=1 && partie.salle<=NB_SALLES){
    if(confirm("Une partie est en cours pour l'équipe « "+partie.equipe+" » (salle "+partie.salle+"/"+NB_SALLES+").\nVoulez-vous la reprendre ?")){
      Object.assign(ETAT, {
        equipe:partie.equipe, niveau:partie.niveau||"CM2", salle:partie.salle,
        enigme:partie.enigme||0, score:partie.score||0, motsCles:partie.motsCles||[],
        badges:partie.badges||ETAT.badges, msEcoules:partie.msEcoules||0,
        enigmesReussies:partie.enigmesReussies||0, indicesTotal:partie.indicesTotal||0,
        tempsParSalle:partie.tempsParSalle||{}, fini:false,
        enigmesPremierCoup:partie.enigmesPremierCoup||0, erreursTotal:partie.erreursTotal||0,
        coffreOuvert:!!partie.coffreOuvert, coffrePremierCoup:!!partie.coffrePremierCoup
      });
      ETAT.debut = Date.now() - ETAT.msEcoules;
      entrerDansLeJeu(true);
      return;
    }else{
      localStorage.removeItem(CLE_SAUVEGARDE);
    }
  }else if(partie && partie.fini){
    localStorage.removeItem(CLE_SAUVEGARDE);
  }
});

function verifierPret(){
  document.getElementById("btn-demarrer").disabled = !(ETAT.equipe.length>=2 && ETAT.niveau);
}
/** Affiche « 15 énigmes » ou « 20 énigmes » sous le choix du niveau. */
function majApercuNiveau(){
  const el = document.getElementById("apercu-niveau");
  if(!el || !ENIGMES) return;
  el.textContent = `${ETAT.niveau} · ${nbEnigmesTotal()} énigmes réparties en ${NB_SALLES} salles · ${scoreMax()} points maximum`;
}

function lancerCine(base, titre, suite){
  if(ETAT.reglages.cinematiques !== false && typeof jouerCinematique === "function"){
    jouerCinematique({base, titre, onFin:suite});
  }else{ suite(); }
}

function appliquerReglages(){
  document.documentElement.style.setProperty("--taille-texte", ETAT.reglages.tailleTexte+"rem");
  setNarrationActif(ETAT.reglages.narrationActive);
  setVolume(ETAT.reglages.volume);
  if(typeof setSonsActifs === "function") setSonsActifs(ETAT.reglages.sonsActifs !== false);
  if(typeof setVolumeSons === "function") setVolumeSons(ETAT.reglages.volumeSons !== undefined ? ETAT.reglages.volumeSons : 0.55);
  document.body.classList.toggle("calme", !!ETAT.reglages.animationsReduites);
  if(typeof setDecorsVideo === "function") setDecorsVideo(ETAT.reglages.decorsVideo !== false);
  if(typeof setSonVideo === "function")    setSonVideo(!!ETAT.reglages.sonVideo);
  if(typeof setFigerVideos === "function") setFigerVideos(!!ETAT.reglages.animationsReduites);
}

function entrerDansLeJeu(reprise){
  appliquerReglages();
  aller("ecran-salle");
  demarrerTimer();
  majHUD();
  afficherSalle(ETAT.salle);
  if(reprise) toast("Partie reprise ✓");
  if(!VERIF && typeof demarrerSync === "function") demarrerSync();
}

/* ============================================================
   AFFICHAGE D'UNE SALLE
   ============================================================ */
function salleEnigmes(n){
  const bloc = (ENIGMES.salles||[]).find(s=>s.num===n);
  return bloc ? enigmesDe(bloc) : [];
}

function afficherSalle(n){
  const salle = DONNEES.salles[n-1];
  if(!salle){ finDuJeu(); return; }
  ETAT.salleDebut = Date.now();
  ETAT.indicesSalle = 0;
  if(typeof stopperVideos === "function") stopperVideos();

  const c = document.getElementById("salle-contenu");
  c.innerHTML = `
    ${barreProgression()}
    <h2>📜 Page ${salle.num}/${NB_SALLES} — ${salle.titre}</h2>
    ${htmlScene(salle.decor, salle)}
    <div id="zone-dialogue"></div>
    <div class="zone-enigme" id="zone-enigme"></div>
  `;
  activerScene(c.querySelector(".scene"));
  if(typeof son === "function") son("transition");
  if(typeof ambiance === "function") ambiance(salle.decor);
  lancerDialogueIntro(salle);
  afficherEnigmeCourante();
  majHUD();
  sauvegarder();
}

async function lancerDialogueIntro(salle){
  let texte = salle.dialogue_intro.texte;
  if(ETAT.reglages.apiActive && ETAT.reglages.apiCle && typeof genererDialogue === "function"){
    try{
      const gen = await genererDialogue({
        perso: salle.dialogue_intro.perso,
        situation: "Arrivée dans : " + salle.titre,
        niveau: ETAT.niveau, reussite:false
      });
      if(gen && gen.trim()) texte = gen;
    }catch(e){ console.warn("IA indisponible, texte écrit conservé :", e.message); }
  }
  afficherDialogue({perso:salle.dialogue_intro.perso, nom:salle.dialogue_intro.nom, texte});
}

/* ---- Une énigme à la fois ---- */
function afficherEnigmeCourante(){
  const liste = salleEnigmes(ETAT.salle);
  const zone = document.getElementById("zone-enigme");
  if(!liste.length){
    zone.innerHTML = `<div class="feedback erreur show">Aucune énigme n'a pu être chargée pour cette salle.</div>`;
    return;
  }
  if(ETAT.enigme >= liste.length){ validerSalle(ETAT.salle); return; }
  const e = liste[ETAT.enigme];
  zone.innerHTML = filEnigmes(liste.length) + enigmeHTML(e, ETAT.enigme+1, liste.length);
  // v2 : taire le personnage dès que les élèves commencent l'énigme (le chrono ne s'arrête jamais)
  zone.addEventListener("pointerdown", ()=>{ if("speechSynthesis" in window) speechSynthesis.cancel(); }, {once:true});
  activerEnigme(e, (en, indices, erreurs)=>reussirEnigme(e, liste, indices, erreurs));
  zone.scrollIntoView({behavior:"smooth", block:"nearest"});
  sauvegarder();
}

function reussirEnigme(e, liste, indices, erreurs){
  ETAT.enigmesReussies++;
  const premierCoup = !erreurs;
  if(premierCoup) ETAT.enigmesPremierCoup = (ETAT.enigmesPremierCoup || 0) + 1;
  ajouterScore(premierCoup ? PTS_PREMIER_COUP : PTS_APRES_ERREUR, premierCoup ? "tout juste du premier coup 🎯" : "énigme résolue");
  confettis(premierCoup ? 40 : 12);
  ETAT.enigme++;
  sauvegarder();
  if(ETAT.enigme >= liste.length){
    setTimeout(()=>validerSalle(ETAT.salle), 700);
  }else{
    const zone = document.getElementById("zone-enigme");
    const suite = document.createElement("div");
    suite.className = "boutons";
    suite.innerHTML = `<button class="btn grand bleu" id="btn-enigme-suivante">➡️ Énigme suivante (${ETAT.enigme+1}/${liste.length})</button>`;
    zone.appendChild(suite);
    suite.querySelector("button").addEventListener("click", afficherEnigmeCourante);
    suite.scrollIntoView({behavior:"smooth", block:"center"});
  }
}

/* Une vérification fausse (compteur pour le bilan et le tableau de bord). */
function compterErreur(){
  ETAT.erreursTotal = (ETAT.erreursTotal || 0) + 1;
  sauvegarder();
}

/* ---- Salle bouclée : la page du carnet est retrouvée ---- */
function validerSalle(n){
  const salle = DONNEES.salles[n-1];
  const duree = Date.now() - ETAT.salleDebut;
  const dejaValidee = ETAT.tempsParSalle[n] !== undefined;   // reprise après rechargement
  ETAT.tempsParSalle[n] = duree;

  if(salle.motCle && !ETAT.motsCles.includes(salle.motCle)) ETAT.motsCles.push(salle.motCle);
  if(typeof son === "function") setTimeout(()=>son("deverrouille"), 300);

  let pts = 0, raison = "";
  const seuil = (ETAT.niveau === "CM1" ? 8 : 10) * 60000;  // rythme attendu par salle
  if(duree < seuil && ETAT.indicesSalle === 0){ pts = PTS_RAPIDITE; raison = "salle rapide et sans indice 🏃"; }
  else if(duree < seuil){ pts = Math.max(1, PTS_RAPIDITE-1); raison = "salle rapide"; }
  if(pts && !dejaValidee) ajouterScore(pts, raison);
  attribuerBadges(n, duree);

  const zone = document.getElementById("zone-enigme");
  zone.innerHTML = `
    <div class="mot-cle">
      <div class="lib">Tampon ${n} du bon de lancement — mot obtenu</div>
      <div class="val">${salle.motCle}</div>
      <div class="a-noter">✍️ Notez ce mot sur votre fiche de mission : il ne sera plus affiché !</div>
    </div>
  `;
  confettis(50);
  sauvegarder();

  if(n === NB_SALLES){
    ajouterBoutonCoffre(()=>setTimeout(()=>lancerCine("final", "Le bon de lancement est complet", finDuJeu), 1600));
    return;
  }

  function boutonSuivant(){
    if(document.getElementById("btn-salle-suivante")) return;
    const b = document.createElement("div");
    b.className = "boutons";
    b.innerHTML = `<button class="btn grand vert" id="btn-salle-suivante">➡️ Chercher le tampon suivant</button>`;
    zone.appendChild(b);
    b.querySelector("button").addEventListener("click", ()=>{
      ETAT.salle++; ETAT.enigme = 0;
      if(ETAT.salle > NB_SALLES) finDuJeu(); else afficherSalle(ETAT.salle);
    });
    b.scrollIntoView({behavior:"smooth", block:"center"});
  }
  boutonSuivant();
}

/* ============================================================
   LE COFFRE FINAL — les élèves retapent les mots notés sur leur
   fiche de mission, salle par salle. Rien n'est rempli pour eux.
   ============================================================ */
function afficherCoffre(suite){
  if(ETAT.coffreOuvert){ suite(); return; }
  const zone = document.getElementById("zone-enigme") || document.getElementById("salle-contenu");
  const dlg = document.querySelector("#salle-contenu .personnage-scene");
  if(dlg) dlg.remove();
  let erreurs = 0;
  zone.innerHTML = `
    <div class="enigme-carte coffre-final" id="coffre-final">
      <div class="enigme-tete"><span class="enigme-num">Énigme finale</span><h3>🔐 Le coffre final</h3></div>
      <div class="bandeau-bareme">🎯 Tout juste du premier coup : <b>${PTS_COFFRE_PREMIER} points</b> · après une erreur : ${PTS_COFFRE_APRES} points seulement</div>
      <div class="consigne">Recopiez, salle par salle, les mots que vous avez notés sur votre fiche de mission. Les accents et les majuscules ne comptent pas.</div>
      ${DONNEES.salles.map((s,i)=>`<div class="coffre-ligne">
        <label for="coffre-${i}">Salle ${s.num} — ${s.titre}</label>
        <input type="text" id="coffre-${i}" autocomplete="off" spellcheck="false" maxlength="24">
      </div>`).join("")}
      <div class="feedback" id="fb-coffre"></div>
      <div class="center"><button class="btn grand vert" id="btn-coffre">🔓 Ouvrir le coffre</button></div>
    </div>`;
  const fb = document.getElementById("fb-coffre");
  const valider = ()=>{
    const champs = DONNEES.salles.map((s,i)=>document.getElementById("coffre-"+i));
    if(champs.some(c=>!c.value.trim())){
      fb.className = "feedback indice show"; fb.innerHTML = "✋ Il manque au moins un mot."; return;
    }
    const justes = DONNEES.salles.filter((s,i)=>normaliser(champs[i].value) === normaliser(s.motCle)).length;
    if(justes === DONNEES.salles.length){
      ETAT.coffreOuvert = true;
      champs.forEach(c=>c.disabled = true);
      document.getElementById("btn-coffre").disabled = true;
      ajouterScore(erreurs ? PTS_COFFRE_APRES : PTS_COFFRE_PREMIER, erreurs ? "coffre ouvert" : "coffre ouvert du premier coup 🎯");
      if(!erreurs) ETAT.coffrePremierCoup = true;
      fb.className = "feedback succes" + (erreurs ? "" : " premier-coup") + " show";
      fb.innerHTML = erreurs ? `✔ Le coffre s'ouvre : +${PTS_COFFRE_APRES} points.` : `🎯 <b>Tout juste du premier coup !</b> +${PTS_COFFRE_PREMIER} points`;
      if(typeof son === "function") son("deverrouille");
      confettis(60);
      sauvegarder();
      setTimeout(suite, 900);
    }else{
      erreurs++;
      if(typeof compterErreur === "function") compterErreur();
      if(typeof son === "function") son("erreur");
      fb.className = "feedback erreur show";
      fb.innerHTML = `✗ <b>Le coffre reste fermé.</b> ${justes} mot${justes>1?"s":""} juste${justes>1?"s":""} sur ${DONNEES.salles.length}.`
        + (erreurs === 1 ? `<div class="perte-bonus">Le bonus du premier coup est perdu : vérifiez votre fiche de mission.</div>` : "");
    }
  };
  document.getElementById("btn-coffre").addEventListener("click", valider);
  zone.querySelectorAll("input").forEach(inp=>inp.addEventListener("keydown", ev=>{ if(ev.key === "Enter") valider(); }));
  zone.scrollIntoView({behavior:"smooth", block:"start"});
}

function ajouterBoutonCoffre(suite){
  const zone = document.getElementById("zone-enigme");
  const b = document.createElement("div");
  b.className = "boutons";
  b.innerHTML = `<button class="btn grand vert" id="btn-coffre-final">🔐 Aller au coffre final</button>`;
  zone.appendChild(b);
  b.querySelector("button").addEventListener("click", ()=>afficherCoffre(suite));
  b.scrollIntoView({behavior:"smooth", block:"center"});
}

/* ---- Badges ---- */
function attribuerBadges(n, duree){
  if(duree < 6*60000) ETAT.badges.vitesse = true;                 // une salle en moins de 6 min
  if(n === 2 && ETAT.indicesSalle === 0) ETAT.badges.mecene = true;     // grande salle sans indice
  if(n === 4 && ETAT.indicesSalle === 0) ETAT.badges.plans = true;      // cabinet des plans sans indice
  if(n === NB_SALLES && ETAT.indicesTotal <= 3) ETAT.badges.atelier = true;
}

/* ============================================================
   FIN DU JEU
   ============================================================ */
function finDuJeu(){
  ETAT.fini = true;
  if(typeof stopperVideos === "function") stopperVideos();
  aller("ecran-fin");
  if(typeof ambiance === "function") ambiance("accueil");
  if(typeof son === "function"){
    son("succes"); setTimeout(()=>son("deverrouille"), 600); setTimeout(()=>son("badge"), 1300);
  }
  const min = Math.floor(ETAT.msEcoules/60000), sec = Math.floor((ETAT.msEcoules%60000)/1000);
  const c = document.getElementById("fin-contenu");
  c.innerHTML = `
    <h2>Le bon de lancement est signé</h2>
    <div id="fin-dialogue"></div>
    ${serruresHTML()}
    <div class="article-secret devise-pli">
      <div class="numero">LE BON DE LANCEMENT</div>
      <div class="texte">« On <b>ANALYSE</b> le terrain, on laisse l'argile <b>REPOSER</b>, on la <b>BROIE</b>, on l'<b>ÉPURE</b>,
        et on <b>CONCASSE</b> les roches : la pâte est alors stable et de qualité constante. »</div>
      <ol class="regnes-pli" aria-label="Les cinq étapes">
        <li><b>1</b> <span>analyser le terrain, extraire</span></li>
        <li><b>2</b> <span>pourrissement et maturation</span></li>
        <li><b>3</b> <span>broyage</span></li>
        <li><b>4</b> <span>épuration</span></li>
        <li><b>5</b> <span>matières dures</span></li>
      </ol>
      <div style="font-size:.8rem;opacity:.75">Le bon est signé : le lot de pâte peut être lancé demain matin.</div>
    </div>
    <div class="pli-final" id="pli-final" aria-hidden="true">
      <svg viewBox="0 0 220 150" width="220" height="150" xmlns="http://www.w3.org/2000/svg">
        <path d="M40 140 V66 Q40 22 110 22 Q180 22 180 66 V140 Z" fill="#0f4c81" stroke="#0b2a4a" stroke-width="2"/>
        <path d="M76 140 V96 a34 34 0 0 1 68 0 V140 Z" fill="#c2410c"/>
        <path d="M110 136 c-12 -8 -12 -20 -3 -30 3 7 7 8 8 3 9 8 9 19 -5 27z" fill="#ffb347"/>
        <rect x="150" y="6" width="16" height="26" fill="#0b2a4a"/>
        <g class="sceaux">${[0,1,2,3,4].map(i=>`<g class="sceau" style="--i:${i}"><rect x="${48+i*26}" y="${56+(i%2)*8}" width="24" height="60" fill="#f3f8fd" stroke="#2f75b5" transform="rotate(${i*3-6} ${60+i*26} 86)"/></g>`).join("")}</g>
      </svg>
    </div>
    <div class="grille-badges">
      ${badgeHTML("vitesse","⏱️","Équipe rapide","une salle en moins de 6 minutes")}
      ${badgeHTML("mecene","🔬","Œil du parc","salle 2 sans aucun indice")}
      ${badgeHTML("plans","🧤","Sécurité d'abord","salle 4 sans aucun indice")}
      ${badgeHTML("atelier","🏺","Main sûre","3 indices au maximum sur toute la partie")}
    </div>
    <p style="text-align:center;opacity:.85">⏱️ Temps total : <b>${min} min ${sec} s</b>
       · 🧩 Énigmes résolues : <b>${ETAT.enigmesReussies}/${nbEnigmesTotal()}</b></p>
    <hr style="border:none;border-top:2px dotted var(--parchemin-ombre);margin:18px 0">
    <h2>Avant de lancer le lot : cinq questions de synthèse</h2>
    <p class="center" style="opacity:.85">Chaque bonne réponse fait avancer le lot. Réponds aux cinq questions, puis vérifie.</p>
    <div id="quizz"></div>
    <div class="feedback" id="fb-quizz"></div>
    <div class="boutons" id="quizz-actions" style="display:none">
      <button class="btn grand vert" id="btn-voir-score">Lancer le lot et voir le score</button>
    </div>
    <div id="score-recap" style="display:none"></div>
    <div class="boutons" style="margin-top:24px">
      <button class="btn bleu" id="btn-rejouer">🔄 Rejouer</button>
      <button class="btn gris" id="btn-imprimer-bilan">🖨️ Imprimer le bilan</button>
    </div>
  `;
  const fin = null;   // v2 : aucun texte après la résolution
  if(fin){
    setTimeout(()=>{
      const scene = document.createElement("div");
      scene.className = "personnage-scene entrer";
      scene.innerHTML = `
        <div class="portrait">${htmlPortrait(fin.perso)}</div>
        <div class="bulle"><div class="nom-perso">${fin.nom}</div><div class="texte" id="fin-texte"></div></div>`;
      c.querySelector("#fin-dialogue").appendChild(scene);
      activerPortrait(scene.querySelector(".portrait-conteneur"));
      machineEcrire(scene.querySelector("#fin-texte"), fin.texte);
      if(NARRATION.parlerActif) parler(fin.perso, fin.texte, scene);
    }, 200);
  }
  construireQuizz();
  document.getElementById("btn-rejouer").addEventListener("click", ()=>{
    localStorage.removeItem(CLE_SAUVEGARDE);
    location.reload();
  });
  document.getElementById("btn-imprimer-bilan").addEventListener("click", imprimerBilan);
  confettis(100);
  sauvegarder();
}

function badgeHTML(cle, icone, nom, desc){
  return `<div class="badge ${ETAT.badges[cle]?"gagne":""}">
    <div class="icone">${icone}</div><div class="nom">${nom}</div><div class="desc">${desc}</div></div>`;
}

/* ============================================================
   QUIZZ FINAL — 5 questions, différenciées, lues dans
   assets/data/evaluations.json (clé "quizz_final")
   ============================================================ */
const QUIZZ_FALLBACK = {
  CM1:[
    {"q": "Pourquoi prépare-t-on les matières premières ?", "options": ["pour qu'elles soient moins chères", "pour obtenir une pâte stable et de qualité constante", "pour les colorer"], "bonne": 1},
    {"q": "Quelle est la première étape de préparation de l'argile ?", "options": ["le broyage", "l'analyse du terrain", "la maturation"], "bonne": 1},
    {"q": "Pendant le pourrissement, l'argile est stockée…", "options": ["dehors", "dans un four", "dans un silo sombre"], "bonne": 0},
    {"q": "Le tamis vibrant sert à…", "options": ["trier les grains selon leur taille", "attirer le fer", "cuire l'argile"], "bonne": 0},
    {"q": "La chamotte est…", "options": ["de l'argile déjà cuite, puis broyée", "un sable lavé", "un fondant"], "bonne": 0}
  ],
  CM2:[
    {"q": "Combien de temps dure le pourrissement ?", "options": ["quelques jours", "de 3 à 24 mois", "au moins 2 semaines"], "bonne": 1},
    {"q": "Après la maturation, le taux d'humidité de l'argile est de…", "options": ["18 % à 22 %", "13 % à 18 %", "5 % à 8 %"], "bonne": 1},
    {"q": "Quelle machine broie à l'aide de billes ?", "options": ["le désagrégateur", "le broyeur à billes", "le concasseur à percussion"], "bonne": 1},
    {"q": "Quelle technique sépare le feldspath de la silice ?", "options": ["la flottation", "le tamisage", "le déferrage"], "bonne": 0},
    {"q": "Pour atteindre un sable enfoui, on…", "options": ["retire la couche supérieure du sol", "utilise des explosifs", "attend la pluie"], "bonne": 0}
  ]
};
function quizzCourant(){
  const ev = (typeof window !== "undefined" && window.EVAL_DATA) || null;
  const src = (ev && ev.quizz_final) || QUIZZ_FALLBACK;
  return (src[ETAT.niveau] || QUIZZ_FALLBACK[ETAT.niveau] || QUIZZ_FALLBACK.CM2).slice(0, NB_QUIZ);
}

function construireQuizz(){
  const cont = document.getElementById("quizz");
  if(!cont) return;
  const QUIZZ = quizzCourant();
  cont.innerHTML = QUIZZ.map((item,i)=>`
    <div class="qcm-question" data-i="${i}">
      <div class="q">${i+1}. ${item.q}</div>
      ${item.options.map((o,j)=>`<label class="qcm-option" data-j="${j}">${o}</label>`).join("")}
    </div>`).join("");
  const repondu = Array(QUIZZ.length).fill(null);
  cont.querySelectorAll(".qcm-question").forEach(qi=>{
    const i = +qi.dataset.i;
    qi.querySelectorAll(".qcm-option").forEach(opt=>{
      opt.addEventListener("click", ()=>{
        qi.querySelectorAll(".qcm-option").forEach(x=>x.classList.remove("select","bien","mal"));
        opt.classList.add("select");
        repondu[i] = +opt.dataset.j;
        if(repondu.every(r=>r!==null)) document.getElementById("quizz-actions").style.display="flex";
      });
    });
  });
  document.getElementById("btn-voir-score").onclick = ()=>{
    if(ETAT.quiz.repondu) return;   // quizz déjà compté : pas de points en double
    let score = 0;
    QUIZZ.forEach((item,i)=>{
      const qi = cont.querySelector(`.qcm-question[data-i="${i}"]`);
      qi.querySelectorAll(".qcm-option").forEach(opt=>{
        const j = +opt.dataset.j;
        opt.classList.remove("select");
        if(j===item.bonne) opt.classList.add("bien");
        else if(j===repondu[i]) opt.classList.add("mal");
      });
      if(repondu[i]===item.bonne) score++;
    });
    ETAT.quiz = {repondu:true, score};
    ETAT.score += score*PTS_QUIZ;
    majHUD();
    const fb = document.getElementById("fb-quizz");
    fb.className = "feedback " + (score>=4?"succes":(score>=3?"indice":"erreur")) + " show";
    fb.innerHTML = `Tu as <b>${score}/${QUIZZ.length}</b> bonnes réponses (+${score*PTS_QUIZ} points). ${
      score===5?"Sans faute : le lot peut partir, la préparation est entre de bonnes mains." :
      score>=4?"Presque parfait. Relis la leçon de la question manquée avant le lancement." :
      score>=3?"Le bon s'entrouvre. Relis les leçons sur l'argile et sa préparation." :
               "Le lot reste en attente. Reprends les leçons, de la carrière au laboratoire."}`;
    const pli = document.getElementById("pli-final");
    if(pli){ pli.querySelectorAll(".sceau").forEach((g,i)=>{ if(i < Math.max(1, score)) g.classList.add("saute"); }); if(score >= 3) pli.classList.add("ouvert"); }
    afficherRecap();
    sauvegarder();
  };
}

function afficherRecap(){
  const recap = document.getElementById("score-recap");
  const max = scoreMax();
  const min = Math.floor(ETAT.msEcoules/60000), sec = Math.floor((ETAT.msEcoules%60000)/1000);
  const nbBadges = Object.values(ETAT.badges).filter(Boolean).length;
  const part = ETAT.score / max;
  const mention = part>=0.9 ? "🏆 Cheffe ou chef de fabrication"
                : part>=0.75 ? "🥈 Compagnon de l'atelier"
                : part>=0.55 ? "🥉 Apprentie ou apprenti confirmé"
                : "📜 Nouvelle recrue";
  recap.style.display = "block";
  recap.innerHTML = `
    <div class="article-secret">
      <div class="sceau">🏁</div>
      <div class="numero">BILAN DE L'ÉQUIPE « ${ETAT.equipe.toUpperCase()} »</div>
      <div class="score-final">${ETAT.score}<span class="sur"> / ${max}</span></div>
      <div style="font-size:1.1rem;color:var(--bleu-fonce);font-weight:bold">${mention}</div>
      <hr style="border:none;border-top:1px solid #c9b78a;margin:12px 0">
      <div>⏱️ Temps : <b>${min} min ${sec} s</b></div>
      <div>🧩 Énigmes : <b>${ETAT.enigmesReussies}/${nbEnigmesTotal()}</b></div>
      <div>🎯 Justes du premier coup : <b>${ETAT.enigmesPremierCoup||0}/${nbEnigmesTotal()}</b> · ✗ Erreurs : <b>${ETAT.erreursTotal||0}</b></div>
      <div>📜 Fiches : <b>${ETAT.motsCles.length}/${NB_SALLES}</b></div>
      <div>💡 Indices utilisés : <b>${ETAT.indicesTotal}</b></div>
      <div>📝 Quizz : <b>${ETAT.quiz.score}/${NB_QUIZ}</b></div>
      <div>🏅 Badges : <b>${nbBadges}/4</b></div>
      <div>Niveau : <b>${ETAT.niveau}</b></div>
    </div>`;
  recap.scrollIntoView({behavior:"smooth", block:"center"});
  confettis(60);
}

/* Exposé global */
window.ETAT = ETAT;
window.DONNEES = () => DONNEES;
window.ENIGMES = () => ENIGMES;
window.CONCOURS = () => CONCOURS;
window.NB_SALLES = NB_SALLES;
window.afficherSalle = afficherSalle;
window.validerSalle = validerSalle;
window.finDuJeu = finDuJeu;
window.sauvegarder = sauvegarder;
window.majHUD = majHUD;
window.ajouterScore = ajouterScore;
window.penaliserIndice = penaliserIndice;
window.toast = toast;
window.confettis = confettis;
window.scoreMax = scoreMax;
window.nbEnigmesTotal = nbEnigmesTotal;
window.salleEnigmes = salleEnigmes;
window.enigmesDe = enigmesDe;
window.quizzCourant = quizzCourant;
