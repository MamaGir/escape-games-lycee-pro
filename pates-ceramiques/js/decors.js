/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de « Les fiches du four »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux (Amboise, printemps 1518) :
     imprimerie  l'imprimerie de Maître Jacquet
     salle       la grande salle du château, tapisseries et salamandres
     atelier     l'atelier de Léonard au manoir du Cloux
     plans       le cabinet des plans des châteaux
     galerie     la galerie des tableaux, en perspective
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["magasin"];
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

const SALLE_NUM = { "magasin":1, "laboratoire":2, "reserve":3, "preparation":4, "four":5 };

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
const OISEAUX = `
  <g stroke="#3a3a3a" stroke-width="1.6" fill="none" opacity=".7">
    <path d="M0 0 q5 -5 10 0 q5 -5 10 0"><animateMotion dur="40s" repeatCount="indefinite" path="M-40 60 L840 34"/></path>
    <path d="M0 0 q4 -4 8 0 q4 -4 8 0"><animateMotion dur="46s" repeatCount="indefinite" path="M-80 80 L860 52"/></path>
  </g>`;
/* Flamme de bougie animée (x, y) */
const flamme = (x, y) => `<g transform="translate(${x},${y})"><rect x="-3" y="0" width="6" height="18" fill="#f3ecd8" stroke="#c9b98f" stroke-width=".6"/>
  <path d="M0 -12 Q5 -4 0 0 Q-5 -4 0 -12 Z" fill="#ffb23c"><animateTransform attributeName="transform" type="scale" values="1 1;1 1.25;.95 1;1 1.15;1 1" dur="1.3s" repeatCount="indefinite"/></path>
  <circle cy="-5" r="12" fill="#ffd27a" opacity=".22"><animate attributeName="opacity" values=".15;.3;.18;.28;.15" dur="1.6s" repeatCount="indefinite"/></circle></g>`;

const SALAMANDRE = (x, y, s=1, c="#c9a227") => `<g transform="translate(${x},${y}) scale(${s})"><path d="M-30 4 Q-18 -10 0 -4 Q16 2 26 -8 Q30 -2 22 4 Q8 12 -6 8 Q-20 6 -30 12 Z" fill="${c}"/>
  <g stroke="${c}" stroke-width="2.4"><line x1="-14" y1="2" x2="-18" y2="10"/><line x1="-2" y1="4" x2="2" y2="12"/></g>
  <g fill="#e08a1e" opacity=".8"><path d="M-26 16 q3 -10 6 0 q3 -9 6 0 q3 -10 6 0 q3 -9 6 0 q3 -10 6 0 q3 -9 6 0 Z"><animate attributeName="opacity" values=".55;.95;.6;.9;.55" dur="1.6s" repeatCount="indefinite"/></path></g></g>`;
const F_COURONNE = (x, y, c="#c9a227") => `<g transform="translate(${x},${y})"><path d="M-12 -14 l4 6 l4 -8 l4 8 l4 -8 l4 8 l4 -6 l0 8 l-24 0 Z" fill="${c}"/>
  <text y="16" text-anchor="middle" font-family="Georgia,serif" font-size="24" font-weight="bold" fill="${c}">F</text></g>`;

const SVG_DECORS = {

/* SALLE 1 — Le magasin des matières premières : palettes de sacs, étagères, néons */
"magasin": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs><linearGradient id="murM" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d9e4ee"/><stop offset="100%" stop-color="#b7c7d6"/></linearGradient></defs>
  <rect width="800" height="300" fill="url(#murM)"/><rect y="238" width="800" height="62" fill="#6f7c88"/>
  <g stroke="#9fb0c0" stroke-width="2">${[0,1,2,3,4,5,6,7].map(i=>`<line x1="${i*110}" y1="238" x2="${i*110-40}" y2="300"/>`).join("")}</g>
  <g>${[150,400,650].map(x=>`<rect x="${x-60}" y="14" width="120" height="6" rx="3" fill="#f4fbff"><animate attributeName="opacity" values="1;.85;1;1;.9;1" dur="5s" repeatCount="indefinite"/></rect>`).join("")}</g>
  ${[[60,"#efe7d6"],[230,"#d9c7a4"],[400,"#c96e4a"],[570,"#e8e8e8"]].map(([x,c],k)=>`<g transform="translate(${x},0)">
     <rect x="0" y="226" width="130" height="12" fill="#a57a4a"/>
     ${[0,1,2].map(r=>[0,1].map(cc=>`<rect x="${6+cc*60}" y="${186-r*40}" width="56" height="38" rx="8" fill="${c}" stroke="#7d8a96" stroke-width="1.5"/><rect x="${18+cc*60}" y="${198-r*40}" width="32" height="12" fill="#fff" opacity=".8"/>`).join("")).join("")}
     <text x="65" y="80" text-anchor="middle" font-family="Segoe UI,Arial" font-size="13" font-weight="bold" fill="#0f4c81">${["KAOLIN","BALL CLAY","TERRE ROUGE","SABLE"][k]}</text></g>`).join("")}
  <g transform="translate(735,150)"><rect x="-22" y="-60" width="44" height="80" rx="4" fill="#0f4c81"/><rect x="-16" y="-52" width="32" height="20" fill="#9fd3ff"/><text y="0" text-anchor="middle" font-size="9" fill="#fff" font-family="Arial">25 kg</text></g>
</svg>`,

/* SALLE 2 — Le laboratoire : paillasse, microscope, coupelles, tableau */
"laboratoire": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <rect width="800" height="300" fill="#e9f2f8"/><rect y="250" width="800" height="50" fill="#9aaab8"/>
  <rect x="40" y="30" width="300" height="120" rx="4" fill="#ffffff" stroke="#2f75b5" stroke-width="4"/>
  <g font-family="Segoe UI,Arial" font-size="18" fill="#0f4c81"><text x="60" y="66">Kaolinite</text><text x="60" y="96">Illite</text><text x="60" y="126">Smectite</text></g>
  <g fill="#2f75b5"><rect x="190" y="54" width="40" height="14"/><rect x="190" y="84" width="80" height="14"/><rect x="190" y="114" width="130" height="14"/></g>
  <rect x="0" y="190" width="800" height="18" fill="#f7f9fb" stroke="#b7c7d6"/><rect x="20" y="208" width="760" height="42" fill="#cfdbe6"/>
  <g transform="translate(500,190)"><rect x="-40" y="-8" width="80" height="8" fill="#26303a"/><path d="M20 -8 C 40 -40 30 -80 0 -100" stroke="#26303a" stroke-width="10" fill="none"/>
    <rect x="-22" y="-120" width="18" height="60" rx="4" fill="#3a4654" transform="rotate(-20 -13 -90)"/><rect x="-30" y="-40" width="50" height="6" fill="#3a4654"/>
    <circle cx="-6" cy="-46" r="5" fill="#9fd3ff"><animate attributeName="r" values="4;6;4" dur="3s" repeatCount="indefinite"/></circle></g>
  ${[0,1,2,3,4].map(i=>`<g transform="translate(${80+i*60},176)"><ellipse rx="22" ry="7" fill="#fff" stroke="#7d8a96"/><ellipse rx="14" ry="4" fill="${["#f5f2ea","#e6dcc8","#c9a77a","#b5532f","#d7cfc2"][i]}"/><text y="-12" text-anchor="middle" font-size="9" font-family="Arial" fill="#0f4c81">E${i+1}</text></g>`).join("")}
  <g transform="translate(680,140)"><rect x="-30" y="0" width="60" height="50" rx="3" fill="#ffffff" stroke="#7d8a96"/><circle cx="0" cy="25" r="14" fill="#e9f2f8" stroke="#2f75b5" stroke-width="3"/></g>
</svg>`,

/* SALLE 3 — La réserve des argiles : bacs sous bâches, étagères, étiquettes tombées */
"reserve": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <rect width="800" height="300" fill="#cdd6de"/><rect y="244" width="800" height="56" fill="#8a7a66"/>
  ${[0,1,2].map(r=>`<rect x="430" y="${60+r*60}" width="340" height="8" fill="#5c6670"/>`).join("")}
  ${[0,1,2].map(r=>[0,1,2,3,4].map(c=>`<rect x="${440+c*66}" y="${28+r*60}" width="52" height="32" rx="4" fill="${["#f5f2ea","#e6dcc8","#c9a77a","#a8805a","#b5532f"][(c+r)%5]}" stroke="#5c6670"/>`).join("")).join("")}
  ${[[60,"#b5532f"],[200,"#f2efe8"],[340,"#c9a77a"]].map(([x,c])=>`<g transform="translate(${x},170)"><rect x="0" y="0" width="110" height="74" rx="6" fill="#3a4654"/><path d="M-6 6 Q55 -24 116 6 L110 20 Q55 -6 0 20 Z" fill="#2f75b5" opacity=".85"/><ellipse cx="55" cy="22" rx="46" ry="10" fill="${c}"/></g>`).join("")}
  ${[[470,268,-12],[560,276,8],[650,264,20],[720,280,-6]].map(([x,y,r])=>`<rect x="${x}" y="${y}" width="40" height="16" fill="#fff" stroke="#0f4c81" transform="rotate(${r} ${x+20} ${y+8})"/>`).join("")}
  <g fill="#7fb3e0" opacity=".7">${[120,260,390].map((x,i)=>`<circle cx="${x}" cy="170" r="2.5"><animate attributeName="cy" values="170;244" dur="${1.6+i*.4}s" repeatCount="indefinite"/></circle>`).join("")}</g>
</svg>`,

/* SALLE 4 — La salle de préparation : malaxeur, quatre bacs, armoire grillagée */
"preparation": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <rect width="800" height="300" fill="#dfe7ee"/><rect y="246" width="800" height="54" fill="#7a8794"/>
  <g transform="translate(140,140)"><rect x="-70" y="40" width="140" height="66" rx="8" fill="#2f75b5"/><path d="M-60 40 Q0 -10 60 40 Z" fill="#cfdbe6" stroke="#0f4c81" stroke-width="3"/>
    <g><rect x="-4" y="-40" width="8" height="70" fill="#3a4654"/><rect x="-30" y="20" width="60" height="6" fill="#3a4654"><animateTransform attributeName="transform" type="rotate" from="0 0 23" to="360 0 23" dur="3s" repeatCount="indefinite"/></rect></g></g>
  ${["Simples","Siliceux","Combustibles","Fondants"].map((t,i)=>`<g transform="translate(${280+i*95},196)"><rect x="0" y="0" width="80" height="50" rx="4" fill="#5c6670"/><ellipse cx="40" cy="4" rx="36" ry="7" fill="${["#c9a77a","#efe4c8","#d9b98a","#f4f1ea"][i]}"/><text x="40" y="34" text-anchor="middle" font-size="11" font-family="Segoe UI,Arial" fill="#fff">${t}</text></g>`).join("")}
  <g transform="translate(700,60)"><rect x="-56" y="0" width="112" height="186" fill="#c8d2db" stroke="#3a4654" stroke-width="3"/>
    <g stroke="#3a4654" stroke-width="1" opacity=".6">${[0,1,2,3,4,5,6,7,8,9].map(i=>`<line x1="${-56+i*12}" y1="0" x2="${-56+i*12}" y2="186"/>`).join("")}</g>
    <path d="M0 30 L22 68 L-22 68 Z" fill="#ffd400" stroke="#111" stroke-width="2"/><text x="0" y="62" text-anchor="middle" font-size="22" font-weight="bold" fill="#111">!</text></g>
</svg>`,

/* SALLE 5 — La halle des fours : four, regard incandescent, pyromètre */
"four": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <rect width="800" height="300" fill="#2a3644"/><rect y="244" width="800" height="56" fill="#3e4a58"/>
  <g transform="translate(330,40)"><rect x="0" y="0" width="260" height="204" rx="10" fill="#8a96a3" stroke="#1e2a36" stroke-width="4"/>
    <rect x="22" y="22" width="216" height="160" rx="6" fill="#5c6670"/><circle cx="130" cy="102" r="26" fill="#ff8a3d"><animate attributeName="fill" values="#ff8a3d;#ffb347;#ff7a2a;#ff8a3d" dur="2.4s" repeatCount="indefinite"/></circle>
    <circle cx="130" cy="102" r="44" fill="#ff8a3d" opacity=".18"><animate attributeName="opacity" values=".12;.26;.12" dur="2.4s" repeatCount="indefinite"/></circle>
    <rect x="236" y="70" width="14" height="60" rx="4" fill="#1e2a36"/></g>
  <g transform="translate(130,90)"><rect x="-60" y="-40" width="120" height="70" rx="6" fill="#0b1724" stroke="#2f75b5" stroke-width="3"/>
    <text x="0" y="6" text-anchor="middle" font-family="Consolas,monospace" font-size="24" fill="#ffb347">1280 °C<animate attributeName="opacity" values="1;.7;1" dur="2s" repeatCount="indefinite"/></text>
    <text x="0" y="22" text-anchor="middle" font-size="10" fill="#9fd3ff" font-family="Arial">PYROMÈTRE</text></g>
  <g transform="translate(680,150)">${[0,1,2,3].map(i=>`<rect x="-50" y="${i*24}" width="100" height="6" fill="#a57a4a"/><g>${[0,1,2].map(j=>`<path d="M${-40+j*32} ${i*24} q12 -16 24 0 z" fill="#f5f2ea"/>`).join("")}</g>`).join("")}</g>
  <path d="M0 0 L800 0 L800 30 Q400 60 0 30 Z" fill="#ff8a3d" opacity=".06"/>
</svg>`
};



window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
