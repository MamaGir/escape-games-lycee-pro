# -*- coding: utf-8 -*-
# Génère matieres-premieres/README.md à partir des données JSON (solutions toujours à jour).
# Lancement depuis la racine du dépôt : python matieres-premieres/tests/generer-readme.py
import json, sys, re, os
R = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(R + "/assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open(R + "/assets/data/dialogues.json", encoding="utf-8"))
URL = "matieres-premieres/"   # adresse relative : remplacer par l'adresse GitHub Pages une fois le dépôt publié

def propre(s):
    return re.sub(r"<[^>]+>", "", s).strip()

def solution(e, niv):
    d = e.get(niv.lower()) or e.get("commun") or {}
    t = e["type"]
    L = []
    if t == "qcm":
        for q in d["questions"]:
            L.append(f"- {propre(q['q'])} → **{propre(q['options'][q['bonne']])}**")
    elif t == "vraifaux":
        for a in d["affirmations"]:
            L.append(f"- {propre(a['txt'])} → **{'Vrai' if a['vrai'] else 'Faux'}**")
    elif t == "association":
        for p in d["paires"]:
            L.append(f"- {p['g']} → **{p['d']}**")
    elif t == "ordre":
        for it in sorted(d["items"], key=lambda x: x["rang"]):
            L.append(f"{it['rang']}. {it['txt']}" + (f" ({it['sous']})" if it.get("sous") else ""))
    elif t == "tri":
        cols = {c["id"]: c["titre"] for c in d["colonnes"]}
        for cid, titre in cols.items():
            L.append(f"- **{titre}** : " + " ; ".join(c["txt"] for c in d["cartes"] if c["col"] == cid))
    elif t == "trous":
        reps = re.findall(r"\[\[(.+?)\]\]", d["texte"])
        L.append("Mots attendus, dans l'ordre : **" + "**, **".join(reps) + "**")
        trop = [x for x in d.get("etiquettes", []) if x not in reps]
        if trop: L.append(f"Étiquettes en trop : {', '.join(trop)}")
    elif t == "lettres":
        L.append("Lettres à cliquer dans l'ordre : **" + " ".join(d["cible"]) + "**")
    elif t == "code":
        for c in d["champs"]:
            L.append(f"- {c['libelle']} → **{c['valeur']}**")
    elif t == "intrus":
        L.append("Intrus : **" + next(c["txt"] for c in d["cartes"] if c["intrus"]) + "**")
    elif t == "instrument":
        for it in d["items"]:
            L.append(f"- {it['libelle']} ({'lire' if it['mode']=='lire' else 'régler'}) → **{it['valeur']} {d.get('unite','')}**")
    elif t == "plan":
        for c in d["cases"]:
            L.append(f"- {propre(c['libelle'])} → **{c['reponse']}**")
    return "\n".join(L)



NIV = {"CM1": "Essentiel", "CM2": "Expert"}
NOTION = {1: "Pourquoi préparer, analyser le terrain, extraire", 2: "Pourrissement et maturation", 3: "Machines à broyer l'argile",
          4: "Tamisage, déferrage, flottation, sécurité", 5: "Feldspath, sable de silice, chamotte"}
out = []
w = out.append
w("# Le bon de lancement\n")
w("**Escape game de technologie céramique — CAP Décoration sur céramique — La préparation des matières premières**  ")
w("45 à 60 minutes · équipes de 3-4 élèves · **15 énigmes au niveau Essentiel, 20 au niveau Expert**.\n")
w("> *Manufacture des Trois Fours (inventée), lundi matin.* Un nouveau lot de pâte doit être lancé demain, mais le bon de lancement")
w("> n'est pas signé. Maëlle, apprentie de 2e année, guide l'équipe de la carrière au laboratoire : chacun des cinq responsables")
w("> appose son tampon et donne un mot si l'équipe maîtrise son étape ; les cinq mots ouvrent le coffre du bon de lancement.\n")
w("Contenu : le cours « Préparation des matières premières des pâtes céramiques » (CAP, version allégée) de l'enseignant, couvert intégralement.\n")
w("| | |\n|---|---|")
w("| ▶ **Jouer** | version classique : `matieres-premieres/` · version immersive : `immersifs/matieres-premieres/` · en local avec `lancer.bat` |")
w("| 📖 **Leçons A4** | `lecons-imprimables.html` (Essentiel ou Expert) |")
w("| 👨‍🏫 **Tableau de bord** | http://127.0.0.1:8000/matieres-premieres/prof.html — mode local |")
w("| 📖 **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) |")
w("| ⚠️ **Points à contrôler** | [A-VERIFIER.md](A-VERIFIER.md) |\n\n---\n")
w("## Les 5 salles\n")
w("| # | Lieu | Notion | Personnage | Mot-clé | Énigmes | Tester |\n|---|---|---|---|---|---|---|")
for s in D["salles"]:
    p = s["dialogue_intro"]["nom"]
    w(f"| {s['num']} | {s['titre']} | {NOTION[s['num']]} | {p} | **{s['motCle']}** | 3 Essentiel · 4 Expert | [Essentiel]({URL}?salle={s['num']}&niveau=CM1) · [Expert]({URL}?salle={s['num']}&niveau=CM2) |")
w(f"| 🏁 | Fin : coffre, bon de lancement signé, quizz | | Maëlle | | 5 questions | [Essentiel]({URL}?salle=6&niveau=CM1) · [Expert]({URL}?salle=6&niveau=CM2) |\n")
w("Phrase-bilan du coffre : **« On ANALYSE le terrain, on laisse l'argile REPOSER, on la BROIE, on l'ÉPURE, et on CONCASSE les roches : la pâte est alors stable et de qualité constante. »**\n")
w("Dans les adresses, `niveau=CM1` correspond au niveau Essentiel et `niveau=CM2` au niveau Expert (clés internes du moteur).\n\n---\n")
w("## Énigmes et solutions\n")
w("<details>\n<summary>⚠️ Solutions — à ne pas projeter en classe</summary>\n")
for se in E["salles"]:
    w(f"### Salle {se['num']} — {se['titre']}\n")
    for e in se["enigmes"]:
        nivs = e.get("niveaux") or ["CM1", "CM2"]
        w(f"#### {e['id']} · {e['titre']} — type `{e['type']}` — {' et '.join(NIV[n] for n in nivs)}\n")
        if len(nivs) == 2 and ("cm1" in e) and ("cm2" in e):
            w("**Essentiel**\n\n" + solution(e, "CM1") + "\n\n**Expert**\n\n" + solution(e, "CM2") + "\n")
        else:
            w(solution(e, nivs[0]) + "\n")
        w(f"*Correction :* {propre(e['correction'])}  \n*Source :* {e['source']} · *Leçon :* `{e['lecon']}`\n")
w("</details>\n\n---\n")
w("## Types d'énigmes utilisés\n")
w("| Type | Énigmes |\n|---|---|")
from collections import defaultdict
T = defaultdict(list)
for se in E["salles"]:
    for e in se["enigmes"]:
        T[e["type"]].append(e["id"] + ("*" if e.get("niveaux") else ""))
for t in E["metadata"]["types"]:
    w(f"| `{t}` | {', '.join(T[t])} |")
w("\n\\* énigme réservée au niveau Expert.\n\n---\n")
w(open(os.path.join(R, "tests", "readme-suite.md"), encoding="utf-8").read())
open(os.path.join(R, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("README.md écrit :", sum(len(x) for x in out), "caractères")
