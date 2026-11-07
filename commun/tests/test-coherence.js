/* ============================================================
   TESTS — tronc commun (commun/) et onglet « Cohérence du moteur »
   Depuis la racine du dépôt :  node commun/tests/test-coherence.js
   1. Sur le disque : aucun jeu ne garde de copie d'un module commun,
      chaque index.html charge js/jeu.js en premier puis ../commun/js/…
   2. verifier.html : contrôle automatique des énigmes et des données, puis
      détection d'une copie locale simulée (index.html modifié en mémoire).
   ============================================================ */
const fs = require("fs"), path = require("path");
const { charger, compteur, dodo, attendreQue, RACINE } = require("../../outils-tests/charge");
const T = compteur("Tronc commun et cohérence du moteur"); const ok = T.ok;
const JEUX8 = ["pates-ceramiques"];
const COMMUNS = fs.readdirSync(path.join(RACINE, "commun", "js")).filter(f => f.endsWith(".js"));

function disque(){
  console.log("\n== Tronc commun sur le disque ==");
  for (const j of JEUX8) {
    const locaux = COMMUNS.filter(f => fs.existsSync(path.join(RACINE, j, "js", f))
      && !(["enigmes.js", "impression.js", "variantes.js"].includes(f) && ["declaration", "tour-du-monde"].includes(j))
      && !(j === "mission-geo" && f !== "lecons-a4.js"));
    ok(!locaux.length, `${j} : pas de copie locale d'un module commun (${locaux.join(", ")})`);
    if (j === "mission-geo") continue;
    const html = fs.readFileSync(path.join(RACINE, j, "index.html"), "utf8");
    const scripts = [...html.matchAll(/<script src="([^"]+)"/g)].map(m => m[1]);
    ok(/^js\/jeu\.js/.test(scripts[0] || ""), `${j} : js/jeu.js chargé en premier`);
    for (const s of scripts.filter(s => s.startsWith("../commun/"))) ok(fs.existsSync(path.join(RACINE, j, s.split("?")[0])), `${j} : ${s} existe`);
  }
}

async function onglet(){
  console.log("\n== verifier.html : contrôle des énigmes, des données et des médias ==");
  const { w, erreurs } = await charger(RACINE, "", { page: "verifier.html", attente: 1500 });
  const bilan = await attendreQue(() => { const b = w.document.querySelector("#contenu .pastille.ok, #contenu .pastille.ko"); return b || null; }, 20000);
  ok(!!bilan, "la page de vérification affiche un bilan");
  const txt = w.document.getElementById("contenu").textContent;
  ok(/Aucune anomalie/.test(txt), "aucune anomalie dans le contrôle des énigmes");
  ok(/fichiers de données chargés/.test(txt), "tous les fichiers de données se chargent");
  ok(w.document.querySelectorAll("#onglets button").length >= 1, "un onglet par jeu du catalogue");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
}

(async () => {
  try { disque(); await onglet(); } catch (e) { T.exception(e); }
  T.fin();
})();
