#!/usr/bin/env python3
"""Complète les brouillons de la variante immersive « Les fiches du four » après migrer-jeu.py.

    python outils/immersif/completer-pates-ceramiques.py immersifs/pates-ceramiques

Écrit : décors dessinés de secours (js/decors-secours.js, format 16:9, repris des décors du jeu classique),
zones cliquables nommées (decors-fx.json), et pour chaque énigme : personnage émetteur, problème narratif,
enjeu, raison du savoir ici, réaction du décor, réplique du personnage pour chaque grade.
Relancer ensuite : python immersifs/pates-ceramiques/outils/embarquer-donnees.py (si présent) et le test.
"""
import json, os, subprocess, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEST = os.path.join(RACINE, sys.argv[1] if len(sys.argv) > 1 else "immersifs/pates-ceramiques")
DATA = os.path.join(DEST, "assets", "data")
DECORS = ["magasin", "laboratoire", "reserve", "preparation", "four"]
MURS = {"magasin": "#d9e4ee", "laboratoire": "#e9f2f8", "reserve": "#cdd6de", "preparation": "#dfe7ee", "four": "#2a3644"}
PERSO = ["ines", "theo", "awa", "lucas", "ferrand"]

# Zones : (libellé, x, y, w, h, description) en % de l'image 16:9 ; l'ordre suit les énigmes 1 à 4 de la salle.
ZONES = {
    "magasin": [("Les étiquettes des sacs", 7.5, 46, 16, 40, "Une palette de kaolin : les étiquettes des sacs se sont décollées."),
                ("Les deux rayons", 29, 46, 37, 40, "Deux rayons de sacs, à trier entre matières plastiques et non plastiques."),
                ("Le carnet d'Inès", 86, 49, 11, 27, "La tablette où Inès note ce qu'elle vérifie."),
                ("La fiche de fabrication", 71, 46, 15, 40, "Une fiche de fabrication à moitié remplie, posée sur les sacs de sable.")],
    "laboratoire": [("Le tableau des minéraux", 5, 40, 37.5, 27, "Trois noms de minéraux et trois barres de plasticité."),
                    ("Le microscope", 56, 46, 12, 30, "Une lame d'argile sous l'objectif."),
                    ("Les coupelles d'échantillons", 7, 66, 34, 12, "Cinq coupelles numérotées : d'où viennent ces argiles ?"),
                    ("Le tiroir des échantillons", 79, 59, 12, 18, "Le tiroir « argiles secondaires »… un échantillon n'est pas à sa place.")],
    "reserve": [("Les bacs sans étiquette", 7.5, 68, 31, 20, "Des bacs d'argile humide, rouges, blancs, beiges."),
                ("Le rayonnage", 54, 39, 42.5, 37, "Six étagères vides d'étiquettes."),
                ("Les commandes du jour", 57, 90, 38, 9, "Les bons de commande tombés au sol."),
                ("L'armoire à cadenas", 42, 68, 14, 19, "Le bac de la dernière livraison, fermé par un cadenas à molettes.")],
    "preparation": [("Les quatre bacs", 35, 76, 47, 12, "Quatre bacs de dégraissants à remplir."),
                    ("Le malaxeur", 8.5, 55, 18, 34, "Le malaxeur où la pâte prend forme."),
                    ("L'armoire des fondants", 80, 46, 15, 42, "Une armoire grillagée, pictogramme « toxique »."),
                    ("Les étiquettes des bacs", 35, 66, 47, 10, "Le rôle de chaque bac, à recopier sur son étiquette.")],
    "four": [("Le grand four", 41, 42, 33, 45, "Le four électrique, son regard orange."),
             ("Le pyromètre", 8.5, 43, 16, 17, "L'écran qui affiche la température du four."),
             ("Les pièces à enfourner", 78, 62, 14, 22, "Des pièces crues de plusieurs familles de pâtes."),
             ("Le cahier de recettes", 11, 75, 11, 13, "Le cahier de recettes taché d'huile.")]
}

# Narration : par énigme (id) → (problème, enjeu, pourquoi ici, effet, réaction, réplique Essentiel, réplique Expert)
N = {
 "e1-1": ("Les sacs de la palette ont perdu leurs étiquettes de vocabulaire.", "Sans les bons mots, Inès ne peut pas préparer le bon de sortie.",
          "On ne commande pas une matière dont on ne connaît pas le nom.", "eclat", "Les étiquettes se recollent une à une sur les sacs.",
          "Commencez par les mots du métier : relie chaque mot à sa définition.", "Six mots, six définitions. À l'atelier, on parle juste."),
 "e1-2": ("Un livreur a mélangé les sacs des deux rayons.", "Une pâte avec un sac de sable à la place de l'argile ne se modèle pas.",
          "Le magasin range les matières selon leur rôle dans la pâte.", "ouverture", "Les deux rayons s'allument : chaque sac est à sa place.",
          "Remettez chaque sac dans son rayon : celles qui se modèlent, et les autres.", "Dix sacs. Plastique ou non plastique ? Pas de place pour l'hésitation."),
 "e1-3": ("Inès a noté des phrases, mais certaines sont fausses.", "Une fausse règle dans le carnet, et toute une fournée est ratée.",
          "Le carnet d'Inès sert de référence à tout l'atelier.", "calme", "La tablette affiche une coche verte à chaque phrase vérifiée.",
          "Mon carnet contient des erreurs. Vrai ou faux ?", "Vérifiez mes cinq phrases : je recopie seulement les vraies."),
 "e1-4": ("La fiche de fabrication est à moitié effacée.", "Sans fiche complète, personne ne sait doser la pâte.",
          "La fiche de fabrication résume ce qu'est une pâte céramique.", "lumiere", "La fiche se complète et rejoint le cahier.",
          "", "La fiche de fabrication a des trous. Deux étiquettes sont des pièges."),
 "e2-1": ("Le tableau des minéraux a été effacé par le chiffon du ménage.", "Théo ne peut pas classer ses échantillons sans cette échelle.",
          "La plasticité d'une argile dépend de ses minéraux.", "lumiere", "Les trois barres du tableau se remplissent dans le bon ordre.",
          "Aidez-moi à remettre les trois minéraux dans l'ordre.", "Du moins plastique au plus plastique, sans repères cette fois."),
 "e2-2": ("Théo veut vérifier que vous savez ce que vous regardez au microscope.", "Il ne confie pas son laboratoire à quelqu'un qui confond minéral et argile.",
          "Le microscope montre les particules qui composent l'argile.", "eclat", "La lame s'éclaire sous l'objectif.",
          "Trois questions, et je vous laisse regarder.", "Trois questions précises : qu'est-ce qu'une argile, au juste ?"),
 "e2-3": ("Les coupelles sont mélangées : primaires et secondaires ensemble.", "Un mauvais classement fausse toutes les recettes.",
          "L'origine d'une argile explique sa plasticité.", "ouverture", "Les coupelles se rangent en deux rangées.",
          "Restée sur place ou voyageuse ? Rangez les étiquettes.", "Huit étiquettes, attention aux phrases : elles décrivent autant que les noms."),
 "e2-4": ("Un échantillon s'est glissé dans le mauvais tiroir.", "Si l'intrus reste là, la prochaine commande sera fausse.",
          "Une seule argile du chapitre est primaire.", "calme", "Le tiroir se referme proprement.",
          "", "Un de ces échantillons n'a rien à faire dans le tiroir des argiles secondaires."),
 "e3-1": ("Les bacs d'argile n'ont plus d'étiquette.", "Awa ne peut rien livrer tant qu'elle ne sait pas ce qu'il y a dedans.",
          "La couleur est le premier indice pour reconnaître une argile.", "eclat", "Chaque bac reçoit sa plaque.",
          "Regardez les couleurs : quelle argile est dans chaque bac ?", "Reliez chaque argile à ce qui la distingue vraiment."),
 "e3-2": ("Les six étagères sont vides.", "L'atelier attend ses argiles pour la journée.",
          "Chaque argile a ses usages : c'est ainsi qu'on les range.", "ouverture", "Le rayonnage se remplit, étagère par étagère.",
          "Placez chaque argile sur l'étagère de son usage.", "Six étagères, deux étiquettes en trop. Réfléchissez aux usages."),
 "e3-3": ("Trois commandes attendent une réponse.", "Une mauvaise argile, et la commande revient.",
          "Choisir une argile, c'est connaître ses propriétés.", "lumiere", "Les bons de commande se tamponnent « validé ».",
          "Pour chaque commande, quelle argile ?", "Trois commandes délicates : répondez comme une professionnelle ou un professionnel."),
 "e3-4": ("Le bac de la dernière livraison est fermé par un cadenas.", "Sans l'ouvrir, la réserve reste incomplète.",
          "Deux nombres du chapitre ouvrent le cadenas.", "ouverture", "Le cadenas s'ouvre avec un déclic.",
          "", "Deux molettes : une température et un nombre du laboratoire."),
 "e4-1": ("Les dégraissants sont dans des sacs sans nom.", "Un mauvais bac, et la pâte se fissure au séchage.",
          "Chaque type de dégraissant a son rôle.", "ouverture", "Les quatre bacs se remplissent.",
          "Rangez chaque matière dans son bac.", "Neuf matières, quatre bacs : simples, siliceux, combustibles, fondants."),
 "e4-2": ("Lucas explique son métier, mais il teste votre attention.", "Il ne laisse pas toucher le malaxeur à quelqu'un qui ignore le rôle du dégraissant.",
          "Le dégraissant change le comportement de la pâte.", "calme", "Le malaxeur ralentit, la pâte est prête.",
          "À quoi sert un dégraissant ? Vrai ou faux ?", "Cinq affirmations : certaines sont des pièges classiques."),
 "e4-3": ("L'armoire des fondants contient des poudres au plomb.", "Un geste dangereux peut rendre malade.",
          "La sécurité passe avant tout dans la salle de préparation.", "lumiere", "Le voyant de l'armoire passe au vert.",
          "Un seul de ces gestes est dangereux. Lequel ?", "Trouvez le geste qui ne protège pas du plomb."),
 "e4-4": ("Les étiquettes des bacs doivent indiquer leur rôle.", "Sans rôle écrit, les apprentis se trompent de bac.",
          "Connaître le rôle, c'est choisir le bon dégraissant.", "eclat", "Les étiquettes s'impriment et se collent.",
          "", "Reliez chaque type de dégraissant à son rôle exact."),
 "e5-1": ("Le programme de cuisson est vide.", "Sans ordre de température, le four ne démarre pas.",
          "Chaque famille de pâte cuit à sa température.", "lumiere", "Le regard du four rougeoie davantage.",
          "Rangez ces pâtes de la moins chaude à la plus chaude.", "Sans repères : de la cuisson la moins chaude à la plus chaude."),
 "e5-2": ("Le pyromètre doit être vérifié avant la fournée.", "Une erreur de 100 °C peut faire fondre ou laisser crue la vaisselle.",
          "Lire et régler une température fait partie du métier.", "eclat", "L'écran du pyromètre clignote, puis se stabilise.",
          "Lisez les températures sur le pyromètre.", "Lisez la première, puis réglez le pyromètre pour le grès et le raku."),
 "e5-3": ("Des pièces crues attendent, sans étiquette de famille.", "Une pièce dans la mauvaise fournée est perdue.",
          "On reconnaît une famille de pâte à sa composition et à son aspect.", "calme", "Les pièces se rangent sur les plaques d'enfournement.",
          "Qui suis-je ? Retrouvez chaque famille de pâte.", "Je décris trois pâtes sans les nommer. À vous."),
 "e5-4": ("Le cahier de recettes est taché d'huile.", "Sans recette, impossible de préparer le lot de demain.",
          "Une recette se lit en pourcentages, et le total fait toujours 100 %.", "ouverture", "Les chiffres réapparaissent sous la tache.",
          "", "Retrouvez les nombres cachés : pourcentages et pesée."),
}


def lire(n):
    with open(os.path.join(DATA, n), encoding="utf-8") as f:
        return json.load(f)


def ecrire(n, d):
    with open(os.path.join(DATA, n), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


def decors_secours():
    """Reprend les décors SVG du jeu classique (800×300) et les élargit en 16:9 (800×450) sans rien couper."""
    js = os.path.join(RACINE, "pates-ceramiques", "js", "decors.js")
    code = ("global.window={};" + open(js, encoding="utf-8").read() +
            ";process.stdout.write(JSON.stringify(SVG_DECORS));")
    svgs = json.loads(subprocess.run(["node", "-e", code], capture_output=True, text=True, check=True).stdout)
    out = ["/* Décors dessinés de secours (16:9) — générés par outils/immersif/completer-pates-ceramiques.py",
           "   à partir des décors du jeu classique. Une image déposée dans assets/images/decors/<id>.webp|.jpg|.png les remplace. */",
           "var VML = window.VML || (window.VML = {});", "VML.SVG_DECORS = VML.SVG_DECORS || {};"]
    for d in DECORS:
        s = svgs[d].replace('viewBox="0 0 800 300"', 'viewBox="0 -150 800 450"', 1)
        i = s.index(">") + 1
        s = s[:i] + f'<rect x="0" y="-150" width="800" height="150" fill="{MURS[d]}"/>' + s[i:]
        if d == "four":
            s = s.replace("</svg>", '<g transform="translate(130,210)"><rect x="-38" y="-26" width="76" height="48" rx="3" fill="#f3f8fd" stroke="#2f75b5" stroke-width="3"/>'
                                     '<g stroke="#9fb0c0" stroke-width="2"><line x1="-28" y1="-12" x2="28" y2="-12"/><line x1="-28" y1="0" x2="28" y2="0"/><line x1="-28" y1="12" x2="10" y2="12"/></g>'
                                     '<ellipse cx="14" cy="6" rx="14" ry="9" fill="#c9a24a" opacity=".55"/></g></svg>')
        out.append(f"VML.SVG_DECORS[{json.dumps(d)}] = {json.dumps(s, ensure_ascii=False)};")
    with open(os.path.join(DEST, "js", "decors-secours.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")


def main():
    decors_secours()
    fx = lire("decors-fx.json")
    for d in DECORS:
        z = []
        for k, (lib, x, y, w, h, desc) in enumerate(ZONES[d]):
            z.append({"id": f"objet-{k+1}", "libelle": lib, "x": x, "y": y, "w": w, "h": h, "description": desc})
        fx["decors"][d]["zones"] = z
        fx["decors"][d]["ambiance"] = ["vent"]
    ecrire("decors-fx.json", fx)

    e = lire("enigmes.json")
    for s in e["escales"]:
        n = s["numero"]
        for en in s["enigmes"]:
            p, enj, pq, eff, rea, d1, d2 = N[en["id"]]
            en["personnage_emetteur"] = PERSO[n - 1]
            en["objet_principal"] = f"objet-{en['ordre']}"
            en["probleme_narratif"] = p
            en["enjeu"] = enj
            en["pourquoi_ce_savoir_ici"] = pq
            en["reaction_du_decor"] = {"effet": eff, "description": rea}
            en["liberte_ou_anachronisme"] = "Manufacture et personnages inventés ; toutes les données techniques viennent du chapitre du cours."
            en["niveau_variantes"] = "Essentiel (grade matelot) : repères et données réduites. Expert (grade timonier) : sans repères, plus de cartes, calculs."
            if "matelot" in en and d1:
                en["matelot"]["dialogue"] = d1
            if "timonier" in en and d2:
                en["timonier"]["dialogue"] = d2
            en["_brouillon"] = [b for b in en.get("_brouillon", []) if b == "zones"]
            if not en["_brouillon"]:
                en.pop("_brouillon")
    ecrire("enigmes.json", e)
    print("✔ brouillons complétés : décors 16:9, 20 zones, 20 énigmes (narration, réactions, répliques).")


if __name__ == "__main__":
    main()
