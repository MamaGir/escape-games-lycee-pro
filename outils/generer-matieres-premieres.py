#!/usr/bin/env python3
"""Génère les données du jeu « Le bon de lancement » (La préparation des matières premières, CAP Décoration sur céramique).

Ne pas modifier les JSON à la main : éditer ce script puis relancer
    python outils/generer-matieres-premieres.py
Niveaux : les clés internes restent « cm1 » / « cm2 » (format du moteur commun) ;
l'interface du lycée affiche « Essentiel » (cm1) et « Expert » (cm2) — voir commun/lycee-pro/libelles.js.
Source du contenu : cours « Préparation des matières premières des pâtes céramiques » (CAP, version allégée) de l'enseignant.
"""
import json, os

ICI = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(ICI), "matieres-premieres", "assets", "data")
TITRE = "Le bon de lancement"
COURS = "Cours « Préparation des matières premières des pâtes céramiques », CAP"


def ecrire(nom, d):
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, nom), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")


def en(id_, titre, type_, consigne, correction, indices, cm1=None, cm2=None, lecon="", partie="", expert=None):
    """Énigme : cm1 = Essentiel, cm2 = Expert. expert=dict → énigme réservée au niveau Expert (bloc commun)."""
    e = {"id": id_, "titre": titre, "type": type_}
    if expert is not None:
        e["niveaux"] = ["CM2"]
    e["consigne"] = consigne
    e["source"] = f"{COURS}, {partie}"
    e["correction"] = correction
    e["indices"] = indices
    if expert is not None:
        e["commun"] = expert
    else:
        e["cm1"], e["cm2"] = cm1, cm2
    e["lecon"] = lecon
    return e


# =====================================================================================
# SALLE 1 — La carrière (pourquoi préparer, analyse du terrain, extraction)
# =====================================================================================
S1 = [
    en("1-1", "Les mots du chantier", "association",
       {"cm1": "Relie chaque mot à sa définition : clique sur un mot, puis sur la bonne définition.",
        "cm2": "Six mots du métier ont perdu leur définition. Reconstitue les six paires."},
       "Un gisement est l'endroit où une matière s'est accumulée naturellement. Une impureté est une matière qu'on ne veut pas dans la pâte (racines, cailloux, fer). Broyer, c'est réduire en petits morceaux ou en poudre. Tamiser, c'est trier les grains selon leur taille avec une grille. Un dégraissant rend la pâte moins collante ; un fondant l'aide à fondre à la cuisson.",
       {"cm1": ["Les définitions sont dans l'encadré « Mots à connaître ».", "Un tamis est une grille.", "Une impureté est un intrus dans la pâte."],
        "cm2": ["Commence par les mots que tu connais déjà.", "Dégraissant et fondant ont chacun un effet différent.", "Le feldspath est un fondant."]},
       cm1={"paires": [
           {"g": "Gisement", "d": "Endroit où une matière s'est accumulée naturellement"},
           {"g": "Impureté", "d": "Matière qu'on ne veut pas dans la pâte"},
           {"g": "Broyer", "d": "Réduire en petits morceaux ou en poudre"},
           {"g": "Tamiser", "d": "Trier les grains selon leur taille avec une grille"}]},
       cm2={"paires": [
           {"g": "Gisement", "d": "Endroit où une matière s'est accumulée naturellement"},
           {"g": "Impureté", "d": "Racines, cailloux, fer : ce qu'on ne veut pas dans la pâte"},
           {"g": "Tamiser", "d": "Trier les grains selon leur taille avec un tamis"},
           {"g": "Plastique", "d": "Se modèle facilement sans se casser"},
           {"g": "Dégraissant", "d": "Matière ajoutée pour rendre la pâte moins collante"},
           {"g": "Fondant", "d": "Matière qui aide la pâte à fondre à la cuisson"}]},
       lecon="gisement-extraction", partie="encadré « Mots à connaître »"),

    en("1-2", "Les panneaux de la filière", "ordre",
       {"cm1": "Les six panneaux de la filière de l'argile ont été mélangés. Remets les étapes dans l'ordre, de la carrière à la matière prête. Utilise les flèches, puis vérifie.",
        "cm2": "Remets dans l'ordre les six étapes de préparation de l'argile, sans l'aide des repères."},
       "Analyse du terrain, extraction, pourrissement, broyage, épuration, maturation : c'est l'ordre du cours, de la carrière à la matière prête à l'emploi.",
       {"cm1": ["La première étape se fait avant de creuser.", "L'argile reste dehors plusieurs mois avant d'être cassée.", "La dernière étape se passe dans un silo."],
        "cm2": ["On analyse le terrain avant d'extraire.", "Le pourrissement a lieu avant le broyage.", "L'épuration précède la maturation."]},
       cm1={"items": [{"txt": "Analyser le terrain", "sous": "échantillons en grille", "rang": 1},
                      {"txt": "Extraire", "sous": "carrière à ciel ouvert", "rang": 2},
                      {"txt": "Pourrissement", "sous": "l'argile reste dehors", "rang": 3},
                      {"txt": "Broyer", "sous": "on casse l'argile", "rang": 4},
                      {"txt": "Épurer", "sous": "tamis et aimants", "rang": 5},
                      {"txt": "Maturation", "sous": "au silo", "rang": 6}]},
       cm2={"items": [{"txt": "Analyser le terrain", "rang": 1}, {"txt": "Extraire", "rang": 2}, {"txt": "Pourrissement", "rang": 3},
                      {"txt": "Broyer", "rang": 4}, {"txt": "Épurer", "rang": 5}, {"txt": "Maturation", "rang": 6}]},
       lecon="gisement-extraction", partie="partie I, « Vue d'ensemble »"),

    en("1-3", "Le carnet d'Odile", "vraifaux",
       {"cm1": "Odile, la cheffe de carrière, a noté quatre phrases dans son carnet. Pour chacune, dis si elle est vraie ou fausse.",
        "cm2": "Vérifie les cinq phrases du carnet d'Odile : vraie ou fausse ?"},
       "Dans la nature, les matières premières ne sont pas prêtes à l'emploi : on les prépare pour obtenir une pâte stable et de qualité constante. Avant d'extraire, on analyse le terrain en prélevant un échantillon par carré d'une grille. L'argile est extraite dans des carrières à ciel ouvert, en général à l'entrée de l'hiver. L'argile grasse, quasiment pure, donne un produit de meilleure qualité que l'argile maigre.",
       {"cm1": ["Relis le début de la partie I.", "Un échantillon par carré de la grille.", "Les excavatrices travaillent à ciel ouvert."],
        "cm2": ["Un gisement est fait de plusieurs couches.", "L'extraction a lieu à l'entrée de l'hiver.", "Maigre = sableuse, avec beaucoup d'impuretés."]},
       cm1={"affirmations": [
           {"txt": "Dans la nature, les matières premières sont prêtes à l'emploi.", "vrai": False, "explication": "Elles contiennent des impuretés, des morceaux trop gros, trop d'eau."},
           {"txt": "Avant d'extraire l'argile, on analyse le terrain.", "vrai": True, "explication": "On prélève des échantillons pour repérer la meilleure couche."},
           {"txt": "L'argile est extraite dans une carrière à ciel ouvert.", "vrai": True, "explication": "Avec des excavatrices et des camions-bennes."},
           {"txt": "On prélève un seul échantillon pour tout le gisement.", "vrai": False, "explication": "On en prélève un par carré de la grille."}]},
       cm2={"affirmations": [
           {"txt": "Préparer les matières premières rend la pâte stable et de qualité constante.", "vrai": True, "explication": "La pièce se modèle, sèche et cuit toujours de la même façon."},
           {"txt": "Toutes les couches d'un gisement sont identiques.", "vrai": False, "explication": "Les strates sont toutes différentes."},
           {"txt": "On découpe le terrain en carrés et on prélève un échantillon par carré.", "vrai": True, "explication": "On repère ainsi la meilleure couche."},
           {"txt": "En général, l'extraction a lieu à l'entrée de l'hiver.", "vrai": True, "explication": "C'est l'indication du cours."},
           {"txt": "Une argile « maigre » donne un produit de meilleure qualité qu'une argile « grasse ».", "vrai": False, "explication": "L'argile grasse est quasiment pure : c'est elle qui donne le meilleur produit."}]},
       lecon="gisement-extraction", partie="parties I et II.1"),

    en("1-4", "La fiche d'analyse du terrain", "trous", {"cm2": "Complète la fiche d'analyse du terrain avec les bonnes étiquettes. Deux étiquettes sont en trop."},
       "Avant d'extraire, on analyse le terrain : on le découpe en carrés (une grille) et on prélève un échantillon par carré pour repérer la meilleure couche. L'argile grasse, quasiment pure, donne un produit de meilleure qualité que l'argile maigre, qui contient beaucoup d'impuretés.",
       {"cm2": ["Le premier mot manquant est une action qui précède l'extraction.", "On découpe le terrain en carrés : cela dessine une grille.", "Les étiquettes en trop parlent de cuisson et de verre."]},
       expert={"texte": "<p>Avant d'extraire l'argile, on [[analyse]] le terrain : on le découpe en carrés, c'est une [[grille]], et on prélève un [[échantillon]] par carré. On repère ainsi la meilleure [[couche]]. Une argile « [[grasse]] » est quasiment pure : le produit est de meilleure qualité. Une argile « [[maigre]] » contient beaucoup d'impuretés.</p>",
               "etiquettes": ["analyse", "grille", "échantillon", "couche", "grasse", "maigre", "émail", "vitrifiée"]},
       lecon="gisement-extraction", partie="partie II.1"),
]

# =====================================================================================
# SALLE 2 — Le parc d'argile et le silo (pourrissement, maturation)
# =====================================================================================
S2 = [
    en("2-1", "Dehors, sous la pluie", "vraifaux",
       {"cm1": "Malik surveille le parc d'argile. Pour chacune de ses quatre phrases, dis si elle est vraie ou fausse.",
        "cm2": "Malik a noté cinq phrases sur le pourrissement. Vraie ou fausse ?"},
       "Pendant le pourrissement, l'argile est stockée dehors pendant 3 à 24 mois. La pluie, le gel et le dégel fragmentent les grains, et des bactéries décomposent les restes de plantes. L'argile devient plus plastique et plus résistante.",
       {"cm1": ["Relis le paragraphe « Le pourrissement ».", "L'argile reste dehors.", "On compte en mois, pas en jours."],
        "cm2": ["La durée se compte en mois.", "Gel et dégel fragmentent les grains.", "Les bactéries s'attaquent aux restes de plantes."]},
       cm1={"affirmations": [
           {"txt": "Pendant le pourrissement, l'argile est stockée dehors.", "vrai": True, "explication": "Elle subit la pluie, le gel et le dégel."},
           {"txt": "Le pourrissement dure quelques jours.", "vrai": False, "explication": "Il dure de 3 à 24 mois."},
           {"txt": "La pluie, le gel et le dégel fragmentent les grains.", "vrai": True, "explication": "C'est ce qui rend l'argile plus fine."},
           {"txt": "Après le pourrissement, l'argile est plus plastique et plus résistante.", "vrai": True, "explication": "C'est le résultat de cette étape."}]},
       cm2={"affirmations": [
           {"txt": "Le pourrissement dure de 3 à 24 mois.", "vrai": True, "explication": "L'argile est stockée dehors pendant tout ce temps."},
           {"txt": "Des bactéries décomposent les restes de plantes.", "vrai": True, "explication": "Elles nettoient l'argile."},
           {"txt": "Seule la pluie agit sur l'argile : le gel ne sert à rien.", "vrai": False, "explication": "Le gel et le dégel fragmentent aussi les grains."},
           {"txt": "Après le pourrissement, l'argile est moins plastique.", "vrai": False, "explication": "Elle devient plus plastique et plus résistante."},
           {"txt": "L'argile est stockée à l'abri, dans un hangar fermé.", "vrai": False, "explication": "Elle est stockée dehors."}]},
       lecon="pourrissement-maturation", partie="partie II.2"),

    en("2-2", "Le parc ou le silo ?", "tri",
       {"cm1": "Range chaque étiquette : pourrissement (dehors) ou maturation (au silo) ?",
        "cm2": "Range les huit étiquettes : pourrissement ou maturation ? Attention aux durées."},
       "Le pourrissement a lieu dehors, de 3 à 24 mois : pluie, gel, dégel et bactéries rendent l'argile plus plastique et plus résistante. La maturation a lieu dans un silo humide et sombre, au moins 2 semaines : l'humidité baisse.",
       {"cm1": ["Pourrissement = dehors, sous la pluie.", "Maturation = dans un silo, à l'abri.", "Le silo est humide et sombre."],
        "cm2": ["Les durées ne sont pas les mêmes : mois d'un côté, semaines de l'autre.", "L'humidité baisse pendant la maturation.", "Les bactéries travaillent dehors."]},
       cm1={"colonnes": [{"id": "pou", "titre": "Pourrissement"}, {"id": "mat", "titre": "Maturation"}],
            "cartes": [{"txt": "Stockée dehors", "col": "pou"}, {"txt": "Pluie, gel et dégel", "col": "pou"}, {"txt": "De 3 à 24 mois", "col": "pou"},
                       {"txt": "Silo humide et sombre", "col": "mat"}, {"txt": "Au moins 2 semaines", "col": "mat"}, {"txt": "L'humidité baisse", "col": "mat"}]},
       cm2={"colonnes": [{"id": "pou", "titre": "Pourrissement"}, {"id": "mat", "titre": "Maturation"}],
            "cartes": [{"txt": "Stockée dehors", "col": "pou"}, {"txt": "Les grains se fragmentent", "col": "pou"}, {"txt": "Des bactéries décomposent les restes de plantes", "col": "pou"},
                       {"txt": "De 3 à 24 mois", "col": "pou"},
                       {"txt": "Silo humide et sombre", "col": "mat"}, {"txt": "Au moins 2 semaines", "col": "mat"},
                       {"txt": "Le taux d'humidité baisse", "col": "mat"}, {"txt": "De 18-22 % à 13-18 % d'humidité", "col": "mat"}]},
       lecon="pourrissement-maturation", partie="parties II.2 et III.3"),

    en("2-3", "Le taux d'humidité", "qcm",
       {"cm1": "Malik te pose trois questions sur l'humidité de l'argile. Choisis la bonne réponse à chacune.",
        "cm2": "Malik veut vérifier tes chiffres. Réponds à ses trois questions."},
       "L'argile fraîchement extraite contient de 18 % à 22 % d'eau. Après la maturation (au moins 2 semaines en silo), son taux d'humidité baisse : de 13 % à 18 %.",
       {"cm1": ["Le taux d'humidité, c'est la quantité d'eau.", "Il baisse pendant la maturation.", "Regarde le tableau de la partie III.3."],
        "cm2": ["Les deux fourchettes se recoupent un peu.", "Fraîche : 18 à 22 %.", "Après maturation : 13 à 18 %."]},
       cm1={"questions": [
           {"q": "L'argile fraîchement extraite contient…", "options": ["de 18 % à 22 % d'eau", "de 50 % à 60 % d'eau", "moins de 5 % d'eau"], "bonne": 0, "explication": "C'est le taux d'humidité de l'argile fraîche."},
           {"q": "Pendant la maturation, le taux d'humidité…", "options": ["monte", "baisse", "ne change pas"], "bonne": 1, "explication": "Ses propriétés changent et son taux d'humidité baisse."},
           {"q": "L'argile reste en silo au moins…", "options": ["2 jours", "2 semaines", "2 ans"], "bonne": 1, "explication": "Au moins 2 semaines, dans un silo humide et sombre."}]},
       cm2={"questions": [
           {"q": "Après la maturation, le taux d'humidité est de…", "options": ["18 % à 22 %", "13 % à 18 %", "5 % à 8 %"], "bonne": 1, "explication": "Il baisse par rapport à l'argile fraîchement extraite."},
           {"q": "Que devient l'argile après le pourrissement ?", "options": ["Plus plastique et plus résistante", "Plus sableuse", "Plus rouge"], "bonne": 0, "explication": "Les grains se fragmentent et les restes de plantes sont décomposés."},
           {"q": "Où se fait la maturation ?", "options": ["Dehors, sous la pluie", "Dans un four", "Dans un silo humide et sombre"], "bonne": 2, "explication": "L'argile y est entreposée au moins 2 semaines."}]},
       lecon="pourrissement-maturation", partie="partie III.3"),

    en("2-4", "Le cadran du silo", "code", {"cm2": "Le cadran du silo a trois molettes. Trouve les trois nombres."},
       "Le pourrissement dure au plus 24 mois. La maturation dure au moins 2 semaines. Après la maturation, le taux d'humidité va jusqu'à 18 % au plus.",
       {"cm2": ["Le premier nombre est un nombre de mois : le plus grand de la fourchette 3 à 24.", "Le deuxième nombre est un nombre de semaines.", "Le troisième est un pourcentage : le plus grand de la fourchette 13 à 18."]},
       expert={"champs": [{"libelle": "Durée maximale du pourrissement (mois)", "valeur": "24", "longueur": 2},
                          {"libelle": "Durée minimale de la maturation (semaines)", "valeur": "2", "longueur": 1},
                          {"libelle": "Taux d'humidité maximal après maturation (%)", "valeur": "18", "longueur": 2}]},
       lecon="pourrissement-maturation", partie="parties II.2 et III.3"),
]

# =====================================================================================
# SALLE 3 — L'atelier de broyage (machines à broyer l'argile)
# =====================================================================================
S3 = [
    en("3-1", "Les plaques des machines", "association",
       {"cm1": "Les plaques de quatre machines sont tombées. Relie chaque machine à sa façon de fonctionner.",
        "cm2": "Cinq machines de l'atelier ont perdu leur plaque. Relie chaque machine à son principe."},
       "Broyeur à meule : deux meules qui tournent écrasent l'argile. Brise-mottes : des rouleaux ou des marteaux cassent les mottes. Désagrégateur : une chemise lisse et une chemise striée avec des lames désagrègent l'argile. Broyeur à marteaux : des marteaux qui tournent vite frappent l'argile. Broyeur à billes : un cylindre rempli de billes qui tourne ; le frottement fragmente l'argile.",
       {"cm1": ["Le tableau des machines est dans la partie III.1.", "Les meules écrasent.", "Les billes frottent."],
        "cm2": ["Chaque machine a un verbe : écraser, casser, désagréger, frapper, frotter.", "La chemise striée porte des lames.", "Le marteau frappe, le brise-mottes casse."]},
       cm1={"paires": [{"g": "Broyeur à meule", "d": "Deux meules qui tournent écrasent l'argile"},
                       {"g": "Brise-mottes", "d": "Des rouleaux ou des marteaux cassent les mottes"},
                       {"g": "Broyeur à marteaux", "d": "Des marteaux qui tournent vite frappent l'argile"},
                       {"g": "Broyeur à billes", "d": "Un cylindre qui tourne, rempli de billes"}]},
       cm2={"paires": [{"g": "Broyeur à meule", "d": "Deux meules qui tournent écrasent l'argile"},
                       {"g": "Brise-mottes", "d": "Des rouleaux ou des marteaux cassent les mottes"},
                       {"g": "Désagrégateur", "d": "Une chemise lisse et une chemise striée avec des lames"},
                       {"g": "Broyeur à marteaux", "d": "Des marteaux qui tournent vite, sortie par une grille"},
                       {"g": "Broyeur à billes (alsing)", "d": "Le frottement des billes dans un cylindre qui tourne"}]},
       lecon="broyage", partie="partie III.1, tableau des machines"),

    en("3-2", "Le plan de l'atelier", "plan",
       {"cm1": "Karim range son atelier. Place chaque machine sur le bon poste : clique sur une étiquette, puis sur la case. Une étiquette est en trop.",
        "cm2": "Place chaque machine sur le poste qui correspond à sa description. Deux étiquettes sont en trop."},
       "Poste meule : deux meules écrasent l'argile. Poste marteaux : l'argile sort par une grille quand elle est assez fine. Poste billes : un cylindre qui tourne rempli de billes ; broyage à sec ou avec de l'eau. Poste mottes : des rouleaux ou des marteaux cassent les mottes. Poste lames : une chemise lisse et une chemise striée désagrègent l'argile.",
       {"cm1": ["Lis la description écrite sur chaque poste.", "Le broyeur à billes contient des billes.", "Le brise-mottes casse les mottes."],
        "cm2": ["Chaque machine a une façon de fonctionner différente.", "La grille de sortie est celle du broyeur à marteaux.", "Les lames sont dans le désagrégateur."]},
       cm1={"titre": "Le plan de l'atelier de broyage", "colonnes": 2,
            "cases": [{"libelle": "Poste 1 : deux meules qui tournent écrasent l'argile", "reponse": "Broyeur à meule"},
                      {"libelle": "Poste 2 : des marteaux frappent l'argile, qui sort par une grille", "reponse": "Broyeur à marteaux"},
                      {"libelle": "Poste 3 : un cylindre qui tourne, rempli de billes", "reponse": "Broyeur à billes"},
                      {"libelle": "Poste 4 : des rouleaux cassent les mottes", "reponse": "Brise-mottes"}],
            "etiquettes": ["Broyeur à meule", "Broyeur à marteaux", "Broyeur à billes", "Brise-mottes", "Tamis vibrant"]},
       cm2={"titre": "Le plan de l'atelier de broyage", "colonnes": 2,
            "cases": [{"libelle": "Poste 1 : l'argile sort quand elle est assez fine, à travers une grille", "reponse": "Broyeur à marteaux"},
                      {"libelle": "Poste 2 : deux meules qui tournent", "reponse": "Broyeur à meule"},
                      {"libelle": "Poste 3 : un tiers de billes, un tiers d'argile, un tiers d'eau", "reponse": "Broyeur à billes"},
                      {"libelle": "Poste 4 : une chemise lisse et une chemise striée avec des lames", "reponse": "Désagrégateur"},
                      {"libelle": "Poste 5 : des rouleaux ou des marteaux qui cassent les mottes", "reponse": "Brise-mottes"}],
            "etiquettes": ["Broyeur à marteaux", "Broyeur à meule", "Broyeur à billes", "Désagrégateur", "Brise-mottes", "Tamis vibrant", "Concasseur à mâchoires"]},
       lecon="broyage", partie="partie III.1"),

    en("3-3", "Les questions de Karim", "qcm",
       {"cm1": "Karim te pose trois questions sur le broyage. Choisis la bonne réponse à chacune.",
        "cm2": "Karim veut être sûr que tu connais les détails. Réponds à ses trois questions."},
       "Broyer, c'est casser l'argile en petits morceaux : on réduit sa taille. Dans le broyeur à billes, le frottement des billes fragmente l'argile ; le broyage se fait à sec ou avec de l'eau (un tiers de billes, un tiers d'argile, un tiers d'eau). Dans le broyeur à marteaux, l'argile sort à travers une grille quand elle est assez fine.",
       {"cm1": ["Broyer, c'est réduire la taille.", "Les billes frottent contre l'argile.", "La grille laisse passer l'argile assez fine."],
        "cm2": ["Relis le tableau des machines.", "Trois tiers égaux.", "Le désagrégateur travaille avec des lames."]},
       cm1={"questions": [
           {"q": "Broyer l'argile, c'est…", "options": ["la casser en petits morceaux", "la faire cuire", "la colorer"], "bonne": 0, "explication": "On réduit sa taille."},
           {"q": "Dans un broyeur à billes, l'argile est fragmentée par…", "options": ["des lames", "le frottement des billes", "un aimant"], "bonne": 1, "explication": "Le cylindre tourne et les billes frottent l'argile."},
           {"q": "Dans le broyeur à marteaux, l'argile sort…", "options": ["quand elle est assez fine, à travers une grille", "dès qu'elle est entrée", "par le haut, en poussière"], "bonne": 0, "explication": "La grille ne laisse passer que l'argile assez fine."}]},
       cm2={"questions": [
           {"q": "Broyage à l'eau dans un broyeur à billes : les proportions sont…", "options": ["un tiers de billes, un tiers d'argile, un tiers d'eau", "la moitié d'eau, le reste d'argile", "uniquement des billes et de l'eau"], "bonne": 0, "explication": "Trois tiers égaux, indique le cours."},
           {"q": "Le broyeur à billes peut broyer…", "options": ["seulement à sec", "à sec ou avec de l'eau", "seulement avec de l'eau"], "bonne": 1, "explication": "Les deux sont possibles."},
           {"q": "Le désagrégateur fonctionne avec…", "options": ["deux meules", "une chemise lisse et une chemise striée avec des lames", "un aimant"], "bonne": 1, "explication": "Les lames désagrègent l'argile."}]},
       lecon="broyage", partie="partie III.1"),

    en("3-4", "La machine qui ne broie pas", "intrus", {"cm2": "Quatre machines de cet atelier broient l'argile. Une seule ne sert pas à la broyer : trouve l'intrus."},
       "Le tamis vibrant n'est pas un broyeur : il trie les grains selon leur taille et élimine les impuretés. Il appartient à l'épuration. Meule, marteaux, désagrégateur et brise-mottes cassent ou écrasent l'argile.",
       {"cm2": ["Cherche la machine qui ne casse rien.", "Elle trie.", "Elle utilise une grille qui vibre."]},
       expert={"cartes": [{"txt": "Broyeur à meule", "sous": "deux meules", "intrus": False},
                          {"txt": "Broyeur à marteaux", "sous": "grille de sortie", "intrus": False},
                          {"txt": "Désagrégateur", "sous": "lames", "intrus": False},
                          {"txt": "Tamis vibrant", "sous": "trie les grains", "intrus": True},
                          {"txt": "Brise-mottes", "sous": "casse les mottes", "intrus": False}]},
       lecon="broyage", partie="parties III.1 et III.2"),
]

# =====================================================================================
# SALLE 4 — La station d'épuration (tamisage, déferrage, flottation, sécurité)
# =====================================================================================
S4 = [
    en("4-1", "Tamis ou aimant ?", "tri",
       {"cm1": "Range chaque étiquette : tamisage (tamis vibrant) ou déferrage (aimants) ?",
        "cm2": "Range les huit étiquettes : tamisage ou déferrage ? Attention aux détails."},
       "Le tamis vibrant trie les grains selon leur taille : il élimine les impuretés (feuilles, racines) et les grains trop gros. Le déferrage utilise des aimants ou des électro-aimants qui attirent les particules de fer ; il sépare le fer de l'argile, sèche ou en barbotine.",
       {"cm1": ["Le tamis a une grille.", "Un aimant attire le fer.", "Le tamis garde les racines et les gros grains."],
        "cm2": ["Barbotine = argile avec de l'eau.", "Le tamis trie selon la taille.", "L'aimant ne retient que le fer."]},
       cm1={"colonnes": [{"id": "tam", "titre": "Tamisage"}, {"id": "def", "titre": "Déferrage"}],
            "cartes": [{"txt": "Trie les grains selon leur taille", "col": "tam"}, {"txt": "Élimine feuilles et racines", "col": "tam"}, {"txt": "Un tamis vibrant", "col": "tam"},
                       {"txt": "Attire les particules de fer", "col": "def"}, {"txt": "Des aimants", "col": "def"}, {"txt": "Sépare le fer de l'argile", "col": "def"}]},
       cm2={"colonnes": [{"id": "tam", "titre": "Tamisage"}, {"id": "def", "titre": "Déferrage"}],
            "cartes": [{"txt": "Trie les grains selon leur taille", "col": "tam"}, {"txt": "Élimine les impuretés", "col": "tam"}, {"txt": "Retire les grains trop gros", "col": "tam"},
                       {"txt": "Un tamis vibrant", "col": "tam"},
                       {"txt": "Aimants ou électro-aimants", "col": "def"}, {"txt": "Attire les particules de fer", "col": "def"},
                       {"txt": "Fonctionne sur l'argile sèche ou en barbotine", "col": "def"}, {"txt": "Épuration magnétique", "col": "def"}]},
       lecon="epuration-purification", partie="partie III.2"),

    en("4-2", "La cellule de flottation", "ordre",
       {"cm1": "Jade te montre la flottation, qui sépare deux poudres. Remets les quatre étapes dans l'ordre.",
        "cm2": "Remets dans l'ordre les cinq étapes de la flottation, sans l'aide des repères."},
       "Flottation : on met de l'eau et de la poudre dans un même mélange, puis on ajoute des réactifs et de l'air. Une des matières s'accroche aux bulles et monte en mousse ; l'autre reste au fond. Exemple : séparer le feldspath de la silice.",
       {"cm1": ["On commence par préparer le mélange.", "Les réactifs et l'air viennent avant les bulles.", "La mousse se forme en dernier."],
        "cm2": ["Eau et poudre d'abord.", "Réactifs et air ensuite.", "Une matière monte, l'autre reste."]},
       cm1={"items": [{"txt": "On mélange l'eau et la poudre", "sous": "le point de départ", "rang": 1},
                      {"txt": "On ajoute des réactifs et de l'air", "sous": "des bulles apparaissent", "rang": 2},
                      {"txt": "Une matière s'accroche aux bulles", "sous": "elle est attirée", "rang": 3},
                      {"txt": "Elle monte en mousse, l'autre reste au fond", "sous": "les deux sont séparées", "rang": 4}]},
       cm2={"items": [{"txt": "On mélange l'eau et la poudre", "rang": 1}, {"txt": "On ajoute des réactifs et de l'air", "rang": 2},
                      {"txt": "Une matière s'accroche aux bulles", "rang": 3}, {"txt": "Elle monte en mousse", "rang": 4},
                      {"txt": "L'autre matière reste au fond", "rang": 5}]},
       lecon="epuration-purification", partie="partie IV.4"),

    en("4-3", "Le panneau de sécurité", "vraifaux",
       {"cm1": "Jade rappelle les règles de sécurité de la station. Pour chaque phrase, dis si elle est vraie ou fausse.",
        "cm2": "Le panneau de sécurité de la station a cinq phrases. Vraie ou fausse ?"},
       "Le broyage, le concassage et le tamisage produisent des poussières fines (silice, argile sèche) dangereuses pour les poumons. Il faut porter un masque, travailler avec aspiration ou à l'humide, et ne jamais balayer à sec.",
       {"cm1": ["Relis l'encadré « Sécurité ».", "Les poussières fines se respirent.", "Balayer à sec soulève la poussière."],
        "cm2": ["Le masque protège les poumons.", "À l'humide, la poussière ne vole pas.", "Balayer à sec la remet en l'air."]},
       cm1={"affirmations": [
           {"txt": "Le broyage et le tamisage produisent des poussières fines.", "vrai": True, "explication": "De la silice, de l'argile sèche."},
           {"txt": "Ces poussières sont dangereuses pour les poumons.", "vrai": True, "explication": "On ne les respire pas."},
           {"txt": "On peut balayer à sec pour nettoyer.", "vrai": False, "explication": "Cela remet la poussière en l'air."},
           {"txt": "On porte un masque dans la station.", "vrai": True, "explication": "C'est une règle de sécurité."}]},
       cm2={"affirmations": [
           {"txt": "Le broyage, le concassage et le tamisage produisent des poussières fines.", "vrai": True, "explication": "Silice et argile sèche."},
           {"txt": "La poussière d'argile sèche est sans danger pour les poumons.", "vrai": False, "explication": "Elle est dangereuse, comme la silice."},
           {"txt": "Travailler avec aspiration ou à l'humide réduit les poussières.", "vrai": True, "explication": "Ce sont les deux moyens du cours."},
           {"txt": "On peut balayer à sec si on est rapide.", "vrai": False, "explication": "On ne balaie jamais à sec."},
           {"txt": "Le masque est facultatif si on tamise peu de temps.", "vrai": False, "explication": "Le masque se porte pour le broyage, le concassage et le tamisage."}]},
       lecon="epuration-purification", partie="encadré « Sécurité »"),

    en("4-4", "La fiche de poste", "trous", {"cm2": "Complète la fiche de poste de la station d'épuration avec les bonnes étiquettes. Deux étiquettes sont en trop."},
       "Un tamis vibrant trie selon la taille ; les aimants attirent le fer ; la flottation sépare le feldspath de la silice. Contre les poussières : masque, et jamais de balayage à sec.",
       {"cm2": ["Le premier mot est le nom de la machine qui trie.", "Les aimants attirent un métal.", "On travaille avec un masque ; on ne balaie jamais à sec."]},
       expert={"texte": "<p>Le [[tamis]] vibrant trie les grains selon leur [[taille]]. Les [[aimants]] attirent les particules de [[fer]]. Pour séparer le feldspath de la silice, on utilise la [[flottation]]. Pour se protéger des poussières, on porte un [[masque]] et on ne balaie jamais à [[sec]].</p>",
               "etiquettes": ["tamis", "taille", "aimants", "fer", "flottation", "masque", "sec", "couleur", "four"]},
       lecon="epuration-purification", partie="parties III.2 et IV.4"),
]

# =====================================================================================
# SALLE 5 — Le laboratoire des matières dures (feldspath, sable de silice, chamotte)
# =====================================================================================
S5 = [
    en("5-1", "Les étiquettes du laboratoire", "association",
       {"cm1": "Madame Aubry a mélangé les étiquettes de ses échantillons. Relie chaque matière ou machine à ce qui la décrit.",
        "cm2": "Relie chacune des six entrées à ce qui la décrit."},
       "Feldspath : fondant, qui aide la pâte à fondre à la cuisson. Sable de silice : dégraissant. Chamotte : argile déjà cuite, puis broyée. Concasseur à mâchoires : la roche est écrasée par pression. Concasseur à percussion : la roche éclate sous les chocs. Tessons broyés : débris de biscuits broyés puis tamisés.",
       {"cm1": ["Le feldspath aide à fondre.", "La chamotte a déjà connu le four.", "Le concasseur à mâchoires écrase."],
        "cm2": ["Les concasseurs travaillent sur les roches.", "Percussion = chocs.", "Les tessons sont des débris de biscuits."]},
       cm1={"paires": [{"g": "Feldspath", "d": "Fondant : aide la pâte à fondre à la cuisson"},
                       {"g": "Sable de silice", "d": "Dégraissant : rend la pâte moins collante"},
                       {"g": "Chamotte", "d": "Argile déjà cuite, puis broyée"},
                       {"g": "Concasseur à mâchoires", "d": "La roche est écrasée par pression"}]},
       cm2={"paires": [{"g": "Feldspath", "d": "Fondant extrait d'un gisement rocheux"},
                       {"g": "Sable de silice", "d": "Dégraissant lavé, tamisé et parfois broyé"},
                       {"g": "Chamotte", "d": "Dégraissant simple, fait d'argile déjà cuite"},
                       {"g": "Concasseur à mâchoires", "d": "La roche est écrasée par pression"},
                       {"g": "Concasseur à percussion", "d": "La roche éclate sous les chocs"},
                       {"g": "Tessons broyés", "d": "Débris de biscuits broyés puis tamisés"}]},
       lecon="matieres-dures", partie="partie IV"),

    en("5-2", "Les trois échantillons", "tri",
       {"cm1": "Trois bacs attendent : feldspath, sable de silice et chamotte. Range chaque étiquette dans le bon bac.",
        "cm2": "Range les neuf étiquettes dans le bon bac : feldspath, sable de silice ou chamotte."},
       "Feldspath : gisement rocheux, explosifs, gros blocs concassés puis broyés et tamisés. Sable de silice : en surface (pelleteuse) ou enfoui (on retire la couche supérieure), puis lavé, tamisé, parfois broyé. Chamotte : tessons broyés et tamisés, ou argile calcinée à une température plus haute que la cuisson de la pâte, puis broyée et tamisée.",
       {"cm1": ["Les explosifs servent pour la roche.", "Le sable se lave.", "La chamotte vient d'une argile déjà cuite."],
        "cm2": ["Les blocs de roche sont ceux du feldspath.", "Fontainebleau : un sable de surface.", "Calcinée = chauffée plus fort que la pâte."]},
       cm1={"colonnes": [{"id": "fel", "titre": "Feldspath"}, {"id": "sab", "titre": "Sable de silice"}, {"id": "cha", "titre": "Chamotte"}],
            "cartes": [{"txt": "Extrait avec des explosifs", "col": "fel"}, {"txt": "Gros blocs de roche concassés", "col": "fel"},
                       {"txt": "Lavé pour enlever l'argile", "col": "sab"}, {"txt": "Extrait avec une pelleteuse", "col": "sab"},
                       {"txt": "Débris de biscuits broyés", "col": "cha"}, {"txt": "Argile déjà cuite, puis broyée", "col": "cha"}]},
       cm2={"colonnes": [{"id": "fel", "titre": "Feldspath"}, {"id": "sab", "titre": "Sable de silice"}, {"id": "cha", "titre": "Chamotte"}],
            "cartes": [{"txt": "Gisement rocheux, techniques minières", "col": "fel"}, {"txt": "Concassé, broyé puis tamisé", "col": "fel"}, {"txt": "Sert de fondant", "col": "fel"},
                       {"txt": "Sable de Fontainebleau, en surface", "col": "sab"}, {"txt": "Couche supérieure du sol retirée pour l'atteindre", "col": "sab"}, {"txt": "Lavé, tamisé, parfois broyé", "col": "sab"},
                       {"txt": "Tessons de biscuits broyés puis tamisés", "col": "cha"}, {"txt": "Argile calcinée plus fort que la cuisson de la pâte", "col": "cha"},
                       {"txt": "Dégraissant simple", "col": "cha"}]},
       lecon="matieres-dures", partie="parties IV.1, IV.2 et IV.3"),

    en("5-3", "Les questions de Madame Aubry", "qcm",
       {"cm1": "Madame Aubry vérifie tes connaissances. Choisis la bonne réponse à chaque question.",
        "cm2": "Madame Aubry attend des réponses précises. Réponds à ses trois questions."},
       "Pour atteindre un sable enfoui, on retire la couche supérieure du sol. Dans un concasseur à percussion, la roche éclate sous les chocs. La chamotte est de l'argile déjà cuite, puis broyée. Une argile calcinée est chauffée à une température plus haute que la cuisson de la pâte, puis broyée et tamisée. Après l'extraction, le sable est lavé, tamisé, et parfois broyé.",
       {"cm1": ["Il faut creuser pour atteindre le sable enfoui.", "Percussion = chocs.", "Chamotte = déjà cuite."],
        "cm2": ["Calcinée = chauffée plus fort.", "Les tessons sont des débris de biscuits.", "Le sable passe d'abord à l'eau."]},
       cm1={"questions": [
           {"q": "Pour atteindre un sable enfoui, on…", "options": ["retire la couche supérieure du sol", "attend la pluie", "utilise un aimant"], "bonne": 0, "explication": "On dégage le sable en retirant le dessus."},
           {"q": "Dans un concasseur à percussion, la roche…", "options": ["est écrasée par pression", "éclate sous les chocs", "fond"], "bonne": 1, "explication": "Elle est projetée à grande vitesse."},
           {"q": "La chamotte est…", "options": ["de l'argile déjà cuite, puis broyée", "un sable lavé", "un fondant"], "bonne": 0, "explication": "C'est un dégraissant simple."}]},
       cm2={"questions": [
           {"q": "Une argile calcinée est chauffée…", "options": ["moins que la cuisson de la pâte", "à une température plus haute que la cuisson de la pâte", "à la même température que la pâte"], "bonne": 1, "explication": "Elle est ensuite broyée et tamisée."},
           {"q": "Après son extraction, le sable de silice est…", "options": ["cuit puis aimanté", "lavé, tamisé et parfois broyé", "mélangé à de l'eau salée"], "bonne": 1, "explication": "Le lavage enlève l'argile et les impuretés."},
           {"q": "Pourquoi les concasseurs à mâchoires écrasent-ils la roche ?", "options": ["Par pression", "Par flottation", "Par magnétisme"], "bonne": 0, "explication": "Mâchoires, giratoire et cône écrasent par pression."}]},
       lecon="matieres-dures", partie="parties IV.2 et IV.3"),

    en("5-4", "Du bloc à la poudre", "ordre", {"cm2": "Remets dans l'ordre les quatre étapes de préparation d'une roche (le feldspath, par exemple), de la carrière à la matière prête."},
       "Roches et sables : extraire, concasser et broyer, tamiser, puis purifier si besoin (aimants ou flottation).",
       {"cm2": ["On commence par sortir la roche du gisement.", "Les blocs sont d'abord concassés, puis broyés.", "La purification n'est faite que si besoin."]},
       expert={"items": [{"txt": "Extraire", "rang": 1}, {"txt": "Concasser et broyer", "rang": 2}, {"txt": "Tamiser", "rang": 3}, {"txt": "Purifier (si besoin)", "rang": 4}]},
       lecon="matieres-dures", partie="partie I, « Vue d'ensemble »"),
]

TITRES = ["La carrière", "Le parc d'argile et le silo", "L'atelier de broyage", "La station d'épuration", "Le laboratoire des matières dures"]
SOUS = ["Pourquoi préparer, analyser le terrain, extraire", "Le pourrissement et la maturation", "Les machines à broyer l'argile",
        "Tamisage, déferrage, flottation et sécurité", "Feldspath, sable de silice et chamotte"]
ENIGMES = {
    "metadata": {
        "jeu": TITRE, "version": 1,
        "differenciation": "Essentiel (clé cm1) : 3 énigmes par salle (15). Expert (clé cm2) : 4 énigmes par salle (20). Le champ \"niveaux\": [\"CM2\"] réserve une énigme au niveau Expert.",
        "types": ["qcm", "vraifaux", "association", "ordre", "tri", "trous", "code", "intrus", "plan"],
        "sources": COURS + " (document de l'enseignant). Points à confirmer : A-VERIFIER.md.",
        "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-2\",\"legende\":\"…\",\"source\":\"…\"} (image dans assets/images/cartes/)."
    },
    "salles": [{"num": i + 1, "titre": f"{TITRES[i]} — {SOUS[i]}", "enigmes": s} for i, s in enumerate([S1, S2, S3, S4, S5])]
}

# =====================================================================================
# DIALOGUES (personnages inventés)
# =====================================================================================
P = {"maelle": ("Maëlle", "Apprentie en 2e année de CAP Décoration sur céramique, elle guide l'équipe"),
     "odile": ("Odile", "Cheffe de la carrière"),
     "malik": ("Malik", "Responsable du parc d'argile et des silos"),
     "karim": ("Karim", "Technicien de l'atelier de broyage"),
     "jade": ("Jade", "Technicienne de la station d'épuration"),
     "aubry": ("Madame Aubry", "Cheffe du laboratoire des matières dures")}
MOTS = ["ANALYSER", "REPOSER", "BROYER", "ÉPURER", "CONCASSER"]
DECORS = ["carriere", "parc", "broyage", "epuration", "dures"]
LIEUX = ["La carrière d'argile, à ciel ouvert", "Le parc d'argile et le silo, derrière la carrière", "L'atelier de broyage",
         "La station d'épuration", "Le laboratoire des matières dures"]
DESCR = ["Des gradins d'argile brune, une excavatrice à l'arrêt et un tas fraîchement extrait. Sur un panneau, une grille de carrés numérotés.",
         "Un grand tas d'argile sous la pluie, et, à côté, un silo sombre et humide. Un tableau affiche des dates et des pourcentages.",
         "Des machines alignées le long d'un convoyeur : meule, marteaux, cylindre à billes. Chaque poste a perdu sa plaque.",
         "Un tamis qui vibre, un tambour à aimants et une cellule pleine de bulles. Au mur, un panneau de sécurité.",
         "Des bacs d'échantillons, deux concasseurs miniatures et un tableau des matières dures. Madame Aubry vérifie une étiquette."]
SENS = [["À voir : les gradins d'argile brune", "À entendre : le moteur de l'excavatrice", "À sentir : la terre humide"],
        ["À voir : le grand tas sous la pluie", "À entendre : la pluie sur la bâche du silo", "À toucher : l'argile froide et humide"],
        ["À voir : les machines alignées", "À entendre : le grondement des meules", "À sentir : la poussière d'argile"],
        ["À voir : les bulles de la cellule", "À entendre : la vibration du tamis", "À toucher : l'aimant qui attire un clou"],
        ["À voir : les bacs d'échantillons", "À entendre : les cailloux dans le concasseur", "À sentir : le sable lavé"]]
INTRO = [("odile", "Bienvenue à la carrière. Maëlle m'a prévenue : sans le bon de lancement signé, le lot de pâte de demain ne peut pas partir. Je tamponne la première étape : l'extraction. Avant de vous donner mon tampon, je veux être sûre que vous savez pourquoi on prépare les matières, et comment on trouve la bonne argile."),
         ("malik", "Ici, on laisse faire le temps. L'argile qui sort de la carrière n'est pas prête : elle passe d'abord dehors, puis dans mon silo. Montrez-moi que vous savez ce qui se passe sous la pluie, et combien de temps ça prend : le tampon de l'étape deux est à ce prix."),
         ("karim", "Ça grince, ça gronde, ça casse : c'est l'atelier de broyage. Pas de panique, mais tous les postes ont perdu leur plaque ce matin, et je ne sais plus quelle machine fait quoi. Aidez-moi à tout remettre en place : le tampon de l'étape trois est pour vous."),
         ("jade", "On passe à la propreté : ici, on enlève ce qui n'a rien à faire dans une pâte. Tamis, aimants, flottation : chaque machine a son rôle. Et ici, la sécurité n'est pas une option : la poussière, ça ne pardonne pas. Prouvez-moi que vous la connaissez, et le tampon est à vous."),
         ("aubry", "Dernière étape : les matières dures. Le feldspath, le sable de silice, la chamotte : trois matières qui ne se modèlent pas, mais sans lesquelles la pâte ne tiendrait pas. Montrez-moi que vous savez d'où elles viennent et comment on les prépare, et le dernier tampon est à vous.")]
REUSSITE = [("odile", "Bien analysé ! Mon tampon porte le mot <b>ANALYSER</b> : on ne creuse jamais au hasard. Malik vous attend au parc d'argile."),
            ("malik", "Vous avez compris que le temps travaille pour nous. Mon tampon porte le mot <b>REPOSER</b> : l'argile a besoin de repos. Karim vous attend à l'atelier de broyage."),
            ("karim", "L'atelier est remis en ordre, merci ! Mon tampon porte le mot <b>BROYER</b>. Jade vous attend à la station d'épuration."),
            ("jade", "Station propre, équipe protégée : parfait. Mon tampon porte le mot <b>ÉPURER</b>. Il reste le laboratoire des matières dures : Madame Aubry vous attend.")]
FIN = ("maelle", "Madame Aubry vous a donné le dernier mot : <b>CONCASSER</b>. Vous avez les cinq tampons ! Écrivez les cinq mots dans le bon de lancement, dans l'ordre des salles : le lot de pâte pourra partir demain matin.")

DIALOGUES = {
    "metadata": {"jeu": TITRE, "sujet": "La préparation des matières premières des pâtes céramiques : pourquoi préparer, extraction, pourrissement, broyage, épuration, maturation, feldspath, sable de silice, chamotte — CAP Décoration sur céramique",
                 "niveaux": ["Essentiel", "Expert"], "sources": COURS},
    "personnages": {k: {"nom": v[0], "role": v[1]} for k, v in P.items()},
    "intro_accueil": "Bonjour, je suis Maëlle, apprentie en deuxième année. Bienvenue à la manufacture des Trois Fours ! Demain matin, un nouveau lot de pâte doit être lancé. Problème : le bon de lancement n'est pas signé. Pour qu'il le soit, chacune des cinq étapes de la préparation des matières premières doit être validée par son responsable, qui appose son tampon et vous donne un mot. Les cinq mots ouvriront le bon de lancement. On commence par la carrière ?",
    "salles": []
}
for i in range(5):
    s = {"num": i + 1, "titre": TITRES[i], "decor": DECORS[i], "motCle": MOTS[i], "lieu": LIEUX[i], "description": DESCR[i], "sens": SENS[i],
         "dialogue_intro": {"perso": INTRO[i][0], "nom": P[INTRO[i][0]][0], "texte": INTRO[i][1]}}
    if i < 4:
        s["dialogue_reussite"] = {"perso": REUSSITE[i][0], "nom": P[REUSSITE[i][0]][0], "texte": REUSSITE[i][1]}
    else:
        s["dialogue_fin"] = {"perso": FIN[0], "nom": P[FIN[0]][0], "texte": FIN[1]}
    DIALOGUES["salles"].append(s)

# =====================================================================================
# LEÇONS
# =====================================================================================
LECONS = {"lecons": [
    {"id": "gisement-extraction", "salle": 1, "icone": "I", "titre": "Pourquoi préparer ? Trouver et extraire l'argile", "duree": "4 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Expliquer pourquoi on prépare les matières premières", "Citer dans l'ordre les étapes de préparation de l'argile", "Expliquer comment on trouve et on extrait l'argile"],
     "contenu": {
         "cm1": "<h4>Pourquoi préparer ?</h4><p>Dans la nature, les matières premières ne sont <b>pas prêtes à l'emploi</b> : elles contiennent des <b>impuretés</b>, des morceaux trop gros, trop d'eau. On les prépare pour que la pâte soit <b>stable</b> et de <b>qualité constante</b>.</p><h4>Les étapes pour l'argile</h4><p><b>Analyser le terrain</b>, <b>extraire</b>, <b>pourrissement</b>, <b>broyer</b>, <b>épurer</b>, <b>maturation</b>.</p><div class='encadre'>Avant d'extraire, on découpe le terrain en carrés (une <b>grille</b>) et on prélève <b>un échantillon par carré</b> : on trouve ainsi la <b>meilleure couche</b>.</div>",
         "cm2": "<h4>Pourquoi préparer ?</h4><p>Dans la nature, les matières premières ne sont <b>pas prêtes à l'emploi</b> : elles contiennent des <b>impuretés</b>, des morceaux trop gros, trop d'eau, des grains de tailles différentes. Il faut les <b>extraire</b>, les <b>casser</b>, les <b>trier</b>, les <b>nettoyer</b>, puis parfois les laisser <b>reposer</b>. Ainsi la pâte est <b>stable</b> et de <b>qualité constante</b> : la pièce se modèle, sèche et cuit toujours de la même façon.</p><h4>Trouver la bonne couche</h4><p>Un <b>gisement</b> est fait de plusieurs <b>couches</b> (les strates), toutes <b>différentes</b>. Avant d'extraire, on <b>analyse le terrain</b> : on le découpe en carrés, c'est une <b>grille</b>, et on prélève <b>un échantillon par carré</b>. On repère ainsi la <b>meilleure couche</b>.</p><h4>Extraire</h4><p>L'argile est extraite dans des <b>carrières à ciel ouvert</b>, avec des <b>excavatrices</b> et des <b>camions-bennes</b>. En général, l'extraction a lieu à <b>l'entrée de l'hiver</b>.</p><div class='encadre'>Une argile <b>« maigre »</b> (sableuse) contient beaucoup d'<b>impuretés</b> : produit de moins bonne qualité. Une argile <b>« grasse »</b> (plastique) est quasiment <b>pure</b> : produit de meilleure qualité.</div><h4>Deux filières</h4><p>Pour l'<b>argile</b> : analyser le terrain, extraire, pourrissement, broyer, épurer, maturation. Pour les <b>roches et sables</b> : extraire, concasser et broyer, tamiser, purifier si besoin.</p>"},
     "lexique": [{"mot": "gisement", "def": "endroit où une matière (argile, roche, sable) s'est accumulée naturellement"}, {"mot": "impureté", "def": "matière qu'on ne veut pas dans la pâte (racines, cailloux, fer)"},
                 {"mot": "strates", "def": "couches d'un gisement, toutes différentes"}, {"mot": "argile grasse", "def": "argile plastique, quasiment pure"}],
     "frise": [{"date": "1", "evt": "analyser le terrain"}, {"date": "2", "evt": "extraire"}, {"date": "3", "evt": "pourrissement"},
               {"date": "4", "evt": "broyer"}, {"date": "5", "evt": "épurer"}, {"date": "6", "evt": "maturation"}],
     "frise_titre": "Les six étapes de préparation de l'argile",
     "document": {"type": "text", "titre": "Les deux argiles", "contenu": "Argile « maigre » (sableuse) : beaucoup d'impuretés, produit de moins bonne qualité. Argile « grasse » (plastique) : quasiment pure, produit de meilleure qualité.", "source": COURS + ", partie II.1."},
     "sources": COURS + ", parties I et II.1."},
    {"id": "pourrissement-maturation", "salle": 2, "icone": "II", "titre": "Le pourrissement et la maturation", "duree": "3 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Expliquer le pourrissement de l'argile", "Expliquer la maturation et le taux d'humidité"],
     "contenu": {
         "cm1": "<h4>Le pourrissement</h4><p>L'argile est stockée <b>dehors</b> pendant <b>3 à 24 mois</b>. Pluie, gel et dégel <b>fragmentent</b> les grains. Résultat : l'argile devient plus <b>plastique</b> et plus <b>résistante</b>.</p><h4>La maturation</h4><p>L'argile est entreposée <b>au moins 2 semaines</b> dans un <b>silo humide et sombre</b>. Son <b>taux d'humidité</b> baisse : de <b>18-22 %</b> à <b>13-18 %</b>.</p>",
         "cm2": "<h4>Le pourrissement : le repos dehors</h4><p>L'argile est <b>stockée dehors</b> pendant <b>3 à 24 mois</b>. Elle subit la <b>pluie</b>, le <b>gel</b> et le <b>dégel</b> : les grains se <b>fragmentent</b>. Des <b>bactéries</b> décomposent les restes de plantes. Résultat : l'argile devient plus <b>plastique</b> et plus <b>résistante</b>.</p><h4>La maturation : le repos au silo</h4><p>Après le broyage et l'épuration, l'argile est entreposée <b>au moins 2 semaines</b> dans un <b>silo humide et sombre</b>. Ses <b>propriétés</b> changent et son <b>taux d'humidité</b> (la quantité d'eau) baisse.</p><div class='encadre'>Argile <b>fraîchement extraite</b> : <b>18 %</b> à <b>22 %</b> d'eau. Après la <b>maturation</b> : <b>13 %</b> à <b>18 %</b>.</div><h4>Deux repos, deux effets</h4><p>Le pourrissement agit sur les <b>grains</b> et les <b>restes de plantes</b>, dehors, pendant des <b>mois</b>. La maturation agit sur l'<b>humidité</b>, au silo, pendant des <b>semaines</b>. Les deux rendent l'argile prête à l'emploi.</p><h4>Pourquoi laisser reposer ?</h4><p>Une matière première n'est jamais prête à l'emploi en sortant du gisement. En la laissant <b>reposer</b>, on obtient une argile plus <b>plastique</b> et plus <b>résistante</b>, donc une pâte <b>stable</b>, dont la qualité reste constante d'un lot à l'autre.</p>"},
     "lexique": [{"mot": "pourrissement", "def": "repos de l'argile dehors, 3 à 24 mois"}, {"mot": "maturation", "def": "repos de l'argile au silo, au moins 2 semaines"},
                 {"mot": "taux d'humidité", "def": "quantité d'eau contenue dans l'argile"}, {"mot": "silo", "def": "grand réservoir où l'on entrepose la matière"}],
     "frise": [{"date": "dehors", "evt": "pourrissement : 3 à 24 mois, pluie, gel et dégel"}, {"date": "au silo", "evt": "maturation : au moins 2 semaines, humidité de 18-22 % à 13-18 %"}],
     "frise_titre": "Les deux repos de l'argile",
     "document": {"type": "text", "titre": "Le taux d'humidité de l'argile", "contenu": "Argile fraîchement extraite : 18 % à 22 %. Après la maturation : 13 % à 18 %.", "source": COURS + ", partie III.3."},
     "sources": COURS + ", parties II.2 et III.3."},
    {"id": "broyage", "salle": 3, "icone": "III", "titre": "Le broyage de l'argile", "duree": "3 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Expliquer ce qu'est le broyage", "Connaître le principe des principales machines à broyer l'argile"],
     "contenu": {
         "cm1": "<p>Le <b>broyage</b> casse l'argile en <b>petits morceaux</b> : on réduit sa taille.</p><ul><li><b>Broyeur à meule</b> : deux meules <b>écrasent</b> l'argile.</li><li><b>Brise-mottes</b> : rouleaux ou marteaux <b>cassent les mottes</b>.</li><li><b>Broyeur à marteaux</b> : des marteaux <b>frappent</b> l'argile ; elle sort par une <b>grille</b>.</li><li><b>Broyeur à billes</b> : un cylindre rempli de <b>billes</b> ; le <b>frottement</b> fragmente l'argile.</li></ul>",
         "cm2": "<p>Le <b>broyage</b> casse l'argile en petits morceaux : on <b>réduit sa taille</b>. Plusieurs machines sont utilisées.</p><ul><li><b>Broyeur à meule</b> : deux <b>meules</b> qui tournent <b>écrasent</b> l'argile.</li><li><b>Brise-mottes</b> : des rouleaux ou des marteaux <b>cassent les mottes</b>.</li><li><b>Désagrégateur</b> : une chemise lisse et une chemise striée avec des <b>lames</b> <b>désagrègent</b> l'argile.</li><li><b>Broyeur à marteaux</b> : des marteaux qui tournent vite <b>frappent</b> l'argile ; elle sort quand elle est assez fine, à travers une <b>grille</b>.</li><li><b>Broyeur à billes (alsing)</b> : un cylindre qui tourne, rempli de <b>billes</b> ; le <b>frottement</b> fragmente l'argile.</li></ul><div class='encadre'>Le broyage à billes se fait <b>à sec</b> ou <b>avec de l'eau</b> : <b>un tiers de billes, un tiers d'argile, un tiers d'eau</b>. Le broyeur à billes sert aussi pour les <b>roches</b>.</div><h4>Ne pas confondre</h4><p>Un broyeur <b>réduit la taille</b>. Un tamis <b>trie</b> les grains selon leur taille : il intervient à l'<b>épuration</b>, pas au broyage.</p><h4>Choisir sa machine</h4><p>Chaque machine agit autrement : la meule <b>écrase</b>, le brise-mottes <b>casse</b>, le désagrégateur <b>désagrège</b>, les marteaux <b>frappent</b>, les billes <b>frottent</b>. Après le broyage, l'argile passe à l'<b>épuration</b> pour être débarrassée de ses impuretés.</p>"},
     "lexique": [{"mot": "motte", "def": "gros morceau d'argile compact"}, {"mot": "alsing", "def": "autre nom du broyeur à billes"},
                 {"mot": "broyer", "def": "réduire en petits morceaux ou en poudre"}, {"mot": "désagréger", "def": "défaire l'argile en séparant ses morceaux"}],
     "frise": [{"date": "écraser", "evt": "broyeur à meule"}, {"date": "casser", "evt": "brise-mottes"}, {"date": "désagréger", "evt": "désagrégateur"},
               {"date": "frapper", "evt": "broyeur à marteaux"}, {"date": "frotter", "evt": "broyeur à billes"}],
     "frise_titre": "Un verbe pour chaque machine",
     "document": {"type": "text", "titre": "Le broyage à l'eau", "contenu": "Dans un broyeur à billes, le broyage peut se faire avec de l'eau : un tiers de billes, un tiers d'argile, un tiers d'eau.", "source": COURS + ", partie III.1."},
     "sources": COURS + ", partie III.1."},
    {"id": "epuration-purification", "salle": 4, "icone": "IV", "titre": "L'épuration, la purification et la sécurité", "duree": "4 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Dire à quoi servent le tamis vibrant et le séparateur magnétique", "Expliquer la flottation", "Connaître les règles de sécurité face aux poussières"],
     "contenu": {
         "cm1": "<h4>L'épuration de l'argile</h4><p>Le <b>tamis vibrant</b> trie les grains selon leur taille : il élimine les <b>impuretés</b> (feuilles, racines) et les grains trop gros. Le <b>déferrage</b> utilise des <b>aimants</b> qui attirent les particules de <b>fer</b>.</p><h4>La flottation</h4><p>Dans un mélange d'eau et de poudre, on ajoute des <b>réactifs</b> et de l'<b>air</b> : une matière monte en <b>mousse</b>, l'autre reste au fond.</p><div class='encadre'>Sécurité : les poussières fines sont dangereuses pour les <b>poumons</b>. <b>Masque</b>, aspiration ou humide, et <b>jamais de balayage à sec</b>.</div>",
         "cm2": "<h4>L'épuration de l'argile</h4><p>L'épuration enlève les <b>impuretés</b>. L'<b>épuration mécanique</b> est le <b>tamisage</b> : un <b>tamis vibrant</b> trie les grains selon leur taille et élimine les impuretés (feuilles, racines…) et les grains trop gros. L'<b>épuration magnétique</b> est le <b>déferrage</b> : des <b>aimants</b> ou <b>électro-aimants</b> attirent les particules de <b>fer</b>, qui sont séparées de l'argile (sèche ou en barbotine).</p><h4>Purifier les roches et les sables</h4><p>Comme pour l'argile, la <b>séparation magnétique</b> enlève le fer. La <b>flottation</b> sépare deux matières : on ajoute des <b>réactifs</b> et de l'<b>air</b> dans un mélange eau + poudre ; une des matières <b>s'accroche aux bulles</b> et <b>monte en mousse</b>, l'autre <b>reste au fond</b>. Exemple : séparer le <b>feldspath</b> de la <b>silice</b>.</p><div class='encadre'><b>Sécurité</b> : le broyage, le concassage et le tamisage produisent des <b>poussières fines</b> (silice, argile sèche) dangereuses pour les <b>poumons</b>. Porter un <b>masque</b>, travailler <b>avec aspiration</b> ou <b>à l'humide</b>, et ne jamais <b>balayer à sec</b>.</div><h4>Retenir</h4><p>Le <b>tamis</b> trie selon la <b>taille</b>, l'<b>aimant</b> retire le <b>fer</b>, la <b>flottation</b> sépare deux matières grâce aux <b>bulles</b>. Toutes ces opérations visent le même but : une matière <b>propre</b>, sans impureté, pour une pâte de qualité constante.</p>"},
     "lexique": [{"mot": "épuration", "def": "action d'enlever les impuretés"}, {"mot": "barbotine", "def": "argile mélangée à de l'eau"},
                 {"mot": "déferrage", "def": "retrait des particules de fer avec des aimants"}, {"mot": "flottation", "def": "séparation de deux matières grâce à des bulles"}],
     "frise": [{"date": "tamis vibrant", "evt": "trie selon la taille, retire les impuretés"}, {"date": "aimants", "evt": "attirent le fer"},
               {"date": "flottation", "evt": "une matière monte en mousse, l'autre reste au fond"}],
     "frise_titre": "Trois moyens d'épurer ou de purifier",
     "document": {"type": "text", "titre": "Le panneau de sécurité", "contenu": "Poussières fines (silice, argile sèche) : danger pour les poumons. Porter un masque. Travailler avec aspiration ou à l'humide. Ne jamais balayer à sec.", "source": COURS + ", encadré « Sécurité »."},
     "sources": COURS + ", parties III.2 et IV.4."},
    {"id": "matieres-dures", "salle": 5, "icone": "V", "titre": "Les matières dures : feldspath, sable de silice, chamotte", "duree": "4 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Dire comment on obtient le feldspath, le sable de silice et la chamotte", "Distinguer les deux types de concasseurs", "Distinguer fondant et dégraissant"],
     "contenu": {
         "cm1": "<ul><li><b>Feldspath</b> (<b>fondant</b>) : dans un gisement rocheux, extrait avec des <b>explosifs</b> ; les blocs sont <b>concassés</b>, <b>broyés</b>, <b>tamisés</b>.</li><li><b>Sable de silice</b> (<b>dégraissant</b>) : extrait <b>en surface</b> à la pelleteuse, ou <b>enfoui</b> ; puis <b>lavé</b>, <b>tamisé</b>.</li><li><b>Chamotte</b> (<b>dégraissant</b>) : <b>argile déjà cuite</b>, <b>broyée</b> et tamisée.</li></ul><div class='encadre'>Concasseur à <b>mâchoires</b> : la roche est <b>écrasée</b>. Concasseur à <b>percussion</b> : la roche <b>éclate sous les chocs</b>.</div>",
         "cm2": "<h4>Le feldspath (fondant)</h4><p>Le feldspath, la pegmatite et la néphéline sont dans des <b>gisements rocheux</b>. On les extrait avec des <b>techniques minières</b>, souvent des <b>explosifs</b>, pour obtenir de gros <b>blocs de roche</b>. Ils sont <b>concassés</b> (réduits en morceaux de quelques centimètres ou millimètres), puis <b>broyés</b> et <b>tamisés</b>.</p><p>Concasseurs <b>à mâchoires, giratoire, à cône</b> : la roche est <b>écrasée par pression</b>. Concasseur <b>à percussion</b> : la roche est projetée à grande vitesse et <b>éclate sous les chocs</b>.</p><h4>Le sable de silice (dégraissant)</h4><p>Le sable est <b>en surface</b> (par exemple le sable de Fontainebleau) : on l'extrait directement avec une <b>pelleteuse</b>. S'il est <b>enfoui</b>, on <b>retire la couche supérieure</b> du sol. Ensuite, il est <b>lavé</b> (pour enlever l'argile et les impuretés), <b>tamisé</b>, et parfois <b>broyé</b>.</p><h4>La chamotte (dégraissant)</h4><p>Les <b>tessons broyés</b> : des débris de <b>biscuits</b> (pièces déjà cuites) sont broyés puis tamisés. Les <b>argiles calcinées</b> : de l'argile est <b>calcinée</b> à une température <b>plus haute</b> que la cuisson de la pâte, puis broyée et tamisée.</p>"},
     "lexique": [{"mot": "chamotte", "def": "argile déjà cuite, puis broyée"}, {"mot": "fondant", "def": "matière qui aide la pâte à fondre à la cuisson"},
                 {"mot": "concasser", "def": "casser une roche en morceaux de quelques centimètres ou millimètres"}, {"mot": "calciner", "def": "chauffer très fort une argile"}],
     "frise": [{"date": "feldspath", "evt": "gisement rocheux, explosifs, concassage, broyage, tamisage"}, {"date": "sable de silice", "evt": "surface ou enfoui, lavage, tamisage, parfois broyage"},
               {"date": "chamotte", "evt": "tessons ou argile calcinée, broyage, tamisage"}],
     "frise_titre": "Trois matières dures, trois préparations",
     "document": {"type": "text", "titre": "Les deux types de chamotte", "contenu": "Tessons broyés : des débris de biscuits sont broyés puis tamisés. Argiles calcinées : de l'argile est calcinée à une température plus haute que la cuisson de la pâte, puis broyée et tamisée.", "source": COURS + ", partie IV.3."},
     "sources": COURS + ", parties IV.1 à IV.3."}
]}

# =====================================================================================
# ÉVALUATIONS
# =====================================================================================
def q(t, o, b, pts=None):
    d = {"q": t, "options": o, "bonne": b}
    if pts:
        d["pts"] = pts
    return d


EVAL = {
    "metadata": {"sujet": "La préparation des matières premières", "niveaux": ["Essentiel", "Expert"],
                 "programme": "CAP Décoration sur céramique — technologie des matériaux : préparation des matières premières des pâtes céramiques.", "sources": COURS},
    "quizz_final": {
        "CM1": [q("Pourquoi prépare-t-on les matières premières ?", ["pour qu'elles soient moins chères", "pour obtenir une pâte stable et de qualité constante", "pour les colorer"], 1),
                q("Quelle est la première étape de préparation de l'argile ?", ["le broyage", "l'analyse du terrain", "la maturation"], 1),
                q("Pendant le pourrissement, l'argile est stockée…", ["dehors", "dans un four", "dans un silo sombre"], 0),
                q("Le tamis vibrant sert à…", ["trier les grains selon leur taille", "attirer le fer", "cuire l'argile"], 0),
                q("La chamotte est…", ["de l'argile déjà cuite, puis broyée", "un sable lavé", "un fondant"], 0)],
        "CM2": [q("Combien de temps dure le pourrissement ?", ["quelques jours", "de 3 à 24 mois", "au moins 2 semaines"], 1),
                q("Après la maturation, le taux d'humidité de l'argile est de…", ["18 % à 22 %", "13 % à 18 %", "5 % à 8 %"], 1),
                q("Quelle machine broie à l'aide de billes ?", ["le désagrégateur", "le broyeur à billes", "le concasseur à percussion"], 1),
                q("Quelle technique sépare le feldspath de la silice ?", ["la flottation", "le tamisage", "le déferrage"], 0),
                q("Pour atteindre un sable enfoui, on…", ["retire la couche supérieure du sol", "utilise des explosifs", "attend la pluie"], 0)]},
    "qcm": {
        "CM1": [q("L'argile est extraite dans…", ["une carrière à ciel ouvert", "un atelier fermé", "un four"], 0, 1), q("Avant d'extraire, on prélève un échantillon par…", ["carré de la grille", "camion", "mois"], 0, 1),
                q("Un gisement, c'est…", ["un endroit où une matière s'est accumulée naturellement", "une machine", "une recette"], 0, 1), q("Le pourrissement dure…", ["de 3 à 24 mois", "quelques heures", "une semaine"], 0, 1),
                q("La maturation a lieu dans…", ["un silo humide et sombre", "un four", "une carrière"], 0, 1), q("Le broyeur à marteaux laisse sortir l'argile par…", ["une grille", "un aimant", "une meule"], 0, 1),
                q("Les aimants servent à enlever…", ["le fer", "l'eau", "le sable"], 0, 1), q("Pour se protéger des poussières, on porte…", ["un masque", "un chapeau", "des lunettes de soleil"], 0, 1),
                q("Le feldspath est un…", ["fondant", "tamis", "silo"], 0, 1), q("Le sable de silice est un…", ["dégraissant", "fondant", "broyeur"], 0, 1)],
        "CM2": [q("Une argile « grasse » est…", ["quasiment pure", "sableuse", "toujours rouge"], 0, 1), q("En général, l'extraction a lieu…", ["à l'entrée de l'hiver", "en plein été", "la nuit"], 0, 1),
                q("Pendant le pourrissement, les bactéries…", ["décomposent les restes de plantes", "cuisent l'argile", "colorent l'argile"], 0, 1), q("La maturation dure…", ["au moins 2 semaines", "3 à 24 mois", "une heure"], 0, 1),
                q("Le désagrégateur fonctionne avec…", ["des lames", "des aimants", "des billes seulement"], 0, 1), q("Le broyage à l'eau d'un broyeur à billes : proportions…", ["⅓ billes, ⅓ argile, ⅓ eau", "½ eau, ½ argile", "⅔ billes, ⅓ eau"], 0, 1),
                q("Le déferrage fonctionne avec l'argile…", ["sèche ou en barbotine", "uniquement cuite", "uniquement gelée"], 0, 1), q("La flottation sépare des matières grâce à…", ["des bulles", "des aimants", "des meules"], 0, 1),
                q("Un concasseur à percussion…", ["projette la roche à grande vitesse", "écrase par pression", "trie les grains"], 0, 1), q("La chamotte « argile calcinée » est chauffée…", ["plus haut que la cuisson de la pâte", "moins que la pâte", "à l'eau froide"], 0, 1),
                q("Les tessons broyés sont…", ["des débris de biscuits", "des cailloux de rivière", "des morceaux de verre"], 0, 1), q("Le sable de Fontainebleau est un exemple de sable…", ["en surface", "enfoui", "calciné"], 0, 1)]},
    "questions_fermees": {
        "CM1": [{"q": "Dans la nature, les matières premières sont prêtes à l'emploi.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "L'argile est extraite dans des carrières à ciel ouvert.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Le déferrage enlève le fer avec des aimants.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "La chamotte est de l'argile déjà cuite, puis broyée.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Cite les six étapes de préparation de l'argile.", "type": "court", "rep": "analyse du terrain, extraction, pourrissement, broyage, épuration, maturation", "pts": 1},
                {"q": "Cite une machine qui broie l'argile.", "type": "court", "rep": "broyeur à meule, brise-mottes, désagrégateur, broyeur à marteaux, broyeur à billes", "pts": 1},
                {"q": "À quoi sert un tamis vibrant ?", "type": "court", "rep": "à trier les grains selon leur taille et à éliminer les impuretés", "pts": 1},
                {"q": "Cite une règle de sécurité face aux poussières.", "type": "court", "rep": "masque, aspiration ou humide, ne jamais balayer à sec", "pts": 1}],
        "CM2": [{"q": "Le pourrissement dure quelques jours.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "L'argile « maigre » est quasiment pure.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "La flottation sépare le feldspath de la silice.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Le sable de silice se trouve toujours enfoui.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Explique pourquoi on prépare les matières premières.", "type": "court", "rep": "elles ne sont pas prêtes à l'emploi (impuretés, morceaux trop gros, trop d'eau) ; on obtient une pâte stable et de qualité constante", "pts": 2},
                {"q": "Décris la maturation de l'argile.", "type": "court", "rep": "au moins 2 semaines dans un silo humide et sombre ; le taux d'humidité baisse (de 18-22 % à 13-18 %)", "pts": 2},
                {"q": "Distingue un concasseur à mâchoires et un concasseur à percussion.", "type": "court", "rep": "mâchoires : la roche est écrasée par pression ; percussion : la roche éclate sous les chocs", "pts": 2},
                {"q": "Explique comment on obtient la chamotte (deux types).", "type": "court", "rep": "tessons broyés puis tamisés ; argile calcinée à une température plus haute que la cuisson de la pâte, puis broyée et tamisée", "pts": 2}]},
    "etudes_documents": {
        "CM1": [{"titre": "Le taux d'humidité de l'argile", "document": {"contenu": "Argile fraîchement extraite : 18 % à 22 %. Après la maturation : 13 % à 18 %.", "source": COURS + ", partie III.3."},
                 "questions": [{"q": "Quelle est l'humidité de l'argile fraîchement extraite ?", "type": "court", "rep": "18 % à 22 %", "pts": 1},
                               {"q": "Que devient le taux d'humidité après la maturation ?", "type": "court", "rep": "il baisse (13 % à 18 %)", "pts": 1}]},
                {"titre": "Le panneau de sécurité", "document": {"contenu": "Poussières fines (silice, argile sèche) : danger pour les poumons. Porter un masque. Travailler avec aspiration ou à l'humide. Ne jamais balayer à sec.", "source": COURS + ", encadré « Sécurité »."},
                 "questions": [{"q": "Pourquoi les poussières sont-elles dangereuses ?", "type": "court", "rep": "elles sont dangereuses pour les poumons", "pts": 1},
                               {"q": "Cite deux règles à respecter.", "type": "court", "rep": "porter un masque ; travailler avec aspiration ou à l'humide ; ne jamais balayer à sec", "pts": 2}]}],
        "CM2": [{"titre": "Argile maigre et argile grasse", "document": {"contenu": "Argile « maigre » (sableuse) : beaucoup d'impuretés, produit de moins bonne qualité. Argile « grasse » (plastique) : quasiment pure, produit de meilleure qualité.", "source": COURS + ", partie II.1."},
                 "questions": [{"q": "Quelle argile est la plus pure ?", "type": "court", "rep": "l'argile grasse", "pts": 1},
                               {"q": "Pourquoi l'argile maigre donne-t-elle un produit de moins bonne qualité ?", "type": "court", "rep": "elle contient beaucoup d'impuretés", "pts": 1},
                               {"q": "Avec quelle méthode repère-t-on la meilleure couche d'un gisement ?", "type": "court", "rep": "on découpe le terrain en carrés (grille) et on prélève un échantillon par carré", "pts": 2}]},
                {"titre": "Les deux types de chamotte", "document": {"contenu": "Tessons broyés : des débris de biscuits sont broyés puis tamisés. Argiles calcinées : de l'argile est calcinée à une température plus haute que la cuisson de la pâte, puis broyée et tamisée.", "source": COURS + ", partie IV.3."},
                 "questions": [{"q": "Qu'est-ce qu'un tesson broyé ?", "type": "court", "rep": "un débris de biscuit (pièce déjà cuite) broyé puis tamisé", "pts": 1},
                               {"q": "Que signifie « calcinée » ici ?", "type": "court", "rep": "chauffée à une température plus haute que la cuisson de la pâte", "pts": 1}]}]},
    "fiches_preparatoires": [
        {"salle": i + 1, "titre": f"{TITRES[i]} — {SOUS[i]}", "objectifs": LECONS["lecons"][i]["objectifs"],
         "vocabulaire": LECONS["lecons"][i]["lexique"][:4], "contexte": DESCR[i]} for i in range(5)]
}

# =====================================================================================
# LEÇONS A4 (visuels SVG dessinés par script, jamais par IA)
# =====================================================================================
def svg_filiere():
    et = ["Analyser", "Extraire", "Pourrissement", "Broyer", "Épurer", "Maturation"]
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 150" role="img" aria-label="Les six étapes de préparation de l\'argile" font-family="Segoe UI, Helvetica, Arial, sans-serif">',
         '<rect width="380" height="150" fill="#f3f8fd"/>']
    for k, n in enumerate(et):
        x = 12 + k * 61
        s.append(f'<rect x="{x}" y="42" width="54" height="50" rx="6" fill="#2f75b5"/><text x="{x+27}" y="22" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f4c81">{k+1}</text>'
                 f'<text x="{x+27}" y="71" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#fff">{n}</text>')
        if k < 5:
            s.append(f'<path d="M{x+55} 67 l5 0" stroke="#0f4c81" stroke-width="2"/>')
    s.append('<text x="190" y="125" font-size="11" text-anchor="middle" fill="#0b2a4a">De la carrière à la matière prête à l\'emploi.</text></svg>')
    return "".join(s)


def svg_humidite():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 170" role="img" aria-label="Taux d\'humidité avant et après la maturation" font-family="Segoe UI, Helvetica, Arial, sans-serif">',
         '<rect width="380" height="170" fill="#f3f8fd"/>']
    for k, (n, a, b) in enumerate([("Argile fraîche", 18, 22), ("Après maturation", 13, 18)]):
        y = 40 + k * 50
        s.append(f'<text x="14" y="{y+16}" font-size="12" font-weight="bold" fill="#0b2a4a">{n}</text>'
                 f'<rect x="150" y="{y}" width="{(b-a)*20}" height="22" rx="4" fill="#2f75b5" transform="translate({(a-13)*20} 0)"/>'
                 f'<text x="{150+(a-13)*20+(b-a)*10}" y="{y+16}" font-size="11" font-weight="bold" text-anchor="middle" fill="#fff">{a} à {b} %</text>')
    s.append('<text x="190" y="150" font-size="11" text-anchor="middle" fill="#0b2a4a">Le taux d\'humidité baisse pendant la maturation.</text></svg>')
    return "".join(s)


A4 = {"_commentaire": "Généré par outils/generer-matieres-premieres.py — ne pas modifier à la main.",
      "jeu": {"titre": TITRE, "matiere": "Technologie céramique", "theme": "La préparation des matières premières", "couleur": "#0F4C81", "accent": "#C2410C", "couleur_pale": "#DCEEFF", "accent_pale": "#FFE9DB"},
      "lecons": {
          "gisement-extraction": {"competence": "Expliquer pourquoi on prépare les matières premières ; citer dans l'ordre les étapes de préparation de l'argile.",
                                  "visuels": [{"type": "svg", "titre": "Les six étapes de préparation de l'argile", "legende": "De la carrière à la matière prête à l'emploi.", "svg": svg_filiere(), "etiquette": "Schéma", "source": COURS + ", partie I."}]},
          "pourrissement-maturation": {"competence": "Expliquer le pourrissement et la maturation de l'argile.",
                                       "visuels": [{"type": "svg", "titre": "Le taux d'humidité de l'argile", "legende": "Avant et après la maturation.", "svg": svg_humidite(), "etiquette": "Schéma", "source": COURS + ", partie III.3."}]},
          "broyage": {"competence": "Dire à quoi sert le broyage et connaître le principe des principales machines.", "visuels": []},
          "epuration-purification": {"competence": "Dire à quoi servent le tamis et le séparateur magnétique ; connaître les règles de sécurité.", "visuels": []},
          "matieres-dures": {"competence": "Expliquer comment on obtient le sable de silice, la chamotte et le feldspath.", "visuels": []}}}

if __name__ == "__main__":
    ecrire("enigmes.json", ENIGMES)
    ecrire("dialogues.json", DIALOGUES)
    ecrire("lecons.json", LECONS)
    ecrire("evaluations.json", EVAL)
    ecrire("lecons-a4.json", A4)
    n1 = sum(1 for s in ENIGMES["salles"] for e in s["enigmes"] if "niveaux" not in e)
    n2 = sum(len(s["enigmes"]) for s in ENIGMES["salles"])
    print(f"✔ {TITRE} : {n1} énigmes Essentiel, {n2} énigmes Expert, 5 leçons, évaluations écrites dans {os.path.relpath(DATA)}")
