#!/usr/bin/env python3
"""Complète les brouillons de la variante immersive « Le bon de lancement » après migrer-jeu.py.

    python outils/immersif/completer-matieres-premieres.py immersifs/matieres-premieres

Écrit : décors dessinés de secours (js/decors-secours.js, format 16:9, repris des décors du jeu classique),
zones cliquables nommées (decors-fx.json), et pour chaque énigme : personnage émetteur, problème narratif,
enjeu, raison du savoir ici, réaction du décor, réplique du personnage pour chaque grade.
Relancer ensuite : python immersifs/matieres-premieres/outils/embarquer-donnees.py puis le test.
"""
import json, os, subprocess, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEST = os.path.join(RACINE, sys.argv[1] if len(sys.argv) > 1 else "immersifs/matieres-premieres")
DATA = os.path.join(DEST, "assets", "data")
DECORS = ["carriere", "parc", "broyage", "epuration", "dures"]
MURS = {"carriere": "#cfe3f1", "parc": "#cfe3f1", "broyage": "#dfe7ee", "epuration": "#e1ebf3", "dures": "#e9f2f8"}
PERSO = ["odile", "malik", "karim", "jade", "aubry"]

# Zones : (libellé, x, y, w, h, description) en % de l'image 16:9 ; l'ordre suit les énigmes 1 à 4 de la salle.
ZONES = {
    "carriere": [("Le panneau des mots", 7, 44, 18, 24, "Un panneau de chantier : six mots du métier, six définitions effacées."),
                 ("Les gradins", 28, 62, 24, 28, "Les gradins de la carrière, où les panneaux de la filière ont été mélangés par le vent."),
                 ("L'engin d'Odile", 58, 58, 14, 28, "L'engin de la cheffe de carrière, avec son carnet posé sur le capot."),
                 ("La fiche d'analyse", 80, 58, 16, 30, "La fiche d'analyse du terrain, à moitié effacée.")],
    "parc": [("Le tas sous la pluie", 4, 60, 52, 30, "L'argile fraîchement sortie, qui pourrit dehors sous la pluie."),
             ("Le silo", 72, 42, 15, 16, "Le silo humide et sombre où l'argile mûrit."),
             ("L'afficheur du parc", 11, 41, 24, 13, "L'afficheur du parc : durées de repos et taux d'humidité."),
             ("Le cadran du silo", 75, 60, 11, 12, "Le cadran à trois molettes qui verrouille la porte du silo.")],
    "broyage": [("Le panneau des plaques", 86, 41, 12, 15, "Le panneau « Plaques manquantes » : les plaques des machines sont tombées."),
                ("Le plan de l'atelier", 30, 6, 22, 24, "Le plan de l'atelier : des postes numérotés, sans nom de machine."),
                ("Le poste de Karim", 59, 46, 14, 36, "La grosse machine du technicien : Karim vérifie vos connaissances ici."),
                ("Les machines en marche", 29, 52, 23, 20, "Une machine qui tourne, mais qui ne broie pas.")],
    "epuration": [("Le tamis vibrant", 6, 48, 23, 40, "Un tamis vibrant : il trie les grains selon leur taille."),
                  ("La cellule de flottation", 56, 45, 28, 44, "La cellule où deux poudres se séparent."),
                  ("Le panneau de sécurité", 87, 41, 11, 34, "Le panneau des règles de sécurité de la station."),
                  ("La fiche de poste", 38, 56, 15, 30, "La fiche de poste, affichée près de l'aimant.")],
    "dures": [("Le tableau des étiquettes", 7, 38, 41, 23, "Le tableau du laboratoire : une matière, un rôle, des étiquettes mélangées."),
              ("Les trois bacs", 7, 66, 48, 22, "Trois bacs : feldspath, sable de silice, chamotte."),
              ("Le bureau de Madame Aubry", 77, 54, 12, 32, "La machine de la responsable du laboratoire."),
              ("Le concasseur", 62, 54, 12, 32, "Le concasseur : un bloc de roche y devient poudre.")],
}

# Narration : par énigme (id) → (problème, enjeu, pourquoi ici, effet, réaction, réplique Essentiel, réplique Expert)
# Pour la première énigme de chaque salle, le dialogue d'accueil du jeu (dialogues.json) est conservé.
N = {
 "e1-1": ("Le panneau de chantier a perdu les définitions de six mots du métier.", "Sans le vocabulaire, personne ne comprend le bon de lancement.",
          "On ne prépare pas une matière dont on ne connaît pas les mots.", "eclat", "Les définitions se rétablissent une à une sur le panneau.", "", ""),
 "e1-2": ("Le vent a mélangé les panneaux de la filière de l'argile.", "Une étape oubliée, et l'argile arrive mal préparée à l'atelier.",
          "La carrière est le début de la filière : il faut en connaître l'ordre.", "ouverture", "Les panneaux s'alignent dans le bon sens, de la carrière à la matière prête.",
          "Remettez les étapes dans l'ordre, de la carrière à la matière prête.", "Six étapes, aucun repère : de la carrière à la matière prête."),
 "e1-3": ("Odile a noté des phrases dans son carnet, mais certaines sont fausses.", "Une fausse règle dans le carnet, et l'extraction se fait au mauvais moment.",
          "Le carnet d'Odile guide l'équipe d'extraction.", "calme", "Une coche verte s'affiche à côté de chaque phrase vérifiée.",
          "Mon carnet contient des erreurs. Vrai ou faux ?", "Vérifiez mes cinq phrases : je ne recopie que les vraies."),
 "e1-4": ("La fiche d'analyse du terrain est à moitié effacée.", "Sans analyse, on ne sait pas si le gisement vaut la peine d'être exploité.",
          "On analyse le terrain avant d'extraire.", "lumiere", "La fiche se complète et le tampon d'Odile se pose.",
          "", "La fiche d'analyse a des trous. Deux étiquettes sont des pièges."),
 "e2-1": ("Malik hésite : que se passe-t-il quand l'argile reste dehors sous la pluie ?", "S'il se trompe, l'argile sera mise au silo trop tôt.",
          "Le pourrissement est la première phase de repos de l'argile.", "calme", "La pluie s'arrête et l'argile s'assombrit doucement.",
          "Voilà mes phrases sur le pourrissement. Vrai ou faux ?", "Cinq phrases sur le pourrissement. Attention aux durées."),
 "e2-2": ("Les étiquettes du parc et du silo sont mélangées.", "Une argile mal rangée mûrit trop vite ou pas du tout.",
          "On distingue ce qui se passe dehors et ce qui se passe au silo.", "ouverture", "Les étiquettes se collent sur le tas et sur la porte du silo.",
          "Dehors ou au silo ? Rangez chaque étiquette.", "Huit étiquettes : pourrissement ou maturation. Les durées comptent."),
 "e2-3": ("L'hygromètre de Malik affiche des chiffres que personne ne comprend.", "Une argile trop humide ou trop sèche se travaille mal.",
          "Le taux d'humidité dit si l'argile est prête.", "eclat", "L'aiguille de l'hygromètre se stabilise.",
          "Je vous pose trois questions sur l'humidité.", "Trois questions de chiffres : je veux des réponses précises."),
 "e2-4": ("La porte du silo est fermée par un cadran à trois molettes.", "Sans ouvrir le silo, on ne peut pas sortir l'argile mûre.",
          "Trois nombres du chapitre ouvrent le cadran.", "ouverture", "Le cadran s'ouvre avec un déclic.",
          "", "Trois molettes : trois nombres du chapitre."),
 "e3-1": ("Les plaques des machines sont tombées de leur support.", "Karim ne peut pas lancer un broyage sans savoir quelle machine fait quoi.",
          "Chaque machine broie à sa façon.", "eclat", "Chaque plaque retrouve sa machine.", "", ""),
 "e3-2": ("Le plan de l'atelier n'a plus de noms de machines.", "Une machine au mauvais poste, et le broyage s'arrête.",
          "Chaque machine a sa place dans l'atelier.", "ouverture", "Les noms s'inscrivent sur le plan, poste par poste.",
          "Placez chaque machine sur son poste.", "Placez chaque machine sur le poste de sa description. Deux étiquettes sont en trop."),
 "e3-3": ("Karim veut vérifier que vous savez choisir une machine.", "Une mauvaise machine, et l'argile sort mal broyée.",
          "Choisir sa machine, c'est connaître ce qu'elle fait.", "lumiere", "Les voyants des machines passent au vert.",
          "Trois questions sur le broyage.", "Trois questions de détail : je ne confie pas les machines à n'importe qui."),
 "e3-4": ("Cinq machines tournent, mais une ne broie pas l'argile.", "Si l'intruse reste dans la liste, le broyage est faux.",
          "Une seule machine de l'atelier ne sert pas à broyer.", "calme", "La machine intruse s'arrête, les autres continuent.",
          "", "Quatre machines broient l'argile. Laquelle n'est pas à sa place ?"),
 "e4-1": ("Le tamis vibrant et l'aimant se partagent les étiquettes.", "Un morceau de fer dans la pâte, et la pièce éclate à la cuisson.",
          "Tamisage et déferrage n'enlèvent pas la même chose.", "ouverture", "Les étiquettes se placent sous le tamis ou sous l'aimant.",
          "Tamis ou aimant ? Rangez chaque étiquette.", "Huit étiquettes : tamisage ou déferrage. Attention aux détails."),
 "e4-2": ("Les étapes de la cellule de flottation sont dans le désordre.", "Une étape sautée, et les deux poudres restent mélangées.",
          "La flottation sépare deux poudres de nature différente.", "calme", "Les bulles remontent, la cellule se met en route.",
          "Remettez les étapes de la flottation dans l'ordre.", "Cinq étapes, sans repères : l'ordre de la flottation."),
 "e4-3": ("Le panneau de sécurité de la station est couvert de phrases.", "Une mauvaise habitude, et la poussière devient un danger.",
          "La sécurité passe avant tout à la station d'épuration.", "lumiere", "Le voyant du panneau passe au vert.",
          "Rappel des règles de sécurité. Vrai ou faux ?", "Cinq phrases sur la sécurité : repérez les mauvais gestes."),
 "e4-4": ("La fiche de poste de la station est incomplète.", "Sans fiche de poste, les apprentis se trompent de geste.",
          "Connaître son poste, c'est connaître ses machines et ses règles.", "eclat", "La fiche s'imprime et se colle au mur.",
          "", "La fiche de poste a des trous. Deux étiquettes sont en trop."),
 "e5-1": ("Les étiquettes des échantillons sont mélangées.", "Un échantillon mal étiqueté, et le lot de pâte est faux.",
          "Chaque matière dure a sa description.", "eclat", "Les étiquettes retrouvent leurs échantillons.", "", ""),
 "e5-2": ("Trois bacs attendent leurs matières.", "Du sable dans le bac du feldspath, et la pâte fond mal.",
          "Chaque matière dure a son rôle dans la pâte.", "ouverture", "Les trois bacs se remplissent de poudres de couleurs différentes.",
          "Feldspath, sable de silice ou chamotte ? Rangez chaque étiquette.", "Neuf étiquettes, trois bacs : feldspath, sable de silice, chamotte."),
 "e5-3": ("Madame Aubry veut s'assurer que vous connaissez vos matières.", "Elle ne signe pas le dernier tampon à la légère.",
          "Les matières dures s'obtiennent en les concassant et en les broyant.", "lumiere", "Le tampon de Madame Aubry s'illumine.",
          "Quelques questions, et je signe.", "Des questions précises : je n'accepte que des réponses exactes."),
 "e5-4": ("Le bloc de roche doit devenir une poudre utilisable.", "Sans ordre des étapes, la roche reste un bloc.",
          "Du bloc à la poudre : on concasse, on broie, on tamise.", "ouverture", "Le bloc se transforme en une poudre fine.",
          "", "Remettez les étapes dans l'ordre, du bloc brut à la matière prête."),
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
    js = os.path.join(RACINE, "matieres-premieres", "js", "decors.js")
    code = ("global.window={};" + open(js, encoding="utf-8").read() +
            ";process.stdout.write(JSON.stringify(SVG_DECORS));")
    svgs = json.loads(subprocess.run(["node", "-e", code], capture_output=True, text=True, check=True).stdout)
    out = ["/* Décors dessinés de secours (16:9) — générés par outils/immersif/completer-matieres-premieres.py",
           "   à partir des décors du jeu classique. Une image déposée dans assets/images/decors/<id>.webp|.jpg|.png les remplace. */",
           "var VML = window.VML || (window.VML = {});", "VML.SVG_DECORS = VML.SVG_DECORS || {};"]
    for d in DECORS:
        s = svgs[d].replace('viewBox="0 0 800 300"', 'viewBox="0 -150 800 450"', 1)
        i = s.index(">") + 1
        s = s[:i] + f'<rect x="0" y="-150" width="800" height="150" fill="{MURS[d]}"/>' + s[i:]
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
            en["liberte_ou_anachronisme"] = "Manufacture et personnages inventés ; toutes les données techniques viennent du cours."
            en["niveau_variantes"] = "Essentiel (grade matelot) : repères et données réduites. Expert (grade timonier) : sans repères, plus de cartes, chiffres du cours."
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
