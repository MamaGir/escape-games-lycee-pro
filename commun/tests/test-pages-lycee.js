/* ============================================================
   PAGES DU LYCÉE PRO — test de fumée
   ------------------------------------------------------------
   Charge chaque page racine dans jsdom (sans réseau) et contrôle : aucune erreur JavaScript,
   un tableau « jeu par jeu » alimenté par le catalogue (espace enseignant), libellés
   Essentiel / Expert (jamais CM1 / CM2 à l'écran), et lien du portail vers chaque jeu.
   Lancer :  node commun/tests/test-pages-lycee.js
   ============================================================ */
const fs = require("fs"), path = require("path");
const { charger, compteur, attendreQue, RACINE } = require("../../outils-tests/charge");
const T = compteur("Pages du lycée pro"); const ok = T.ok;
const PAGES = ["index.html", "enseignant.html", "resultats.html", "classement.html", "passeport.html", "trophees.html", "verifier.html"];

(async () => {
  try {
    const cat = fs.readFileSync(path.join(RACINE, "commun", "donnees", "catalogue.js"), "utf8");
    const dossiers = [...cat.matchAll(/"dossier":\s*"([^"]+)"/g)].map(m => m[1]);
    ok(dossiers.length >= 1, "le catalogue contient au moins un jeu (" + dossiers.join(", ") + ")");
    for (const p of PAGES) {
      console.log("\n== " + p + " ==");
      ok(fs.existsSync(path.join(RACINE, p)), p + " existe");
      const { w, erreurs } = await charger(RACINE, "", { page: p, attente: 1200 });
      ok(erreurs.length === 0, p + " : erreurs JS : " + erreurs.join(" | "));
      const copie = w.document.body.cloneNode(true);
      copie.querySelectorAll("script, style, textarea, code").forEach(n => n.remove());
      const visible = copie.textContent, trouve = (visible.match(/.{0,30}\b(CM[12]|cycle 3)\b.{0,30}/g) || []).filter(t => !/repris/.test(t));   // mention de provenance du moteur : voulue
      ok(!trouve.length, p + " : pas de CM1 / CM2 affiché" + (trouve.length ? " → " + trouve.slice(0, 3).join(" | ") : ""));
      if (p === "enseignant.html") {
        const lignes = await attendreQue(() => { const l = w.document.querySelectorAll("#corps-jeux tr"); return l.length ? l : null; }, 5000);
        ok(lignes && lignes.length === dossiers.length, "enseignant : une ligne par jeu du catalogue (" + (lignes ? lignes.length : 0) + ")");
        const liens = [...w.document.querySelectorAll("#corps-jeux a")].map(a => a.getAttribute("href"));
        ok(dossiers.every(d => liens.includes(d + "/") && liens.includes(d + "/prof.html")), "enseignant : liens jouer et tableau de bord pour chaque jeu");
        ok(!/adopter|annee\.html|periode\.html|faq\.html|presentation\//.test(w.document.documentElement.innerHTML), "enseignant : aucun lien vers une page de l'école");
      }
      if (p === "index.html") {
        const liens = [...w.document.querySelectorAll("a")].map(a => a.getAttribute("href") || "");
        ok(dossiers.every(d => liens.some(h => h.includes(d))), "portail : un lien vers chaque jeu");
      }
    }
  } catch (e) { T.exception(e); }
  T.fin();
})();
