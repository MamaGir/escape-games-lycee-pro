/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — « Les fiches du four »
   ------------------------------------------------------------
   RIG (classes réutilisées par css/animations.css) :
     .tete .yeux .paupiere .bouche .sourcils   → lip-sync
     .buste                                    → respiration
     .bras-g / .bras-d  .avant-g / .avant-d    → épaule / coude
     .main-g  / .main-d                        → mains
     .jambes                                   → appui

   Gestes pilotés par des classes posées sur .portrait :
     .parle · .geste-pointe · .geste-joie · .geste-inquiet · .geste-salue

   Cascade d'affichage (voir js/media.js) :
     VIDÉO assets/videos/personnages/<nom>.mp4
   → IMAGE assets/images/personnages/<nom>.png
   → SVG dessiné ci-dessous

   Personnages (tous inventés) : maelle (apprentie, guide), ines (magasinière),
   theo (laboratoire), awa (réserve), lucas (préparation), ferrand (cheffe du four).
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.maelle;
}

/** HTML complet d'un personnage (image si présente, sinon SVG). */
function htmlPersonnage(perso){
  const src = `assets/images/personnages/${perso}.png`;
  const svg = svgPersonnage(perso);
  return `
    <div class="portrait-conteneur perso-plein-conteneur" data-perso="${perso}">
      <img src="${src}" alt="${perso}" class="portrait-img-cachee"
           onerror="this.style.display='none';this.parentElement.querySelector('.portrait-svg').style.display='block'"
           style="display:none">
      <div class="portrait-svg" style="display:block">${svg}</div>
    </div>`;
}

/** Version de base : media.js la remplace par la cascade vidéo/image. */
function activerPortraitBase(conteneur){
  if(!conteneur) return;
  const img = conteneur.querySelector(".portrait-img-cachee");
  const svg = conteneur.querySelector(".portrait-svg");
  if(!img || !svg) return;
  const test = new Image();
  test.onload = ()=>{ img.style.display="block"; svg.style.display="none"; };
  test.src = img.src;
}

/* ---- Un visage complet ---- */
function visage({idPeau, oeil="#3a2a1a", sourcil="#3a2a1a", joue=".35", nez="#c89a70", bouche="#a8434a", levre="#8d3a40"}){
  return `
      <ellipse cx="100" cy="86" rx="31" ry="36" fill="url(#${idPeau})"/>
      <ellipse cx="82" cy="97" rx="8" ry="5" fill="#e79a97" opacity="${joue}"/>
      <ellipse cx="118" cy="97" rx="8" ry="5" fill="#e79a97" opacity="${joue}"/>
      <g class="sourcils">
        <path d="M82 74 Q88 70 94 74" stroke="${sourcil}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
        <path d="M106 74 Q112 70 118 74" stroke="${sourcil}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      </g>
      <g class="yeux">
        <ellipse cx="88" cy="83" rx="6" ry="4.6" fill="#fff"/>
        <ellipse cx="112" cy="83" rx="6" ry="4.6" fill="#fff"/>
        <circle cx="88" cy="83" r="3" fill="${oeil}"/>
        <circle cx="112" cy="83" r="3" fill="${oeil}"/>
        <circle cx="89.2" cy="81.8" r="1.1" fill="#fff"/>
        <circle cx="113.2" cy="81.8" r="1.1" fill="#fff"/>
        <ellipse class="paupiere" cx="88" cy="83" rx="6.3" ry="4.9" fill="url(#${idPeau})"/>
        <ellipse class="paupiere" cx="112" cy="83" rx="6.3" ry="4.9" fill="url(#${idPeau})"/>
      </g>
      <path d="M100 88 Q97 95 101 97" stroke="${nez}" stroke-width="2" fill="none" stroke-linecap="round"/>
      <ellipse class="bouche bouche-ouverte" cx="100" cy="107" rx="7" ry="4" fill="${bouche}"/>
      <path class="bouche-fermee" d="M93 107 Q100 110 107 107" stroke="${levre}" stroke-width="2" fill="none" stroke-linecap="round"/>`;
}

/**
 * Assemble un personnage plein corps (viewBox 200 × 320).
 * id        suffixe unique des dégradés
 * peau      une entrée de PEAU
 * fond      [clair, foncé] du fond
 * habit     [clair, foncé] du vêtement principal
 * robe      true : robe longue (les jambes ne se voient pas)
 * bas       couleur des chausses (si pas de robe)
 * cheveux   chemin SVG des cheveux (derrière le visage)
 * coiffe    SVG posé par-dessus la tête
 * dessus    SVG ajouté sur le buste (ceinture, tablier, blason…)
 * objetD    SVG tenu dans la main droite
 */
function perso({id, peau, fond, habit, robe=false, bas="#4a3b2a", cheveux="", coiffe="", dessus="", objetD="", visageOpts={}}){
  const g = `url(#habit${id})`, p = `url(#peau${id})`;
  const jambes = robe
    ? `<path d="M66 196 Q60 250 54 300 L146 300 Q140 250 134 196 Z" fill="${g}"/>
       <ellipse cx="80" cy="302" rx="14" ry="5" fill="#3b2a1a"/><ellipse cx="120" cy="302" rx="14" ry="5" fill="#3b2a1a"/>`
    : `<path d="M78 208 L74 292 L92 292 L95 208 Z" fill="${bas}"/>
       <path d="M105 208 L108 292 L126 292 L122 208 Z" fill="${bas}"/>
       <ellipse cx="82" cy="298" rx="15" ry="6" fill="#3b2a1a"/><ellipse cx="118" cy="298" rx="15" ry="6" fill="#3b2a1a"/>`;
  return `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fond${id}" cx="50%" cy="32%" r="78%"><stop offset="0%" stop-color="${fond[0]}"/><stop offset="100%" stop-color="${fond[1]}"/></radialGradient>
    <linearGradient id="peau${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${peau[0]}"/><stop offset="100%" stop-color="${peau[1]}"/></linearGradient>
    <linearGradient id="habit${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${habit[0]}"/><stop offset="100%" stop-color="${habit[1]}"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fond${id})"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">${jambes}</g>
    <g class="bras bras-g">
      <path d="M72 140 Q58 172 56 204" stroke="${g}" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M56 204 Q54 222 58 236" stroke="${g}" stroke-width="14" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="59" cy="242" r="9" fill="${p}"/>
      </g>
    </g>
    <g class="buste">
      <path d="M70 130 Q100 118 130 130 L138 210 Q100 220 62 210 Z" fill="${g}"/>
      <path d="M90 118 L110 118 L110 130 Q100 136 90 130 Z" fill="${p}"/>
      ${dessus}
    </g>
    <g class="bras bras-d">
      <path d="M128 140 Q142 172 144 204" stroke="${g}" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M144 204 Q146 222 142 236" stroke="${g}" stroke-width="14" fill="none" stroke-linecap="round"/>
        <g class="main-d"><circle cx="141" cy="242" r="9" fill="${p}"/>${objetD}</g>
      </g>
    </g>
    <g class="tete">
      ${cheveux}
      ${visage(Object.assign({idPeau:"peau"+id}, visageOpts))}
      ${coiffe}
    </g>
  </g>
</svg>`;
}

/* ============================================================
   BIBLIOTHÈQUE DES PERSONNAGES
   ============================================================ */
const SVG_PERSOS = {

/* MAËLLE — apprentie de 2e année (personnage inventé) : blouse bleue, tablier taché d'engobe, pinceau */
maelle: perso({
  id:"Ma", peau:PEAU.claire, fond:["#2f75b5","#0b2540"], habit:["#2f75b5","#1d4f80"], bas:"#2a3644",
  cheveux:`<path d="M66 92 Q60 50 100 46 Q140 50 134 92 Q132 132 122 150 L116 112 Q100 70 84 112 L78 150 Q68 132 66 92" fill="#7a3e1c"/>`,
  dessus:`<path d="M78 150 L122 150 L126 210 L74 210 Z" fill="#f2efe8"/><g fill="#c96e4a" opacity=".7"><circle cx="90" cy="176" r="4"/><circle cx="110" cy="192" r="3"/></g>`,
  objetD:`<g transform="translate(150,236) rotate(-30)"><rect x="-2" y="-30" width="4" height="34" fill="#a57a4a"/><path d="M-4 -30 L4 -30 L2 -42 L-2 -42 Z" fill="#2a3644"/></g>`,
  visageOpts:{oeil:"#2a3a1a", sourcil:"#5a2a10", joue:".35"}
}),

/* INÈS — magasinière (personnage inventée) : gilet de sécurité, tablette */
ines: perso({
  id:"In", peau:PEAU.foncee, fond:["#6f7c88","#1e2a36"], habit:["#3a4654","#26303a"], bas:"#26303a",
  cheveux:`<path d="M64 90 Q58 46 100 42 Q142 46 136 90 Q134 70 100 66 Q66 70 64 90" fill="#1a1210"/><circle cx="100" cy="40" r="16" fill="#1a1210"/>`,
  dessus:`<path d="M72 136 L92 136 L94 210 L70 208 Z" fill="#ffd400"/><path d="M108 136 L128 136 L130 208 L106 210 Z" fill="#ffd400"/><g fill="#d9e4ee"><rect x="71" y="176" width="22" height="5"/><rect x="107" y="176" width="22" height="5"/></g>`,
  objetD:`<g transform="translate(150,240)"><rect x="-14" y="-20" width="28" height="36" rx="3" fill="#1e2a36"/><rect x="-11" y="-17" width="22" height="28" fill="#9fd3ff"/></g>`,
  visageOpts:{oeil:"#1a1210", sourcil:"#1a1210", joue:".2", nez:"#6e4022"}
}),

/* THÉO — technicien de laboratoire (personnage inventé) : blouse blanche, lunettes, coupelle */
theo: perso({
  id:"Th", peau:PEAU.hale, fond:["#e9f2f8","#7d8a96"], habit:["#f7f9fb","#cfdbe6"], bas:"#2a3644",
  cheveux:`<path d="M68 84 Q66 50 100 48 Q134 50 132 84 Q122 62 100 62 Q78 62 68 84" fill="#2a1a10"/>`,
  dessus:`<path d="M92 130 L100 160 L108 130" fill="#2f75b5"/><g fill="none" stroke="#26303a" stroke-width="3"><circle cx="86" cy="96" r="10"/><circle cx="114" cy="96" r="10"/><line x1="96" y1="96" x2="104" y2="96"/></g>`,
  objetD:`<g transform="translate(150,242)"><ellipse rx="16" ry="6" fill="#fff" stroke="#7d8a96"/><ellipse rx="10" ry="3" fill="#c9a77a"/></g>`,
  visageOpts:{oeil:"#2a1a10", sourcil:"#2a1a10", joue:".25"}
}),

/* AWA — responsable de la réserve (personnage inventée) : bleu de travail, foulard, motte d'argile */
awa: perso({
  id:"Aw", peau:PEAU.foncee, fond:["#c9a77a","#4e3722"], habit:["#1d4f80","#0f2f50"], bas:"#0f2f50",
  cheveux:`<path d="M62 90 Q58 48 100 44 Q142 48 138 90 Q136 66 100 62 Q64 66 62 90" fill="#1a1210"/>`,
  coiffe:`<path d="M60 74 Q62 38 100 36 Q138 38 140 74 Q100 56 60 74 Z" fill="#c2410c"/><circle cx="138" cy="70" r="6" fill="#c2410c"/>`,
  objetD:`<g transform="translate(150,240)"><path d="M-16 6 Q-18 -14 0 -16 Q18 -14 16 6 Z" fill="#b5532f"/></g>`,
  visageOpts:{oeil:"#1a1210", sourcil:"#1a1210", joue:".2", nez:"#6e4022"}
}),

/* LUCAS — préparateur de pâtes (personnage inventé) : masque autour du cou, gants, tablier */
lucas: perso({
  id:"Lu", peau:PEAU.claire, fond:["#9aaab8","#2a3644"], habit:["#5c6670","#3a4654"], bas:"#2a3644",
  cheveux:`<path d="M68 82 Q70 46 100 46 Q130 46 132 82 L126 70 L118 78 L110 66 L100 76 L90 66 L82 78 L74 70 Z" fill="#c9a24a"/>`,
  dessus:`<path d="M80 124 Q100 138 120 124 L118 134 Q100 146 82 134 Z" fill="#f4fbff" stroke="#9aaab8"/><path d="M76 150 L124 150 L128 212 L72 212 Z" fill="#7d4a28"/>`,
  objetD:`<g transform="translate(150,242)"><path d="M-10 -14 L10 -14 L12 10 L-12 10 Z" fill="#2f9e5a"/></g>`,
  visageOpts:{oeil:"#2a3a4a", sourcil:"#a07a30", joue:".35"}
}),

/* MADAME FERRAND — cheffe du four (personnage inventée) : veste ignifugée, gants épais, visière relevée */
ferrand: perso({
  id:"Fe", peau:PEAU.pale, fond:["#c2410c","#2a1206"], habit:["#8a96a3","#5c6670"], bas:"#2a3644",
  cheveux:`<path d="M66 96 Q60 52 100 48 Q140 52 134 96 Q138 118 128 128 Q124 80 100 72 Q76 80 72 128 Q62 118 66 96" fill="#b8b8b8"/>`,
  coiffe:`<path d="M66 64 Q100 30 134 64 L134 72 L66 72 Z" fill="#26303a"/><rect x="70" y="56" width="60" height="10" rx="3" fill="#9fd3ff" opacity=".7"/>`,
  objetD:`<g transform="translate(150,242)"><rect x="-14" y="-16" width="28" height="30" rx="8" fill="#c9a24a"/></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#8a8a8a", joue:".3"}
})
};


/* ---- Gestes ---- */
function geste(cible, nomGeste, duree=2200){
  const el = typeof cible === "string" ? document.querySelector(cible) : cible;
  if(!el) return;
  ["geste-pointe","geste-joie","geste-inquiet","geste-salue"].forEach(c=>el.classList.remove(c));
  if(nomGeste && nomGeste !== "neutre"){
    void el.offsetWidth;
    el.classList.add("geste-"+nomGeste);
    if(duree > 0) setTimeout(()=>el.classList.remove("geste-"+nomGeste), duree);
  }
}

/** Le personnage actuellement à l'écran. */
function persoCourant(){
  return document.querySelector(".personnage-scene .portrait");
}

window.htmlPortrait     = htmlPersonnage;
window.htmlPersonnage   = htmlPersonnage;
window.svgPersonnage    = svgPersonnage;
window.activerPortrait  = activerPortraitBase; // media.js remplace ensuite
window.geste            = geste;
window.persoCourant     = persoCourant;
window.SVG_PERSOS       = SVG_PERSOS;
