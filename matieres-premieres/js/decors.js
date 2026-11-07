/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de « Le bon de lancement »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux (manufacture des Trois Fours, chaîne de préparation) :
     carriere    la carrière d'argile : gradins, excavatrice, grille d'échantillons
     parc        le parc d'argile sous la pluie et le silo
     broyage     l'atelier de broyage : convoyeur, meule, marteaux, billes
     epuration   la station d'épuration : tamis vibrant, aimants, flottation
     dures       le laboratoire des matières dures : feldspath, sable, chamotte
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["carriere"];
  const sens = (contenu.sens||[]).map(s=>`<span>${s}</span>`).join("");
  return `
    <div class="scene scene--media" data-salle="${salle}" data-media="salle${SALLE_NUM[salle]||1}">
      <div class="decor-fallback">${svg}</div>
      <div class="decor-overlay"></div>
      <div class="decor-contenu">
        <span class="lieu">${contenu.lieu||""}</span>
        <p class="description">${contenu.description||""}</p>
        ${sens?`<div class="sens">${sens}</div>`:""}
      </div>
    </div>`;
}

/** Active la scène : cherche le média (vidéo puis image). */
function activerScene(sceneEl){
  if(!sceneEl) return;
  if(typeof nettoyerVideos === "function") nettoyerVideos();
  const base = sceneEl.dataset.media;
  if(base && typeof installerDecor === "function") installerDecor(sceneEl, base);
}

const SALLE_NUM = { "carriere":1, "parc":2, "broyage":3, "epuration":4, "dures":5 };

/* ---- Fragments communs ---- */
const CIEL_JOUR = `
  <linearGradient id="cielJour" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#8fb8de"/><stop offset="70%" stop-color="#e6ecd8"/><stop offset="100%" stop-color="#f1ead2"/>
  </linearGradient>`;
const NUAGES = `
  <g opacity=".65">
    <ellipse cx="140" cy="40" rx="58" ry="13" fill="#fff"><animate attributeName="cx" values="120;700;120" dur="110s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="580" cy="28" rx="42" ry="10" fill="#fff"><animate attributeName="cx" values="560;-60;560" dur="140s" repeatCount="indefinite"/></ellipse>
  </g>`;

const SVG_DECORS = {

/* SALLE 1 — La carrière : gradins d'argile, excavatrice, grille d'échantillons */
"carriere": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_JOUR}</defs>
  <rect width="800" height="300" fill="url(#cielJour)"/>${NUAGES}
  <polygon points="0,150 220,150 220,190 430,190 430,230 640,230 640,262 800,262 800,300 0,300" fill="#a8693b"/>
  <g fill="#c98b5a"><rect x="0" y="150" width="220" height="10"/><rect x="220" y="190" width="210" height="10"/><rect x="430" y="230" width="210" height="10"/><rect x="640" y="262" width="160" height="10"/></g>
  <g fill="#8d5530" opacity=".55"><rect x="0" y="172" width="220" height="6"/><rect x="220" y="212" width="210" height="6"/><rect x="430" y="252" width="210" height="6"/></g>
  <g transform="translate(470,150)"><rect x="0" y="62" width="110" height="18" rx="9" fill="#3a3a3a"/><rect x="10" y="36" width="64" height="28" fill="#e0a526"/><rect x="46" y="14" width="30" height="24" fill="#e0a526"/><rect x="52" y="18" width="18" height="12" fill="#bfe0f5"/>
    <g><path d="M24 40 L-26 6 L-64 42" stroke="#e0a526" stroke-width="8" fill="none" stroke-linejoin="round"/><path d="M-64 42 L-80 64 H-52 Z" fill="#3a3a3a"/>
      <animateTransform attributeName="transform" type="rotate" values="0 24 40;-10 24 40;0 24 40" dur="3.4s" repeatCount="indefinite"/></g></g>
  <g transform="translate(60,60)"><rect x="40" y="46" width="8" height="46" fill="#7a5a3a"/><rect x="0" y="0" width="130" height="54" rx="4" fill="#fff" stroke="#4c5e70" stroke-width="3"/>
    <g stroke="#4c5e70" stroke-width="2">${[1,2,3].map(i=>`<line x1="${i*32.5}" y1="0" x2="${i*32.5}" y2="54"/>`).join("")}<line x1="0" y1="27" x2="130" y2="27"/></g>
    <text x="65" y="-6" text-anchor="middle" font-family="Segoe UI,Arial" font-size="11" font-weight="bold" fill="#0f4c81">GRILLE D'ÉCHANTILLONS</text></g>
  <path d="M240 300 Q270 232 310 242 Q350 252 360 300 Z" fill="#8d5530"/><path d="M252 300 Q276 246 310 254 Q342 262 350 300 Z" fill="#c98b5a" opacity=".5"/>
</svg>`,

/* SALLE 2 — Le parc d'argile sous la pluie et le silo */
"parc": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs><linearGradient id="cielPluie" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#7a8a9a"/><stop offset="100%" stop-color="#b9c4cd"/></linearGradient></defs>
  <rect width="800" height="300" fill="url(#cielPluie)"/><rect y="250" width="800" height="50" fill="#6f7c88"/>
  <path d="M30 250 Q130 120 300 130 Q430 140 470 250 Z" fill="#8d5530"/><path d="M80 250 Q170 150 290 156 Q390 164 420 250 Z" fill="#a8693b" opacity=".6"/>
  <g stroke="#dbe7f2" stroke-width="1.5" opacity=".7">${[...Array(26)].map((_,k)=>`<line x1="${20+k*30}" y1="-20" x2="${12+k*30}" y2="8"><animateTransform attributeName="transform" type="translate" values="0 0;-10 290" dur="${1.1+(k%5)*.15}s" begin="${(k%7)*.12}s" repeatCount="indefinite"/></line>`).join("")}</g>
  <g transform="translate(580,30)"><rect x="0" y="20" width="110" height="216" fill="#4c5e70"/><ellipse cx="55" cy="20" rx="55" ry="14" fill="#7c8fa3"/>
    <g stroke="#33414f" stroke-width="3"><line x1="0" y1="80" x2="110" y2="80"/><line x1="0" y1="140" x2="110" y2="140"/><line x1="0" y1="200" x2="110" y2="200"/></g>
    <rect x="26" y="96" width="58" height="26" rx="3" fill="#fff"/><text x="55" y="114" text-anchor="middle" font-family="Segoe UI,Arial" font-size="13" font-weight="bold" fill="#0f4c81">SILO</text></g>
  <g transform="translate(90,36)"><rect x="0" y="0" width="190" height="56" rx="4" fill="#0b1724" stroke="#2f75b5" stroke-width="3"/>
    <text x="95" y="24" text-anchor="middle" font-family="Consolas,monospace" font-size="14" fill="#ffb347">3 à 24 mois</text><text x="95" y="44" text-anchor="middle" font-family="Consolas,monospace" font-size="12" fill="#9fd3ff">au moins 2 semaines</text></g>
</svg>`,

/* SALLE 3 — L'atelier de broyage : convoyeur, broyeurs */
"broyage": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs><linearGradient id="murB" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d9e4ee"/><stop offset="100%" stop-color="#b7c7d6"/></linearGradient><clipPath id="cvB"><rect x="40" y="206" width="640" height="18"/></clipPath></defs>
  <rect width="800" height="300" fill="url(#murB)"/><rect y="250" width="800" height="50" fill="#6f7c88"/>
  <rect x="30" y="220" width="660" height="12" rx="6" fill="#7c8fa3"/><circle cx="36" cy="226" r="11" fill="#4c5e70"/><circle cx="684" cy="226" r="11" fill="#4c5e70"/>
  <g clip-path="url(#cvB)"><g>${[0,1,2,3,4,5,6,7].map(k=>`<rect x="${-60+k*90}" y="206" width="30" height="14" rx="3" fill="${k%2?"#a8693b":"#c98b5a"}"/>`).join("")}<animateTransform attributeName="transform" type="translate" values="0 0;90 0" dur="2.6s" repeatCount="indefinite"/></g></g>
  <g transform="translate(70,60)"><path d="M0 0H100L84 52H16Z" fill="#4c5e70"/><rect x="10" y="52" width="80" height="106" rx="6" fill="#7c8fa3"/>
    <circle cx="50" cy="104" r="22" fill="#4c5e70"/><g><path d="M50 84V124M30 104H70" stroke="#d9e4ee" stroke-width="5"/><animateTransform attributeName="transform" type="rotate" values="0 50 104;360 50 104" dur="1.4s" repeatCount="indefinite"/></g></g>
  <g transform="translate(240,90)"><rect x="0" y="0" width="170" height="70" rx="35" fill="#7c8fa3"/><g fill="#d9e4ee" opacity=".9"><circle cx="40" cy="36" r="9"/><circle cx="72" cy="42" r="9"/><circle cx="104" cy="32" r="9"/><circle cx="134" cy="40" r="9"/><animateTransform attributeName="transform" type="translate" values="0 0;0 -4;0 0" dur="1.8s" repeatCount="indefinite"/></g></g>
  <g transform="translate(470,60)"><rect x="0" y="40" width="110" height="110" rx="8" fill="#7c8fa3"/><circle cx="55" cy="95" r="34" fill="#4c5e70"/><g stroke="#d9e4ee" stroke-width="6"><line x1="55" y1="61" x2="55" y2="129"/><line x1="21" y1="95" x2="89" y2="95"/><animateTransform attributeName="transform" type="rotate" values="0 55 95;360 55 95" dur="1.1s" repeatCount="indefinite"/></g><rect x="30" y="0" width="50" height="40" fill="#4c5e70"/></g>
  <g transform="translate(700,40)"><rect x="0" y="0" width="80" height="60" rx="4" fill="#fff" stroke="#4c5e70" stroke-width="3"/><text x="40" y="26" text-anchor="middle" font-family="Segoe UI,Arial" font-size="12" font-weight="bold" fill="#0f4c81">PLAQUES</text><text x="40" y="44" text-anchor="middle" font-family="Segoe UI,Arial" font-size="12" font-weight="bold" fill="#c2410c">MANQUANTES</text></g>
</svg>`,

/* SALLE 4 — La station d'épuration : tamis, aimants, flottation */
"epuration": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs><linearGradient id="murE" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e3edf5"/><stop offset="100%" stop-color="#c3d3e0"/></linearGradient></defs>
  <rect width="800" height="300" fill="url(#murE)"/><rect y="252" width="800" height="48" fill="#6f7c88"/>
  <g transform="translate(60,70)"><g><path d="M0 0H120L136 100H-16Z" fill="#4c5e70"/><g fill="#d9e4ee">${[0,1,2,3,4].map(i=>`<circle cx="${12+i*24}" cy="60" r="4"/>`).join("")}${[0,1,2,3].map(i=>`<circle cx="${24+i*24}" cy="78" r="4"/>`).join("")}</g>
      <animateTransform attributeName="transform" type="translate" values="-3 0;3 0;-3 0" dur=".22s" repeatCount="indefinite"/></g><rect x="-6" y="100" width="148" height="80" rx="8" fill="#7c8fa3"/></g>
  <g transform="translate(300,110)"><circle cx="60" cy="60" r="58" fill="#c0392b"/><circle cx="60" cy="60" r="30" fill="#7c8fa3"/><rect x="40" y="-18" width="40" height="14" fill="#eee"/>
    <g><path d="M60 40V80M40 60H80" stroke="#4c5e70" stroke-width="4"/><animateTransform attributeName="transform" type="rotate" values="0 60 60;360 60 60" dur="3s" repeatCount="indefinite"/></g></g>
  <g transform="translate(470,60)"><path d="M0 0H180V30L200 190H-20L0 30Z" fill="none" stroke="#4c5e70" stroke-width="6" stroke-linejoin="round"/><path d="M-10 80H190L200 190H-20Z" fill="#7fb5de" opacity=".85"/>
    <g fill="#fff" opacity=".9">${[[30,170],[70,170],[110,170],[150,170],[90,170]].map(([x,y],k)=>`<circle cx="${x}" cy="${y}" r="${5+k%3*2}"><animate attributeName="cy" values="170;86" dur="${2.4+k*.3}s" begin="${k*.5}s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;0" dur="${2.4+k*.3}s" begin="${k*.5}s" repeatCount="indefinite"/></circle>`).join("")}</g></g>
  <g transform="translate(700,40)"><path d="M40 0L80 70H0Z" fill="#f2c14e" stroke="#33414f" stroke-width="4" stroke-linejoin="round"/><text x="40" y="58" text-anchor="middle" font-family="Arial" font-size="38" font-weight="bold" fill="#33414f">!</text><rect x="-4" y="84" width="88" height="46" rx="3" fill="#fff" stroke="#33414f" stroke-width="3"/><text x="40" y="104" text-anchor="middle" font-family="Segoe UI,Arial" font-size="12" font-weight="bold" fill="#c2410c">MASQUE</text><text x="40" y="120" text-anchor="middle" font-family="Segoe UI,Arial" font-size="10" fill="#33414f">OBLIGATOIRE</text></g>
</svg>`,

/* SALLE 5 — Le laboratoire des matières dures : bacs, concasseurs, tableau */
"dures": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs><linearGradient id="murD" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e3edf5"/><stop offset="100%" stop-color="#c3d3e0"/></linearGradient></defs>
  <rect width="800" height="300" fill="url(#murD)"/><rect y="238" width="800" height="62" fill="#4c5e70"/><rect y="230" width="800" height="12" fill="#7c8fa3"/>
  ${[[60,"#e8d9c4","FELDSPATH"],[190,"#efe7d6","SABLE"],[320,"#c98b5a","CHAMOTTE"]].map(([x,c,t])=>`<g transform="translate(${x},0)"><rect x="0" y="150" width="110" height="80" rx="4" fill="${c}" stroke="#7c8fa3" stroke-width="3"/><rect x="14" y="170" width="82" height="26" fill="#fff" opacity=".85"/><text x="55" y="188" text-anchor="middle" font-family="Segoe UI,Arial" font-size="12" font-weight="bold" fill="#0f4c81">${t}</text></g>`).join("")}
  <g transform="translate(500,100)"><path d="M0 0H80L64 60H16Z" fill="#4c5e70"/><rect x="10" y="60" width="60" height="70" rx="5" fill="#7c8fa3"/><g><path d="M20 90L40 76L60 90" stroke="#d9e4ee" stroke-width="6" fill="none"/><animateTransform attributeName="transform" type="translate" values="0 0;0 6;0 0" dur=".9s" repeatCount="indefinite"/></g></g>
  <g transform="translate(620,100)"><path d="M0 0H80L64 60H16Z" fill="#4c5e70"/><rect x="10" y="60" width="60" height="70" rx="5" fill="#7c8fa3"/><circle cx="40" cy="96" r="14" fill="#4c5e70"/><g stroke="#d9e4ee" stroke-width="4"><line x1="40" y1="84" x2="40" y2="108"/><line x1="28" y1="96" x2="52" y2="96"/><animateTransform attributeName="transform" type="rotate" values="0 40 96;360 40 96" dur="1.5s" repeatCount="indefinite"/></g></g>
  <g transform="translate(60,20)"><rect x="0" y="0" width="320" height="100" rx="6" fill="#0b1724" stroke="#2f75b5" stroke-width="3"/>
    <text x="160" y="30" text-anchor="middle" font-family="Segoe UI,Arial" font-size="14" font-weight="bold" fill="#9fd3ff">Feldspath : fondant</text><text x="160" y="56" text-anchor="middle" font-family="Segoe UI,Arial" font-size="14" font-weight="bold" fill="#ffb347">Sable de silice : dégraissant</text><text x="160" y="82" text-anchor="middle" font-family="Segoe UI,Arial" font-size="14" font-weight="bold" fill="#9fd3ff">Chamotte : argile déjà cuite</text></g>
</svg>`
};



window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
