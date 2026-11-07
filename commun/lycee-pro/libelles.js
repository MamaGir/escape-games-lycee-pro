/* ============================================================
   LIBELLÉS LYCÉE PRO — à charger EN DERNIER dans chaque page.
   ------------------------------------------------------------
   Le moteur commun (hérité des escape games de l'école) garde ses
   clés internes « CM1 » / « CM2 » (données, sauvegardes, synchronisation).
   Ce script ne change que le TEXTE AFFICHÉ :
     CM1 → Essentiel     CM2 → Expert
   Il ne touche ni aux attributs data-*, ni aux valeurs des champs,
   ni au contenu des balises <script> / <style>.
   Pour d'autres noms de niveaux : modifier NIVEAUX_LYCEE ci-dessous.
   ============================================================ */
(function(){
  var NIVEAUX_LYCEE = { "CM1": "Essentiel", "CM2": "Expert" };
  var REMPLACEMENTS = [
    [/\bCM1\s*[-–·\/]\s*CM2\b/g, NIVEAUX_LYCEE.CM1 + " · " + NIVEAUX_LYCEE.CM2],
    [/\bles CM1 et les CM2\b/g, "les niveaux " + NIVEAUX_LYCEE.CM1 + " et " + NIVEAUX_LYCEE.CM2],
    [/\ben CM1\b/g, "au niveau " + NIVEAUX_LYCEE.CM1],
    [/\ben CM2\b/g, "au niveau " + NIVEAUX_LYCEE.CM2],
    [/\bCM1\b/g, NIVEAUX_LYCEE.CM1],
    [/\bCM2\b/g, NIVEAUX_LYCEE.CM2],
    [/\bcycle 3\b/g, "CAP"]
  ];
  var ATTRIBUTS = ["title", "placeholder", "aria-label", "alt"];
  var IGNORER = { SCRIPT:1, STYLE:1, TEXTAREA:1, CODE:1 };

  function traduire(t){
    if(!t || !/CM[12]|cycle 3/.test(t)) return t;
    for(var i = 0; i < REMPLACEMENTS.length; i++) t = t.replace(REMPLACEMENTS[i][0], REMPLACEMENTS[i][1]);
    return t;
  }
  function traiterNoeud(racine){
    if(!racine) return;
    if(racine.nodeType === 3){
      var p = racine.parentNode;
      if(p && !IGNORER[p.nodeName]){ var n = traduire(racine.nodeValue); if(n !== racine.nodeValue) racine.nodeValue = n; }
      return;
    }
    if(racine.nodeType !== 1 || IGNORER[racine.nodeName]) return;
    ATTRIBUTS.forEach(function(a){
      var v = racine.getAttribute && racine.getAttribute(a);
      if(v){ var n = traduire(v); if(n !== v) racine.setAttribute(a, n); }
    });
    var w = document.createTreeWalker(racine, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, null);
    var noeud;
    while((noeud = w.nextNode())){
      if(noeud.nodeType === 3) traiterNoeud(noeud);
      else if(!IGNORER[noeud.nodeName]) ATTRIBUTS.forEach(function(a){
        var v = noeud.getAttribute(a);
        if(v){ var n = traduire(v); if(n !== v) noeud.setAttribute(a, n); }
      });
    }
  }
  window.LIBELLES_LYCEE = { niveaux: NIVEAUX_LYCEE, traduire: traduire };
  function demarrer(){
    traiterNoeud(document.body);
    if(document.title) document.title = traduire(document.title);
    if(typeof MutationObserver === "function"){
      new MutationObserver(function(muts){
        muts.forEach(function(m){
          if(m.type === "characterData") traiterNoeud(m.target);
          else m.addedNodes.forEach(traiterNoeud);
        });
      }).observe(document.body, { childList:true, subtree:true, characterData:true });
    }
  }
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer);
  else demarrer();
})();
