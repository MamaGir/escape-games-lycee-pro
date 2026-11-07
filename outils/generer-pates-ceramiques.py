#!/usr/bin/env python3
"""Génère les données du jeu « Les fiches du four » (Les pâtes céramiques, CAP Décoration sur céramique).

Ne pas modifier les JSON à la main : éditer ce script puis relancer
    python outils/generer-pates-ceramiques.py
Niveaux : les clés internes restent « cm1 » / « cm2 » (format du moteur commun) ;
l'interface du lycée affiche « Essentiel » (cm1) et « Expert » (cm2) — voir commun/lycee-pro/libelles.js.
Source du contenu : chapitre « Les pâtes céramiques » (CAP 1, version simplifiée) de l'enseignant.
"""
import json, os

ICI = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(ICI), "pates-ceramiques", "assets", "data")
TITRE = "Les fiches du four"
COURS = "Chapitre « Les pâtes céramiques », CAP 1"


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
# SALLE 1 — Le magasin des matières premières (composition d'une pâte, vocabulaire)
# =====================================================================================
S1 = [
    en("1-1", "Les étiquettes du magasin", "association",
       {"cm1": "Relie chaque mot à sa définition : clique sur un mot, puis sur la bonne définition.",
        "cm2": "Six mots du métier ont perdu leur définition. Reconstitue les six paires."},
       "Une pâte plastique se modèle sans casser ; trop plastique et collante, elle est « grasse ». Le dégraissant la rend moins collante ; la chamotte en est un exemple (argile cuite puis broyée). L'émail est une poudre de verre délayée dans l'eau ; ce qui est vitrifié est devenu dur et étanche comme du verre.",
       {"cm1": ["Les définitions sont dans l'encadré « Mots à connaître ».", "« Plastique » : on peut modeler sans casser.", "La chamotte a déjà connu le four."],
        "cm2": ["Commence par les mots que tu es sûr de connaître.", "Émail et vitrifié parlent tous les deux de verre : l'un est une poudre, l'autre un état.", "Pâte grasse = le problème ; dégraissant = la solution."]},
       cm1={"paires": [
           {"g": "Plastique", "d": "Se modèle facilement sans se casser"},
           {"g": "Pâte grasse", "d": "Pâte très plastique et collante"},
           {"g": "Dégraissant", "d": "Matière ajoutée pour rendre la pâte moins collante"},
           {"g": "Chamotte", "d": "Argile déjà cuite, puis broyée"}]},
       cm2={"paires": [
           {"g": "Plastique", "d": "Se modèle facilement sans se casser"},
           {"g": "Pâte grasse", "d": "Pâte très plastique et collante"},
           {"g": "Dégraissant", "d": "Matière ajoutée pour rendre la pâte moins collante"},
           {"g": "Chamotte", "d": "Argile déjà cuite, puis broyée"},
           {"g": "Émail", "d": "Poudre de verre délayée dans l'eau, brillante après cuisson"},
           {"g": "Vitrifié", "d": "Devenu dur et étanche, comme du verre"}]},
       lecon="pate-composition", partie="encadré « Mots à connaître »"),

    en("1-2", "Les deux rayons", "tri",
       {"cm1": "Range chaque sac dans le bon rayon : matière plastique ou matière non plastique.",
        "cm2": "Range les dix sacs : matières plastiques (les argiles) ou matières non plastiques (les dégraissants)."},
       "Les matières plastiques sont les argiles : elles permettent de modeler la pièce. Les matières non plastiques sont les dégraissants (chamotte, sable, quartz, paille, sciure, feldspath) : on les ajoute pour que la pâte colle moins.",
       {"cm1": ["Toutes les argiles sont plastiques.", "Les dégraissants ne sont pas plastiques.", "La chamotte est une argile déjà cuite : elle ne se modèle plus."],
        "cm2": ["Le mot « terre », « clay » ou « kaolin » désigne une argile.", "Le feldspath est un dégraissant fondant.", "Paille et sciure brûlent au four : ce sont des dégraissants."]},
       cm1={"colonnes": [{"id": "pla", "titre": "Matières plastiques"}, {"id": "non", "titre": "Matières non plastiques"}],
            "cartes": [{"txt": "Kaolin", "col": "pla"}, {"txt": "Ball clay", "col": "pla"}, {"txt": "Terre à grès", "col": "pla"},
                       {"txt": "Sable", "col": "non"}, {"txt": "Chamotte", "col": "non"}, {"txt": "Paille", "col": "non"}]},
       cm2={"colonnes": [{"id": "pla", "titre": "Matières plastiques"}, {"id": "non", "titre": "Matières non plastiques"}],
            "cartes": [{"txt": "Kaolin", "col": "pla"}, {"txt": "Ball clay", "col": "pla"}, {"txt": "Terre à feu", "col": "pla"},
                       {"txt": "Bentonite", "col": "pla"}, {"txt": "Argile commune", "col": "pla"},
                       {"txt": "Chamotte", "col": "non"}, {"txt": "Quartz", "col": "non"}, {"txt": "Sciure de bois", "col": "non"},
                       {"txt": "Feldspath", "col": "non"}, {"txt": "Sable", "col": "non"}]},
       lecon="pate-composition", partie="partie I"),

    en("1-3", "Le carnet d'Inès", "vraifaux",
       {"cm1": "Inès a noté quatre phrases dans son carnet. Pour chacune, dis si elle est vraie ou fausse.",
        "cm2": "Vérifie les cinq phrases du carnet d'Inès : vraie ou fausse ?"},
       "Dans une pâte, les quantités sont pesées avec précision. Une pâte trop collante (grasse) reçoit un dégraissant, pas davantage d'argile. La plasticité est la capacité à être modelée sans casser.",
       {"cm1": ["Relis le début de la partie I.", "Que fait-on quand la pâte colle trop ?", "La plasticité, c'est se modeler sans casser."],
        "cm2": ["Relis le début de la partie I.", "Une argile est un mélange : plusieurs minéraux et d'autres matières.", "Vitrifié veut dire dur et étanche."]},
       cm1={"affirmations": [
           {"txt": "Dans une pâte, les quantités de chaque matière sont pesées avec précision.", "vrai": True, "explication": "On pèse pour obtenir toujours le même produit."},
           {"txt": "Si la pâte est trop collante, on ajoute de l'argile.", "vrai": False, "explication": "On ajoute un dégraissant."},
           {"txt": "La plasticité, c'est la capacité de l'argile à être modelée sans se casser.", "vrai": True, "explication": "C'est la définition du chapitre."},
           {"txt": "Le sable est une matière plastique.", "vrai": False, "explication": "C'est un dégraissant, une matière non plastique."}]},
       cm2={"affirmations": [
           {"txt": "Une pâte céramique contient des matières plastiques et des matières non plastiques.", "vrai": True, "explication": "Les argiles et les dégraissants."},
           {"txt": "Une pâte grasse est une pâte très peu plastique.", "vrai": False, "explication": "Elle est très plastique et collante."},
           {"txt": "Une argile est faite d'un seul minéral argileux.", "vrai": False, "explication": "Elle en contient plusieurs, mélangés à d'autres matières."},
           {"txt": "Une pièce vitrifiée est dure et étanche.", "vrai": True, "explication": "Comme du verre."},
           {"txt": "La couleur d'une argile dépend de l'endroit où on l'extrait.", "vrai": True, "explication": "Sa couleur et ses propriétés changent selon le gisement."}]},
       lecon="pate-composition", partie="partie I"),

    en("1-4", "La fiche de fabrication", "trous", {"cm2": "Complète la fiche de fabrication avec les bonnes étiquettes. Deux étiquettes sont en trop."},
       "Une pâte céramique mélange de l'argile et d'autres matières pesées avec précision. L'argile apporte la plasticité ; le dégraissant (chamotte, sable…) rend la pâte moins collante.",
       {"cm2": ["Le premier mot manquant est la matière plastique principale.", "« Pesées avec… » : on ne dose pas au hasard.", "Les étiquettes en trop parlent d'émail et de cuisson."]},
       expert={"texte": "<p>Une pâte céramique est un mélange d'[[argile]] et d'autres matières, [[pesées]] avec précision. L'argile apporte la [[plasticité]] : on peut modeler la pièce sans la casser. Si la pâte est trop [[collante]], on ajoute un [[dégraissant]], par exemple de la chamotte ou du sable.</p>",
               "etiquettes": ["argile", "pesées", "plasticité", "collante", "dégraissant", "émail", "vitrifiée"]},
       lecon="pate-composition", partie="partie I"),
]

# =====================================================================================
# SALLE 2 — Le laboratoire (minéraux argileux, plasticité, argile primaire / secondaire)
# =====================================================================================
S2 = [
    en("2-1", "Sous le microscope", "ordre",
       {"cm1": "Range les trois minéraux argileux de la plasticité la plus faible (en haut) à la plus haute (en bas). Utilise les flèches, puis vérifie.",
        "cm2": "Classe les trois minéraux argileux, du moins plastique au plus plastique, sans l'aide des repères."},
       "La kaolinite a une plasticité faible, l'illite une plasticité moyenne, la smectite (par exemple la montmorillonite) une plasticité haute.",
       {"cm1": ["Regarde le tableau des minéraux argileux.", "Le kaolin, peu plastique, contient surtout de la kaolinite.", "Le plus plastique a pour exemple la montmorillonite."],
        "cm2": ["Il y a trois niveaux : faible, moyenne, haute.", "La kaolinite est en haut.", "La smectite est en bas."]},
       cm1={"items": [{"txt": "Kaolinite", "sous": "le minéral du kaolin", "rang": 1},
                      {"txt": "Illite", "sous": "plasticité moyenne", "rang": 2},
                      {"txt": "Smectite", "sous": "exemple : la montmorillonite", "rang": 3}]},
       cm2={"items": [{"txt": "Kaolinite", "rang": 1}, {"txt": "Illite", "rang": 2}, {"txt": "Smectite (montmorillonite)", "rang": 3}]},
       lecon="mineraux-argiles", partie="partie I.1"),

    en("2-2", "Les questions de Théo", "qcm",
       {"cm1": "Théo, le technicien du laboratoire, te pose trois questions. Choisis la bonne réponse à chacune.",
        "cm2": "Théo veut vérifier que tu as compris ce qu'est une argile. Réponds à ses trois questions."},
       "Les minéraux argileux sont des particules microscopiques. Une argile est une matière naturelle qui mélange plusieurs minéraux argileux et d'autres matières ; sa couleur et ses propriétés dépendent du lieu d'extraction.",
       {"cm1": ["Un minéral argileux est minuscule.", "Une argile, c'est un mélange naturel.", "On en compte trois principaux."],
        "cm2": ["Relis « Les minéraux argileux » puis « Les argiles ».", "L'argile n'est pas fabriquée en usine.", "Le lieu d'extraction change la couleur."]},
       cm1={"questions": [
           {"q": "Les minéraux argileux sont…", "options": ["de gros cailloux", "des particules microscopiques", "des morceaux de verre"], "bonne": 1, "explication": "On ne les voit qu'au microscope."},
           {"q": "Combien y a-t-il de minéraux argileux principaux ?", "options": ["3", "5", "10"], "bonne": 0, "explication": "Kaolinite, illite, smectite."},
           {"q": "Une argile est…", "options": ["une matière fabriquée en usine", "une poudre de verre", "une matière naturelle"], "bonne": 2, "explication": "On l'extrait du sol."}]},
       cm2={"questions": [
           {"q": "Une argile contient…", "options": ["un seul minéral argileux pur", "plusieurs minéraux argileux et d'autres matières (sable, quartz, restes de plantes)", "uniquement du sable"], "bonne": 1, "explication": "C'est un mélange naturel."},
           {"q": "Pourquoi deux argiles n'ont-elles pas la même couleur ?", "options": ["Elles viennent d'endroits différents", "On les peint", "Elles ont été cuites"], "bonne": 0, "explication": "Couleur et propriétés dépendent du lieu d'extraction."},
           {"q": "Que désigne la plasticité ?", "options": ["La résistance à la chaleur", "La couleur après cuisson", "La capacité à être modelée sans casser"], "bonne": 2, "explication": "C'est la qualité recherchée pour modeler."}]},
       lecon="mineraux-argiles", partie="partie I.1"),

    en("2-3", "Restée sur place ou voyageuse ?", "tri",
       {"cm1": "Range chaque étiquette : argile primaire ou argile secondaire ?",
        "cm2": "Range les huit étiquettes : argile primaire ou argile secondaire ? Attention aux phrases."},
       "Une argile primaire est restée sur place, là où la roche s'est transformée : c'est le cas du kaolin. Une argile secondaire a été transportée par l'eau ou le vent, s'est mélangée à d'autres matières et est plus plastique : ball clay, terre à feu, terre à grès, argiles communes.",
       {"cm1": ["Primaire = elle n'a pas bougé.", "Secondaire = elle a voyagé avec l'eau ou le vent.", "Une seule argile du chapitre est primaire : la blanche."],
        "cm2": ["Relis l'encadré « Argile primaire ou argile secondaire ? ».", "En voyageant, l'argile se mélange à d'autres matières.", "L'argile secondaire est la plus plastique des deux."]},
       cm1={"colonnes": [{"id": "pri", "titre": "Argile primaire"}, {"id": "sec", "titre": "Argile secondaire"}],
            "cartes": [{"txt": "Restée sur place, là où la roche s'est transformée", "col": "pri"}, {"txt": "Le kaolin", "col": "pri"},
                       {"txt": "Transportée par l'eau ou le vent", "col": "sec"}, {"txt": "La ball clay", "col": "sec"},
                       {"txt": "Les argiles communes (terre rouge)", "col": "sec"}]},
       cm2={"colonnes": [{"id": "pri", "titre": "Argile primaire"}, {"id": "sec", "titre": "Argile secondaire"}],
            "cartes": [{"txt": "Restée sur place, là où la roche s'est transformée", "col": "pri"}, {"txt": "Le kaolin", "col": "pri"},
                       {"txt": "Moins plastique que l'autre type", "col": "pri"},
                       {"txt": "Transportée loin de son origine", "col": "sec"}, {"txt": "Mélangée à d'autres matières pendant le voyage", "col": "sec"},
                       {"txt": "La terre à feu", "col": "sec"}, {"txt": "La terre à grès", "col": "sec"}, {"txt": "La ball clay", "col": "sec"}]},
       lecon="mineraux-argiles", partie="encadré « Argile primaire ou argile secondaire ? »"),

    en("2-4", "L'échantillon mal rangé", "intrus", {"cm2": "Ces échantillons sont tous rangés dans le tiroir « argiles secondaires ». Un seul n'a rien à y faire : trouve l'intrus."},
       "Le kaolin est une argile primaire : il est resté sur place. Ball clay, terre à feu, terre à grès et argiles communes ont été transportées : ce sont des argiles secondaires.",
       {"cm2": ["Cherche l'argile qui n'a pas voyagé.", "Elle est blanche.", "Elle sert à la porcelaine."]},
       expert={"cartes": [{"txt": "Ball clay", "sous": "argile à boulets", "intrus": False},
                          {"txt": "Terre à feu", "sous": "argile réfractaire", "intrus": False},
                          {"txt": "Kaolin", "sous": "argile blanche", "intrus": True},
                          {"txt": "Terre à grès", "sous": "résiste au gel", "intrus": False},
                          {"txt": "Argile commune", "sous": "terre rouge", "intrus": False}]},
       lecon="mineraux-argiles", partie="partie I.1"),
]

# =====================================================================================
# SALLE 3 — La réserve des argiles (les principales argiles, couleurs, usages)
# =====================================================================================
S3 = [
    en("3-1", "Les sacs sans étiquette", "association",
       {"cm1": "Relie chaque argile à sa couleur.",
        "cm2": "Relie chaque argile à ce qui la caractérise le mieux."},
       "Kaolin : blanc. Ball clay : blanc crème à gris clair, très plastique. Terre à feu : beige à brun clair, résiste à environ 1500 °C. Terre à grès : beige à brun, résiste au gel. Argiles communes : rouges, riches en fer. Bentonite : extrêmement plastique.",
       {"cm1": ["La porcelaine est blanche : pense à son argile.", "La terre cuite des briques est rouge.", "La ball clay est presque blanche, un peu grise."],
        "cm2": ["Regarde le tableau « Les argiles » de la synthèse.", "Le fer donne la couleur rouge.", "Réfractaire = résiste au feu."]},
       cm1={"paires": [{"g": "Kaolin", "d": "Blanche"}, {"g": "Ball clay", "d": "Blanc crème à gris clair"},
                       {"g": "Terre à feu", "d": "Beige à brun clair"}, {"g": "Argiles communes", "d": "Rouge"}]},
       cm2={"paires": [{"g": "Kaolin", "d": "Blanche, argile primaire"}, {"g": "Ball clay", "d": "Très plastique, blanc crème à gris clair"},
                       {"g": "Terre à feu", "d": "Résiste à environ 1500 °C"}, {"g": "Terre à grès", "d": "Résiste au gel"},
                       {"g": "Argiles communes", "d": "Riches en fer, rouges"}, {"g": "Bentonite", "d": "Extrêmement plastique"}]},
       lecon="principales-argiles", partie="partie I.1, « Les principales argiles »"),

    en("3-2", "Le rayonnage de la réserve", "plan",
       {"cm1": "Awa range la réserve. Place chaque argile sur la bonne étagère : clique sur une étiquette, puis sur la case. Une étiquette est en trop.",
        "cm2": "Place chaque argile sur l'étagère qui correspond à son usage. Deux étiquettes sont en trop."},
       "Porcelaine et vaisselle fine : kaolin. Briques de four, supports d'enfournement, creusets : terre à feu. Briques et tuiles : argiles communes. Vaisselle, poteries de jardin et carreaux qui résistent au gel : terre à grès. Un peu dans une pâte ou dans un émail : bentonite. Pâtes fines, porcelaine, faïence : ball clay.",
       {"cm1": ["Lis l'usage écrit sur chaque étagère.", "Le four a besoin d'une argile qui résiste au feu.", "Tuiles et briques sont rouges."],
        "cm2": ["Chaque fiche de la partie I.1 donne les usages.", "La bentonite s'ajoute « un peu » : elle n'est jamais seule.", "La terre à grès résiste au gel : pense au jardin."]},
       cm1={"titre": "Le rayonnage de la réserve", "colonnes": 2,
            "cases": [{"libelle": "Étagère 1 : porcelaine et vaisselle fine", "reponse": "Kaolin"},
                      {"libelle": "Étagère 2 : briques de four et creusets", "reponse": "Terre à feu"},
                      {"libelle": "Étagère 3 : briques et tuiles", "reponse": "Argiles communes"},
                      {"libelle": "Étagère 4 : vaisselle, poteries de jardin, carreaux", "reponse": "Terre à grès"}],
            "etiquettes": ["Kaolin", "Terre à feu", "Argiles communes", "Terre à grès", "Bentonite"]},
       cm2={"titre": "Le rayonnage de la réserve", "colonnes": 2,
            "cases": [{"libelle": "Étagère 1 : porcelaine et vaisselle fine (argile primaire)", "reponse": "Kaolin"},
                      {"libelle": "Étagère 2 : plaques et supports d'enfournement", "reponse": "Terre à feu"},
                      {"libelle": "Étagère 3 : tuiles, riche en fer", "reponse": "Argiles communes"},
                      {"libelle": "Étagère 4 : carreaux qui résistent au gel", "reponse": "Terre à grès"},
                      {"libelle": "Étagère 5 : un peu dans l'émail, pour que la poudre ne tombe pas au fond du seau", "reponse": "Bentonite"},
                      {"libelle": "Étagère 6 : pâtes fines et faïence, très plastique", "reponse": "Ball clay"}],
            "etiquettes": ["Kaolin", "Terre à feu", "Argiles communes", "Terre à grès", "Bentonite", "Ball clay", "Chamotte", "Feldspath"]},
       lecon="principales-argiles", partie="partie I.1, « Les principales argiles »"),

    en("3-3", "Le bon choix", "qcm",
       {"cm1": "Pour chaque commande, choisis la bonne argile.",
        "cm2": "Trois commandes arrivent à la réserve. Choisis la bonne réponse à chacune."},
       "Pour une pâte plus plastique, on ajoute un peu de bentonite. Une argile commune rouge foncé contient beaucoup de fer. Le kaolin est fait surtout de kaolinite, peu plastique.",
       {"cm1": ["La bentonite est extrêmement plastique.", "Plus il y a de fer, plus l'argile est rouge.", "Le kaolin est blanc."],
        "cm2": ["La bentonite s'ajoute en petite quantité.", "Le fer colore l'argile.", "Kaolin vient de kaolinite."]},
       cm1={"questions": [
           {"q": "Pour rendre une pâte plus plastique, on ajoute un peu de…", "options": ["sable", "bentonite", "chamotte"], "bonne": 1, "explication": "La bentonite est extrêmement plastique."},
           {"q": "Une argile rouge foncé contient beaucoup de…", "options": ["fer", "kaolin", "verre"], "bonne": 0, "explication": "Le fer colore les argiles communes."},
           {"q": "Pour la porcelaine, on choisit…", "options": ["la terre à feu", "l'argile commune", "le kaolin"], "bonne": 2, "explication": "Le kaolin est blanc."}]},
       cm2={"questions": [
           {"q": "Pourquoi met-on un peu de bentonite dans un émail ?", "options": ["Pour le colorer en rouge", "Pour que la poudre ne tombe pas au fond du seau", "Pour qu'il fonde plus vite"], "bonne": 1, "explication": "Elle garde la poudre en suspension."},
           {"q": "Le kaolin est fait surtout de…", "options": ["kaolinite, de plasticité faible", "smectite, très plastique", "chamotte"], "bonne": 0, "explication": "C'est pour cela qu'il est peu plastique."},
           {"q": "La terre à grès convient aux poteries de jardin car…", "options": ["elle est rouge", "elle fond à 1000 °C", "devenue dure et étanche, elle résiste au gel"], "bonne": 2, "explication": "Elle se vitrifie à la cuisson."}]},
       lecon="principales-argiles", partie="partie I.1"),

    en("3-4", "Le cadenas de la réserve", "code", {"cm2": "Le cadenas de l'armoire des échantillons a deux molettes. Trouve les deux nombres."},
       "La terre à feu résiste à environ 1500 °C sans fondre ni se déformer. Il y a 3 minéraux argileux principaux : kaolinite, illite, smectite.",
       {"cm2": ["Le premier nombre est une température.", "C'est la température que supporte l'argile réfractaire.", "Le second nombre compte des minéraux du laboratoire."]},
       expert={"champs": [{"libelle": "Température (°C) que supporte la terre à feu", "valeur": "1500", "longueur": 4},
                          {"libelle": "Nombre de minéraux argileux principaux", "valeur": "3", "longueur": 1}]},
       lecon="principales-argiles", partie="partie I.1"),
]

# =====================================================================================
# SALLE 4 — La salle de préparation (dégraissants, sécurité)
# =====================================================================================
S4 = [
    en("4-1", "Les quatre bacs", "tri",
       {"cm1": "Lucas prépare les dégraissants. Range chaque matière dans le bon bac.",
        "cm2": "Range les neuf matières dans le bon bac de dégraissant."},
       "Dégraissants simples : chamotte, tessons broyés. Siliceux : sable, quartz, galets de mer broyés. Combustibles : paille, papier, sciure de bois. Fondants : feldspath.",
       {"cm1": ["La chamotte est un dégraissant simple.", "Combustible = ça brûle au four.", "Le feldspath aide à fondre."],
        "cm2": ["Relis le tableau des dégraissants, partie I.2.", "Siliceux : sable et quartz.", "Les tessons sont des morceaux de poterie sans émail."]},
       cm1={"colonnes": [{"id": "sim", "titre": "Simples"}, {"id": "sil", "titre": "Siliceux"}, {"id": "com", "titre": "Combustibles"}, {"id": "fon", "titre": "Fondants"}],
            "cartes": [{"txt": "Chamotte", "col": "sim"}, {"txt": "Sable", "col": "sil"}, {"txt": "Quartz", "col": "sil"},
                       {"txt": "Paille", "col": "com"}, {"txt": "Sciure de bois", "col": "com"}, {"txt": "Feldspath", "col": "fon"}]},
       cm2={"colonnes": [{"id": "sim", "titre": "Simples"}, {"id": "sil", "titre": "Siliceux"}, {"id": "com", "titre": "Combustibles"}, {"id": "fon", "titre": "Fondants"}],
            "cartes": [{"txt": "Chamotte", "col": "sim"}, {"txt": "Tessons broyés", "col": "sim"},
                       {"txt": "Sable", "col": "sil"}, {"txt": "Quartz en poudre", "col": "sil"}, {"txt": "Galets de mer broyés", "col": "sil"},
                       {"txt": "Paille", "col": "com"}, {"txt": "Papier", "col": "com"}, {"txt": "Sciure de bois", "col": "com"},
                       {"txt": "Feldspath", "col": "fon"}]},
       lecon="degraissants-securite", partie="partie I.2"),

    en("4-2", "Les effets du dégraissant", "vraifaux",
       {"cm1": "Lucas explique à quoi sert un dégraissant. Ses phrases sont-elles vraies ou fausses ?",
        "cm2": "Vrai ou faux : vérifie les cinq affirmations de Lucas sur les dégraissants."},
       "Un dégraissant réduit la plasticité : la pâte est moins collante, sèche mieux, se fissure et se déforme moins. Les combustibles laissent de petits trous qui allègent la pièce ; les fondants la rendent dure et vitrifiée.",
       {"cm1": ["Un dégraissant réduit la plasticité.", "La pâte sèche mieux.", "Elle se fissure moins, pas plus."],
        "cm2": ["Relis la phrase sous le titre « Les matières non plastiques ».", "Les combustibles brûlent : il reste des trous.", "Les fondants aident la pâte à fondre."]},
       cm1={"affirmations": [
           {"txt": "Un dégraissant rend la pâte moins collante.", "vrai": True, "explication": "Il réduit sa plasticité."},
           {"txt": "Avec un dégraissant, la pâte se fissure davantage.", "vrai": False, "explication": "Elle se fissure moins."},
           {"txt": "Avec un dégraissant, la pâte sèche mieux.", "vrai": True, "explication": "C'est l'un de ses effets."},
           {"txt": "Un dégraissant rend la pâte plus plastique.", "vrai": False, "explication": "Il réduit la plasticité."}]},
       cm2={"affirmations": [
           {"txt": "Un dégraissant réduit la plasticité de l'argile.", "vrai": True, "explication": "C'est son rôle."},
           {"txt": "Une pâte dégraissée se déforme moins à la cuisson.", "vrai": True, "explication": "Elle est plus stable."},
           {"txt": "Les dégraissants combustibles rendent la pièce plus lourde.", "vrai": False, "explication": "Ils brûlent et laissent des trous : la pièce est plus légère."},
           {"txt": "Les dégraissants fondants rendent la pièce dure et vitrifiée.", "vrai": True, "explication": "Ils aident la pâte à fondre."},
           {"txt": "Les dégraissants siliceux fragilisent la pièce cuite.", "vrai": False, "explication": "Ils résistent à la chaleur et la renforcent."}]},
       lecon="degraissants-securite", partie="partie I.2"),

    en("4-3", "L'armoire des fondants", "intrus",
       {"cm1": "Certaines matières fondantes contiennent du plomb, toxique. Un seul de ces gestes est dangereux : trouve-le.",
        "cm2": "Devant l'armoire des fondants, un seul de ces gestes ne protège pas du plomb : trouve l'intrus."},
       "Le plomb est toxique : on manipule les matières fondantes avec des gants, un masque, et on se lave les mains. Manger ou boire à son poste de travail est dangereux.",
       {"cm1": ["Relis l'encadré « Sécurité ».", "Trois gestes protègent.", "On ne mange jamais là où l'on manipule ces poudres."],
        "cm2": ["Le plomb peut entrer par la bouche et par le nez.", "Gants, masque, lavage des mains : ce sont les trois réflexes.", "L'intrus fait entrer la poudre dans la bouche."]},
       cm1={"cartes": [{"txt": "Porter des gants", "intrus": False}, {"txt": "Porter un masque", "intrus": False},
                       {"txt": "Goûter la poudre", "intrus": True}, {"txt": "Se laver les mains", "intrus": False}]},
       cm2={"cartes": [{"txt": "Porter des gants", "sous": "les mains protégées", "intrus": False},
                       {"txt": "Porter un masque", "sous": "ne pas respirer la poudre", "intrus": False},
                       {"txt": "Se laver les mains", "sous": "après la manipulation", "intrus": False},
                       {"txt": "Prendre son goûter à son poste", "sous": "pour gagner du temps", "intrus": True}]},
       lecon="degraissants-securite", partie="encadré « Sécurité »"),

    en("4-4", "Un rôle pour chaque bac", "association", {"cm2": "Relie chaque type de dégraissant à son rôle."},
       "Simple : moins collante tout en restant solide. Siliceux : résiste à la chaleur et renforce la pièce cuite. Combustible : brûle et laisse de petits trous, la pièce est plus légère. Fondant : aide la pâte à fondre, la pièce devient dure et vitrifiée.",
       {"cm2": ["La colonne « Rôle » du tableau des dégraissants.", "Le combustible disparaît dans le four.", "Le fondant fait fondre."]},
       expert={"paires": [{"g": "Simple (chamotte)", "d": "Rend la pâte moins collante, tout en la gardant solide"},
                          {"g": "Siliceux (sable, quartz)", "d": "Résiste à la chaleur et renforce la pièce cuite"},
                          {"g": "Combustible (paille, sciure)", "d": "Brûle et laisse de petits trous : la pièce est plus légère"},
                          {"g": "Fondant (feldspath)", "d": "Aide la pâte à fondre : la pièce devient dure et vitrifiée"}]},
       lecon="degraissants-securite", partie="partie I.2"),
]

# =====================================================================================
# SALLE 5 — Le four (familles de pâtes, températures, recettes)
# =====================================================================================
S5 = [
    en("5-1", "La montée en température", "ordre",
       {"cm1": "Range ces familles de pâtes de la cuisson la moins chaude (en haut) à la plus chaude (en bas).",
        "cm2": "Classe ces familles de pâtes de la cuisson la moins chaude à la plus chaude. Les températures ne sont pas données."},
       "Terre cuite : 1000 °C. Faïence : 1050 °C. Grès : 1280 °C. Porcelaine dure : jusqu'à 1400 °C. Plus la cuisson est chaude, plus la pâte est dure et étanche.",
       {"cm1": ["Les repères donnent les objets : pense à leur dureté.", "La terre cuite est la moins chaude.", "La porcelaine dure est la plus chaude."],
        "cm2": ["Relis la colonne « Cuisson » de la partie II.", "La faïence cuit un peu plus chaud que la terre cuite.", "Grès et porcelaine sont vitrifiés."]},
       cm1={"items": [{"txt": "Terre cuite", "sous": "briques, tuiles", "rang": 1},
                      {"txt": "Faïence", "sous": "vaisselle émaillée", "rang": 2},
                      {"txt": "Grès", "sous": "dur et étanche", "rang": 3},
                      {"txt": "Porcelaine dure", "sous": "blanche, translucide", "rang": 4}]},
       cm2={"items": [{"txt": "Terre cuite", "rang": 1}, {"txt": "Faïence", "rang": 2}, {"txt": "Grès", "rang": 3}, {"txt": "Porcelaine dure", "rang": 4}]},
       lecon="familles-recettes", partie="partie II"),

    en("5-2", "Le pyromètre du four", "instrument",
       {"cm1": "Lis la température affichée par le pyromètre pour chaque cuisson, puis écris-la.",
        "cm2": "Lis la température de la première cuisson, puis règle le pyromètre pour le grès et pour le raku (glisse le niveau)."},
       "Le pyromètre mesure la température du four. Faïence : 1050 °C. Grès : 1280 °C. Terre cuite et raku : 1000 °C.",
       {"cm1": ["Lis la graduation au niveau du trait.", "Chaque petit trait vaut 10 °C.", "Les nombres sont écrits tous les 100 °C."],
        "cm2": ["Relis la colonne « Cuisson » de la partie II.", "Le raku cuit comme la terre cuite.", "Le grès cuit à 1280 °C."]},
       cm1={"instrument": "thermometre", "unite": "°C", "min": 800, "max": 1400, "pas": 10, "etiquettes": 7,
            "items": [{"libelle": "Cuisson de la terre cuite", "mode": "lire", "valeur": 1000},
                      {"libelle": "Cuisson de la faïence", "mode": "lire", "valeur": 1050},
                      {"libelle": "Cuisson du grès", "mode": "lire", "valeur": 1280}]},
       cm2={"instrument": "thermometre", "unite": "°C", "min": 800, "max": 1400, "pas": 10, "etiquettes": 7,
            "items": [{"libelle": "Pendant une cuisson de faïence", "mode": "lire", "valeur": 1050},
                      {"libelle": "Grès", "mode": "regler", "valeur": 1280},
                      {"libelle": "Raku", "mode": "regler", "valeur": 1000}]},
       lecon="familles-recettes", partie="partie II"),

    en("5-3", "Qui suis-je ?", "qcm",
       {"cm1": "Madame Ferrand décrit trois pâtes. Retrouve la famille de chacune.",
        "cm2": "Madame Ferrand décrit trois pâtes sans les nommer. Retrouve chaque famille."},
       "Plus la cuisson est chaude, plus la pâte devient dure et étanche. Le raku contient beaucoup de chamotte et supporte les chocs de chaleur. La porcelaine est blanche et translucide quand elle est fine ; le vitreous est blanc, vitrifié, émaillé mais non translucide.",
       {"cm1": ["La chamotte aide à supporter les chocs de chaleur.", "Translucide : la lumière passe à travers.", "Chaleur = dureté."],
        "cm2": ["Deux pâtes sont blanches et vitrifiées : une seule laisse passer la lumière.", "La terre cuite est souvent sans émail.", "Relis la colonne « De quoi est faite la pâte ? »."]},
       cm1={"questions": [
           {"q": "Plus la cuisson est chaude, plus la pâte devient…", "options": ["dure et étanche", "molle", "collante"], "bonne": 0, "explication": "C'est la règle de la partie II."},
           {"q": "« J'ai beaucoup de chamotte et je supporte les chocs de chaleur. »", "options": ["la porcelaine", "le raku", "la faïence"], "bonne": 1, "explication": "Le raku cuit à 1000 °C."},
           {"q": "« Je suis blanche et translucide quand je suis fine. »", "options": ["la terre cuite", "le grès", "la porcelaine"], "bonne": 2, "explication": "Elle est faite surtout de kaolin."}]},
       cm2={"questions": [
           {"q": "« Je suis blanche, vitrifiée, toujours émaillée, mais non translucide. »", "options": ["le vitreous", "la porcelaine", "la faïence"], "bonne": 0, "explication": "Sanitaires, vaisselle d'hôtellerie."},
           {"q": "« Je suis rouge, riche en fer, souvent sans émail. »", "options": ["le grès", "la terre cuite", "le raku"], "bonne": 1, "explication": "Briques, tuiles, poteries horticoles."},
           {"q": "« Ma pâte est faite d'argile commune ou blanche, toujours recouverte d'émail, cuite vers 1050 °C. »", "options": ["la porcelaine", "le vitreous", "la faïence"], "bonne": 2, "explication": "Vaisselle, plats, carreaux."}]},
       lecon="familles-recettes", partie="partie II"),

    en("5-4", "Le cahier de recettes", "code", {"cm2": "Une tache d'huile cache des nombres du cahier de recettes. Retrouve-les (le total d'une recette fait toujours 100 %)."},
       "Porcelaine : kaolin 25 + ball clay 25 + feldspath 25 + silice 25 = 100 %. Raku : terre à feu 55 + ball clay 25 + chamotte 20 = 100 %. Pour 20 kg de grès : 50 % de terre à feu, soit 10 kg.",
       {"cm2": ["Additionne les parts connues, puis enlève-les de 100.", "Raku : 55 + 25 = 80.", "La moitié de 20 kg."]},
       expert={"champs": [{"libelle": "Porcelaine : part de silice (%)", "valeur": "25", "longueur": 2},
                          {"libelle": "Raku : part de chamotte (%)", "valeur": "20", "longueur": 2},
                          {"libelle": "Masse de terre à feu (kg) pour 20 kg de pâte à grès (50 %)", "valeur": "10", "longueur": 2}]},
       lecon="familles-recettes", partie="partie III"),
]

TITRES = ["Le magasin des matières", "Le laboratoire", "La réserve des argiles", "La salle de préparation", "Le four"]
SOUS = ["Les matières premières des pâtes", "Minéraux argileux, argile primaire et secondaire", "Les principales argiles et leurs usages",
        "Les dégraissants et la sécurité", "Familles de pâtes, cuisson et recettes"]
ENIGMES = {
    "metadata": {
        "jeu": TITRE, "version": 1,
        "differenciation": "Essentiel (clé cm1) : 3 énigmes par salle (15). Expert (clé cm2) : 4 énigmes par salle (20). Le champ \"niveaux\": [\"CM2\"] réserve une énigme au niveau Expert.",
        "types": ["qcm", "vraifaux", "association", "ordre", "tri", "trous", "code", "intrus", "plan", "instrument"],
        "sources": COURS + " (document de l'enseignant). Points à confirmer : A-VERIFIER.md.",
        "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-2\",\"legende\":\"…\",\"source\":\"…\"} (image dans assets/images/cartes/)."
    },
    "salles": [{"num": i + 1, "titre": f"{TITRES[i]} — {SOUS[i]}", "enigmes": s} for i, s in enumerate([S1, S2, S3, S4, S5])]
}

# =====================================================================================
# DIALOGUES (personnages inventés)
# =====================================================================================
P = {"maelle": ("Maëlle", "Apprentie en 2e année de CAP Décoration sur céramique, elle guide l'équipe"),
     "ines": ("Inès", "Magasinière de la manufacture"),
     "theo": ("Théo", "Technicien du laboratoire"),
     "awa": ("Awa", "Responsable de la réserve des argiles"),
     "lucas": ("Lucas", "Préparateur de pâtes"),
     "ferrand": ("Madame Ferrand", "Cheffe du four")}
MOTS = ["ARGILE", "PLASTICITÉ", "KAOLIN", "DÉGRAISSANT", "CUISSON"]
DECORS = ["magasin", "laboratoire", "reserve", "preparation", "four"]
LIEUX = ["Le magasin des matières premières de la manufacture des Trois Fours", "Le laboratoire d'essais, au premier étage",
         "La réserve des argiles, derrière l'atelier", "La salle de préparation des pâtes", "La halle des fours"]
DESCR = ["Des sacs de 25 kg s'empilent sur des palettes : argiles, sable, chamotte, feldspath. Inès coche une liste sur sa tablette.",
         "Une paillasse blanche, un microscope, des coupelles d'échantillons numérotés. Sur le tableau, trois noms de minéraux.",
         "Des bacs d'argile humide sous des bâches, et six étagères dont les étiquettes sont tombées par terre.",
         "Un malaxeur ronronne. Quatre bacs de dégraissants attendent, et une armoire grillagée porte un pictogramme « toxique ».",
         "Deux grands fours électriques. Sur l'écran du pyromètre, la température monte doucement."]
SENS = [["À voir : les sacs empilés", "À entendre : le chariot élévateur", "À sentir : la poussière d'argile"],
        ["À voir : la lame sous le microscope", "À entendre : le bourdonnement de la lampe", "À toucher : une boulette d'argile humide"],
        ["À voir : des argiles blanches, beiges et rouges", "À entendre : l'eau qui goutte des bâches", "À sentir : la terre mouillée"],
        ["À voir : les bacs de dégraissants", "À entendre : le malaxeur", "À sentir : la sciure de bois"],
        ["À voir : la lueur orange par le regard du four", "À entendre : le ronflement des résistances", "À sentir : la chaleur sur le visage"]]
INTRO = [("ines", "Bonjour l'équipe. Maëlle m'a prévenue : vous cherchez les fiches du cahier de fabrication. J'en garde une. Avant de vous la donner, je veux être sûre que vous savez de quoi est faite une pâte. Ici, chaque sac se pèse, et chaque mot compte."),
         ("theo", "Entrez, mais ne touchez pas aux coupelles. La deuxième fiche parle de ce qu'on voit au microscope : les minéraux qui rendent une argile plus ou moins facile à modeler. Montrez-moi que vous savez lire une argile, et la fiche est à vous."),
         ("awa", "Le coup de vent de ce matin a fait tomber toutes mes étiquettes. Je ne peux pas livrer l'atelier tant que la réserve n'est pas rangée. Aidez-moi à reconnaître chaque argile et à savoir à quoi elle sert : la troisième fiche est pour vous."),
         ("lucas", "Ici, on transforme l'argile en pâte. Trop collante, elle se fissure au séchage ; mal protégée, une poudre peut rendre malade. La quatrième fiche explique les dégraissants et les règles de sécurité. Prouvez-moi que vous les connaissez."),
         ("ferrand", "Le four doit partir ce soir avec la commande du restaurant. Je garde la dernière fiche : les familles de pâtes, leurs températures et nos recettes. Une erreur de température, et toute la fournée est perdue. Montrez-moi que je peux vous faire confiance.")]
REUSSITE = [("ines", "Parfait. Le mot écrit sur ma fiche est <b>ARGILE</b> : sans elle, pas de pâte. Montez au laboratoire, Théo vous attend avec la fiche suivante."),
            ("theo", "Bien observé. Ma fiche porte le mot <b>PLASTICITÉ</b> : c'est elle qu'on règle en choisissant ses argiles. Awa a besoin d'aide à la réserve."),
            ("awa", "La réserve est rangée, merci ! Le mot de ma fiche est <b>KAOLIN</b>, l'argile blanche de la porcelaine. Lucas vous attend en préparation."),
            ("lucas", "Vous pouvez travailler dans ma salle. Le mot de ma fiche est <b>DÉGRAISSANT</b>. Il reste le four : Madame Ferrand n'aime pas attendre.")]
FIN = ("maelle", "Madame Ferrand vous a donné le dernier mot : <b>CUISSON</b>. Vous avez les cinq fiches ! Écrivez les cinq mots dans le coffre du cahier de fabrication, dans l'ordre des salles, et le four pourra partir ce soir.")

DIALOGUES = {
    "metadata": {"jeu": TITRE, "sujet": "Les pâtes céramiques : matières premières, minéraux argileux, argiles, dégraissants, familles de pâtes, cuisson et recettes — CAP Décoration sur céramique, 1re année",
                 "niveaux": ["Essentiel", "Expert"], "sources": COURS},
    "personnages": {k: {"nom": v[0], "role": v[1]} for k, v in P.items()},
    "intro_accueil": "Bonjour, je suis Maëlle, apprentie en deuxième année. Bienvenue à la manufacture des Trois Fours ! Ce soir, le grand four doit cuire la vaisselle commandée par un restaurant. Problème : notre cahier de fabrication a été démonté pour être recopié, et ses cinq fiches sont restées chez cinq collègues. Chacun vous rendra la sienne si vous prouvez que vous maîtrisez la matière. Les cinq mots écrits sur les fiches ouvriront le coffre du cahier. On commence par le magasin ?",
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
    {"id": "pate-composition", "salle": 1, "icone": "I", "titre": "De quoi est faite une pâte céramique ?", "duree": "3 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Dire de quoi est faite une pâte céramique", "Distinguer matières plastiques et non plastiques", "Connaître le vocabulaire de base"],
     "contenu": {
         "cm1": "<h4>Un mélange pesé</h4><p>Une <b>pâte céramique</b> est un mélange d'<b>argile</b> et d'<b>autres matières</b> (sable, chamotte…). Les quantités sont <b>pesées avec précision</b>.</p><h4>Deux sortes de matières</h4><p>Les <b>matières plastiques</b> (les argiles) permettent de modeler la pièce. Les <b>matières non plastiques</b> sont les <b>dégraissants</b>.</p><div class='encadre'>Pâte trop collante (pâte <b>grasse</b>) ? On ajoute un <b>dégraissant</b>.</div>",
         "cm2": "<h4>Un mélange dosé</h4><p>Une <b>pâte céramique</b> mélange de l'<b>argile</b> et d'autres matières (sable, chamotte…). Chaque matière est <b>pesée avec précision</b> pour obtenir un produit précis.</p><h4>Plastique ou non plastique</h4><p>La <b>plasticité</b> est la capacité de l'argile à être modelée sans se casser. Les <b>matières plastiques</b> sont les argiles ; les <b>matières non plastiques</b> sont les <b>dégraissants</b>, qui réduisent la plasticité.</p><div class='encadre'>Une pâte <b>grasse</b> (très plastique et collante) reçoit un <b>dégraissant</b>. Après cuisson, l'<b>émail</b> (poudre de verre délayée) forme une couche brillante ; une pâte <b>vitrifiée</b> est dure et étanche.</div>"},
     "lexique": [{"mot": "plastique", "def": "se modèle facilement sans se casser"}, {"mot": "pâte grasse", "def": "pâte très plastique et collante"},
                 {"mot": "dégraissant", "def": "matière ajoutée pour rendre la pâte moins collante"}, {"mot": "chamotte", "def": "argile déjà cuite, puis broyée"},
                 {"mot": "émail", "def": "poudre de verre délayée dans l'eau, brillante après cuisson"}, {"mot": "vitrifié", "def": "devenu dur et étanche, comme du verre"}],
     "document": {"type": "text", "titre": "Une pâte de porcelaine", "contenu": "Pour préparer 10 kg de pâte à porcelaine : 2,5 kg de kaolin, 2,5 kg de ball clay, 2,5 kg de feldspath et 2,5 kg de silice.", "source": COURS + ", partie III."},
     "sources": COURS + ", encadré « Mots à connaître » et partie I."},
    {"id": "mineraux-argiles", "salle": 2, "icone": "II", "titre": "Minéraux argileux, argiles primaires et secondaires", "duree": "3 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Citer les 3 minéraux argileux et leur plasticité", "Définir une argile", "Distinguer argile primaire et argile secondaire"],
     "contenu": {
         "cm1": "<h4>Les minéraux argileux</h4><p>Ce sont des particules <b>microscopiques</b>. Il y en a <b>3 principaux</b> : la <b>kaolinite</b> (plasticité faible), l'<b>illite</b> (moyenne), la <b>smectite</b> (haute).</p><h4>Deux sortes d'argiles</h4><p>Une argile <b>primaire</b> est restée <b>sur place</b> : c'est le <b>kaolin</b>. Une argile <b>secondaire</b> a été <b>transportée</b> par l'eau ou le vent ; elle est <b>plus plastique</b>.</p>",
         "cm2": "<h4>Les minéraux argileux</h4><p>Particules <b>microscopiques</b> qui composent l'argile : <b>kaolinite</b> (plasticité faible), <b>illite</b> (moyenne), <b>smectite</b>, par exemple la montmorillonite (haute).</p><h4>L'argile, un mélange naturel</h4><p>Une <b>argile</b> est faite de <b>plusieurs minéraux argileux</b> mêlés à d'autres matières (sable, quartz, restes de plantes). Sa couleur et ses propriétés dépendent du lieu d'extraction.</p><div class='encadre'><b>Primaire</b> : restée là où la roche s'est transformée (le kaolin). <b>Secondaire</b> : transportée par l'eau ou le vent, mélangée à d'autres matières, <b>plus plastique</b>.</div>"},
     "lexique": [{"mot": "minéral argileux", "def": "particule microscopique qui compose l'argile"}, {"mot": "argile primaire", "def": "restée sur place (kaolin)"},
                 {"mot": "argile secondaire", "def": "transportée par l'eau ou le vent, plus plastique"}],
     "frise": [{"date": "faible", "evt": "kaolinite"}, {"date": "moyenne", "evt": "illite"}, {"date": "haute", "evt": "smectite (montmorillonite)"}],
     "frise_titre": "La plasticité des minéraux argileux",
     "sources": COURS + ", partie I.1."},
    {"id": "principales-argiles", "salle": 3, "icone": "III", "titre": "Les principales argiles", "duree": "4 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Reconnaître les principales argiles et leur couleur", "Associer chaque argile à ses usages"],
     "contenu": {
         "cm1": "<ul><li><b>Kaolin</b> : blanc, argile primaire, porcelaine.</li><li><b>Ball clay</b> : blanc crème à gris clair, très plastique.</li><li><b>Terre à feu</b> : beige à brun clair, résiste à environ 1500 °C (briques de four).</li><li><b>Terre à grès</b> : beige à brun, résiste au gel.</li><li><b>Argiles communes</b> : rouges, riches en fer (briques, tuiles).</li><li><b>Bentonite</b> : extrêmement plastique, on en ajoute un peu.</li></ul>",
         "cm2": "<p>Le <b>kaolin</b> est la seule argile <b>primaire</b> du chapitre ; les autres sont <b>secondaires</b>.</p><ul><li><b>Kaolin</b> : blanc, surtout de la kaolinite ; porcelaine, vaisselle fine.</li><li><b>Ball clay</b> (argile à boulets) : blanc crème à gris clair, très plastique ; pâtes fines, porcelaine, faïence.</li><li><b>Terre à feu</b> (réfractaire) : beige à brun clair, résiste à environ 1500 °C ; briques de four, supports d'enfournement, creusets.</li><li><b>Terre à grès</b> : beige à brun, se vitrifie et résiste au gel ; vaisselle, poteries de jardin, carreaux.</li><li><b>Argiles communes</b> : rouges (plus de fer = plus foncé) ; briques, tuiles, poteries de jardin.</li><li><b>Bentonite</b> : extrêmement plastique ; un peu dans une pâte, ou dans un émail pour que la poudre ne tombe pas au fond du seau.</li></ul>"},
     "lexique": [{"mot": "réfractaire", "def": "qui résiste aux très hautes températures"}, {"mot": "kaolin", "def": "argile primaire blanche, base de la porcelaine"}],
     "document": {"type": "image", "fichier": "gisements-argiles", "titre": "Six gisements d'argile",
                  "source": "Planche à produire avec outils/photos/deposer-photos.py (photos Wikimedia Commons ou photos du cours)."},
     "sources": COURS + ", partie I.1, « Les principales argiles »."},
    {"id": "degraissants-securite", "salle": 4, "icone": "IV", "titre": "Les dégraissants et la sécurité", "duree": "3 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Expliquer à quoi sert un dégraissant", "Citer des exemples des quatre types", "Connaître les règles de sécurité avec les fondants"],
     "contenu": {
         "cm1": "<p>Un <b>dégraissant</b> rend la pâte <b>moins collante</b> : elle sèche mieux, se fissure moins et se déforme moins.</p><ul><li><b>Simples</b> : chamotte, tessons broyés.</li><li><b>Siliceux</b> : sable, quartz.</li><li><b>Combustibles</b> : paille, papier, sciure (ils brûlent).</li><li><b>Fondants</b> : feldspath.</li></ul><div class='encadre'>Sécurité : certaines matières fondantes contiennent du <b>plomb</b>, toxique. <b>Gants, masque, lavage des mains.</b></div>",
         "cm2": "<p>Un <b>dégraissant</b> <b>réduit la plasticité</b> : pâte moins collante, meilleur séchage, moins de fissures et de déformations à la cuisson.</p><ul><li><b>Simples</b> (chamotte, tessons broyés) : moins collante, reste solide.</li><li><b>Siliceux</b> (sable, quartz, galets broyés) : résistent à la chaleur, renforcent la pièce cuite.</li><li><b>Combustibles</b> (paille, papier, sciure) : brûlent, laissent de petits trous, pièce plus légère.</li><li><b>Fondants</b> (feldspath) : aident à fondre, pièce dure et vitrifiée.</li></ul><div class='encadre'>Le <b>plomb</b> de certains fondants est <b>toxique</b> : gants, masque, lavage des mains ; jamais manger ni boire à son poste.</div>"},
     "lexique": [{"mot": "combustible", "def": "qui brûle à la cuisson"}, {"mot": "fondant", "def": "qui aide la pâte à fondre"}, {"mot": "tessons", "def": "morceaux de poterie sans émail"}],
     "sources": COURS + ", partie I.2 et encadré « Sécurité »."},
    {"id": "familles-recettes", "salle": 5, "icone": "V", "titre": "Familles de pâtes, cuisson et recettes", "duree": "4 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Citer les grandes familles de pâtes et leur température de cuisson", "Lire et compléter une recette en pourcentages"],
     "contenu": {
         "cm1": "<p>Plus la cuisson est <b>chaude</b>, plus la pâte devient <b>dure</b> et <b>étanche</b>.</p><ul><li><b>Terre cuite</b> : 1000 °C (briques, tuiles).</li><li><b>Faïence</b> : 1050 °C, émaillée.</li><li><b>Raku</b> : 1000 °C, beaucoup de chamotte.</li><li><b>Grès</b> : 1280 °C, dur et étanche.</li><li><b>Porcelaine</b> : 1280 à 1400 °C, blanche.</li></ul><div class='encadre'>Dans une recette, le total des parts fait toujours <b>100 %</b>.</div>",
         "cm2": "<ul><li><b>Terre cuite</b> (1000 °C) : argile commune rouge, souvent sans émail.</li><li><b>Faïence</b> (1050 °C) : argile commune ou blanche, toujours émaillée.</li><li><b>Raku</b> (1000 °C) : beaucoup de chamotte, supporte les chocs de chaleur.</li><li><b>Grès</b> (1280 °C) : vitrifié, dur et étanche, avec ou sans émail.</li><li><b>Vitreous</b> (1280 °C) : blanc vitrifié, émaillé, non translucide.</li><li><b>Porcelaine</b> (1280 °C tendre à 1400 °C dure) : blanche, kaolin, translucide si fine.</li></ul><div class='encadre'>Recettes : porcelaine 25/25/25/25 (kaolin, ball clay, feldspath, silice) ; grès 50/30/10/5/5 (terre à feu, kaolin, feldspath, quartz, chamotte) ; raku 55/25/20 (terre à feu, ball clay, chamotte). Pour 20 kg de grès : 10 kg de terre à feu.</div>"},
     "lexique": [{"mot": "translucide", "def": "laisse passer la lumière"}, {"mot": "pyromètre", "def": "appareil qui mesure la température du four"}],
     "frise": [{"date": "1000 °C", "evt": "terre cuite, raku"}, {"date": "1050 °C", "evt": "faïence"}, {"date": "1280 °C", "evt": "grès, vitreous, porcelaine tendre"}, {"date": "1400 °C", "evt": "porcelaine dure"}],
     "frise_titre": "Températures de cuisson",
     "sources": COURS + ", parties II et III."}
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
    "metadata": {"sujet": "Les pâtes céramiques", "niveaux": ["Essentiel", "Expert"],
                 "programme": "CAP Décoration sur céramique, 1re année — technologie des matériaux : les pâtes céramiques.", "sources": COURS},
    "quizz_final": {
        "CM1": [q("Une pâte céramique est un mélange…", ["d'argile et d'autres matières pesées", "de verre et d'eau", "de peinture et de colle"], 0),
                q("Le minéral argileux le moins plastique est…", ["la smectite", "la kaolinite", "l'illite"], 1),
                q("Quelle argile est primaire ?", ["la ball clay", "la terre à feu", "le kaolin"], 2),
                q("Un dégraissant rend la pâte…", ["moins collante", "plus collante", "rouge"], 0),
                q("Le grès cuit vers…", ["600 °C", "1280 °C", "2000 °C"], 1)],
        "CM2": [q("Que fait-on avec une pâte grasse ?", ["on ajoute de la bentonite", "on ajoute un dégraissant", "on la cuit tout de suite"], 1),
                q("Une argile secondaire est…", ["restée sur place", "faite d'un seul minéral", "transportée par l'eau ou le vent, et plus plastique"], 2),
                q("Quelle argile résiste à environ 1500 °C ?", ["la terre à feu", "l'argile commune", "la bentonite"], 0),
                q("Quel dégraissant rend la pièce plus légère ?", ["le feldspath", "la chamotte", "la sciure de bois"], 2),
                q("Recette du raku : terre à feu 55 %, ball clay 25 %, chamotte… ?", ["20 %", "25 %", "10 %"], 0)]},
    "qcm": {
        "CM1": [q("Combien de minéraux argileux principaux ?", ["2", "3", "6"], 1, 1), q("Le kaolin est de couleur…", ["rouge", "blanche", "noire"], 1, 1),
                q("Les argiles communes sont rouges grâce au…", ["fer", "sable", "kaolin"], 0, 1), q("La chamotte est…", ["de la paille", "une argile cuite puis broyée", "un émail"], 1, 1),
                q("Quel dégraissant est combustible ?", ["la paille", "le sable", "le feldspath"], 0, 1), q("Le feldspath est un dégraissant…", ["siliceux", "combustible", "fondant"], 2, 1),
                q("La faïence cuit vers…", ["1050 °C", "1400 °C", "500 °C"], 0, 1), q("La porcelaine est faite surtout de…", ["terre rouge", "kaolin", "chamotte"], 1, 1),
                q("Avec les fondants au plomb, on porte…", ["des gants et un masque", "un tablier seulement", "rien de spécial"], 0, 1),
                q("Le total d'une recette fait…", ["50 %", "100 %", "1000 %"], 1, 1)],
        "CM2": [q("Exemple de smectite :", ["la montmorillonite", "le quartz", "le feldspath"], 0, 1), q("La ball clay est…", ["une argile primaire", "très plastique", "réfractaire"], 1, 1),
                q("Usage de la terre à feu :", ["tuiles", "porcelaine", "briques de four et creusets"], 2, 1), q("Pourquoi la terre à grès convient-elle au jardin ?", ["elle résiste au gel", "elle est rouge", "elle est légère"], 0, 1),
                q("Rôle des dégraissants siliceux :", ["brûler", "résister à la chaleur et renforcer", "colorer"], 1, 1), q("La bentonite dans un émail sert à…", ["le colorer", "le faire fondre", "garder la poudre en suspension"], 2, 1),
                q("Le vitreous est…", ["blanc, vitrifié, non translucide", "rouge et poreux", "translucide"], 0, 1), q("Le raku supporte…", ["les chocs de chaleur", "le gel", "l'acide"], 0, 1),
                q("Grès : terre à feu 50, kaolin 30, feldspath 10, quartz 5, chamotte… ?", ["10 %", "5 %", "15 %"], 1, 1),
                q("Pour 10 kg de porcelaine, combien de kaolin ?", ["2,5 kg", "5 kg", "1 kg"], 0, 1)]},
    "questions_fermees": {
        "CM1": [{"q": "La plasticité, c'est se modeler sans casser.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Le sable est une matière plastique.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Le kaolin est une argile primaire.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Plus la cuisson est chaude, plus la pâte est molle.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Cite les trois minéraux argileux.", "type": "court", "rep": "kaolinite, illite, smectite", "pts": 1},
                {"q": "Cite un dégraissant.", "type": "court", "rep": "chamotte, sable, quartz, paille, sciure, papier, feldspath…", "pts": 1},
                {"q": "À quelle température cuit la terre cuite ?", "type": "court", "rep": "1000 °C", "pts": 1},
                {"q": "Cite un geste de sécurité avec les fondants.", "type": "court", "rep": "gants, masque ou lavage des mains", "pts": 1}],
        "CM2": [{"q": "Une argile secondaire est moins plastique qu'une argile primaire.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Les dégraissants combustibles allègent la pièce.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Le vitreous est translucide.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "La porcelaine dure cuit jusqu'à 1400 °C.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Définis une argile secondaire.", "type": "court", "rep": "argile transportée par l'eau ou le vent, mélangée à d'autres matières, plus plastique", "pts": 2},
                {"q": "Explique à quoi sert un dégraissant et cite 3 exemples.", "type": "court", "rep": "réduire la plasticité (moins collante, sèche mieux, moins de fissures) ; chamotte, sable, paille…", "pts": 2},
                {"q": "Cite la famille de pâte qui contient beaucoup de chamotte.", "type": "court", "rep": "le raku", "pts": 1},
                {"q": "Calcule la masse de kaolin pour 20 kg de grès (30 %).", "type": "court", "rep": "6 kg", "pts": 1}]},
    "etudes_documents": {
        "CM1": [{"titre": "La recette de la porcelaine", "document": {"contenu": "Kaolin 25 % · Ball clay 25 % · Feldspath 25 % · Silice (quartz) 25 %.", "source": COURS + ", partie III."},
                 "questions": [{"q": "Combien de matières contient la recette ?", "type": "court", "rep": "4", "pts": 1},
                               {"q": "Quelle matière est un dégraissant fondant ?", "type": "court", "rep": "le feldspath", "pts": 1},
                               {"q": "Pour 10 kg de pâte, combien de kaolin ?", "type": "court", "rep": "2,5 kg", "pts": 1}]},
                {"titre": "La fiche de la terre à feu", "document": {"contenu": "Couleur : beige à brun clair. Résiste aux très hautes températures (environ 1500 °C) sans fondre ni se déformer. Utilisée pour les briques de four, les plaques et supports d'enfournement, les creusets.", "source": COURS + ", partie I.1."},
                 "questions": [{"q": "Quelle est sa couleur ?", "type": "court", "rep": "beige à brun clair", "pts": 1},
                               {"q": "Pourquoi sert-elle à fabriquer des briques de four ?", "type": "court", "rep": "elle résiste à environ 1500 °C", "pts": 1}]}],
        "CM2": [{"title_hint": "", "titre": "La recette du grès", "document": {"contenu": "Terre à feu 50 % · Kaolin 30 % · Feldspath 10 % · Quartz 5 % · Chamotte 5 %.", "source": COURS + ", partie III."},
                 "questions": [{"q": "Vérifie que le total fait 100 %.", "type": "court", "rep": "50 + 30 + 10 + 5 + 5 = 100", "pts": 1},
                               {"q": "Classe chaque matière : plastique ou non plastique.", "type": "court", "rep": "plastiques : terre à feu, kaolin ; non plastiques : feldspath, quartz, chamotte", "pts": 2},
                               {"q": "Calcule les masses pour 20 kg de pâte.", "type": "court", "rep": "10 kg ; 6 kg ; 2 kg ; 1 kg ; 1 kg", "pts": 2}]},
                {"titre": "Argile primaire ou secondaire ?", "document": {"contenu": "Argile primaire : elle est restée sur place, là où la roche s'est transformée. Argile secondaire : elle a été transportée par l'eau ou le vent, loin de son origine, et s'est mélangée à d'autres matières.", "source": COURS + ", partie I.1."},
                 "questions": [{"q": "Donne un exemple d'argile primaire.", "type": "court", "rep": "le kaolin", "pts": 1},
                               {"q": "Pourquoi l'argile secondaire est-elle souvent colorée ?", "type": "court", "rep": "elle s'est mélangée à d'autres matières (fer…) pendant son transport", "pts": 1}]}]},
    "fiches_preparatoires": [
        {"salle": i + 1, "titre": f"{TITRES[i]} — {SOUS[i]}", "objectifs": LECONS["lecons"][i]["objectifs"],
         "vocabulaire": LECONS["lecons"][i]["lexique"][:4], "contexte": DESCR[i]} for i in range(5)]
}
for d in EVAL["etudes_documents"]["CM2"]:
    d.pop("title_hint", None)

# =====================================================================================
# LEÇONS A4 (visuels SVG dessinés par script, jamais par IA)
# =====================================================================================
def svg_temperatures():
    fam = [("Terre cuite · Raku", 1000), ("Faïence", 1050), ("Grès · Vitreous", 1280), ("Porcelaine dure", 1400)]
    x0, x1, t0, t1 = 40, 340, 900, 1450
    X = lambda t: x0 + (t - t0) / (t1 - t0) * (x1 - x0)
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 200" role="img" aria-label="Températures de cuisson" font-family="Segoe UI, Helvetica, Arial, sans-serif">',
         '<rect width="380" height="200" fill="#f3f8fd"/>',
         f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#f6c08a"/><stop offset="1" stop-color="#c2410c"/></linearGradient></defs>',
         f'<rect x="{x0}" y="92" width="{x1-x0}" height="14" rx="7" fill="url(#g)"/>']
    for t in range(1000, 1500, 100):
        s.append(f'<line x1="{X(t):.1f}" y1="106" x2="{X(t):.1f}" y2="114" stroke="#0f4c81"/><text x="{X(t):.1f}" y="128" font-size="10" text-anchor="middle" fill="#0f4c81">{t} °C</text>')
    for k, (n, t) in enumerate(fam):
        y = 70 if k % 2 == 0 else 50
        s.append(f'<circle cx="{X(t):.1f}" cy="99" r="5" fill="#0f4c81"/><line x1="{X(t):.1f}" y1="94" x2="{X(t):.1f}" y2="{y+4}" stroke="#0f4c81"/>'
                 f'<text x="{X(t):.1f}" y="{y}" font-size="11" font-weight="bold" text-anchor="middle" fill="#0b2a4a">{n}</text>')
    s.append('<text x="190" y="168" font-size="11" text-anchor="middle" fill="#0b2a4a">Plus la cuisson est chaude, plus la pâte est dure et étanche.</text></svg>')
    return "".join(s)


def svg_plasticite():
    m = [("Kaolinite", "faible", 60), ("Illite", "moyenne", 120), ("Smectite", "haute", 180)]
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 190" role="img" aria-label="Plasticité des minéraux argileux" font-family="Segoe UI, Helvetica, Arial, sans-serif">',
         '<rect width="380" height="190" fill="#f3f8fd"/>']
    for k, (n, p, w) in enumerate(m):
        y = 30 + k * 48
        s.append(f'<text x="20" y="{y+16}" font-size="13" font-weight="bold" fill="#0b2a4a">{n}</text>'
                 f'<rect x="120" y="{y}" width="{w}" height="22" rx="4" fill="#2f75b5"/><text x="{126+w}" y="{y+16}" font-size="12" fill="#0f4c81">{p}</text>')
    s.append('</svg>')
    return "".join(s)


A4 = {"_commentaire": "Généré par outils/generer-pates-ceramiques.py — ne pas modifier à la main.",
      "jeu": {"titre": TITRE, "matiere": "Technologie céramique", "theme": "Les pâtes céramiques", "couleur": "#0F4C81", "accent": "#C2410C", "couleur_pale": "#DCEEFF", "accent_pale": "#FFE9DB"},
      "lecons": {
          "pate-composition": {"competence": "Dire de quoi est faite une pâte céramique ; distinguer matières plastiques et non plastiques.", "visuels": []},
          "mineraux-argiles": {"competence": "Citer les 3 minéraux argileux ; définir argile primaire et argile secondaire.",
                               "visuels": [{"type": "svg", "titre": "La plasticité des minéraux argileux", "legende": "Du moins plastique au plus plastique.", "svg": svg_plasticite(), "etiquette": "Schéma", "source": COURS + ", partie I.1."}]},
          "principales-argiles": {"competence": "Reconnaître les différentes argiles, leurs couleurs et leurs usages.", "visuels": []},
          "degraissants-securite": {"competence": "Expliquer à quoi sert un dégraissant et en citer 3 exemples ; règles de sécurité.", "visuels": []},
          "familles-recettes": {"competence": "Citer les grandes familles de pâtes et leur température de cuisson ; lire une recette.",
                                "visuels": [{"type": "svg", "titre": "Températures de cuisson", "legende": "Les grandes familles de pâtes sur l'échelle des températures.", "svg": svg_temperatures(), "etiquette": "Schéma", "source": COURS + ", partie II."}]}}}

# ---- Compléments Expert (texte fidèle au chapitre) et repères visuels de chaque leçon ----
PLUS = {
    "pate-composition": ("<h4>Pourquoi peser ?</h4><p>Chaque pâte a sa <b>recette</b>. Si l'on change les quantités, on change le produit : une pâte plus riche en argile sera plus plastique, mais elle collera davantage, séchera moins bien et risquera de se fissurer. C'est pourquoi les matières sont pesées avec précision, et la recette notée sur une fiche de fabrication.</p>"
                         "<h4>Le rôle de chaque matière</h4><p>L'argile, matière plastique, permet de modeler, de tourner ou de couler la pièce. Les dégraissants, matières non plastiques, rendent la pâte moins collante. Certains restent dans la pièce (chamotte, sable), d'autres brûlent à la cuisson (paille, sciure), d'autres encore aident la pâte à fondre (feldspath).</p>"
                         "<h4>Le vocabulaire de l'atelier</h4><p>Une pâte <b>plastique</b> se modèle sans casser ; une pâte <b>grasse</b> est très plastique et collante. La <b>chamotte</b> est de l'argile déjà cuite, puis broyée. L'<b>émail</b> est une poudre de verre mélangée à de l'eau : après la cuisson, il forme une couche brillante comme du verre. Une pâte <b>vitrifiée</b> est devenue dure et étanche, comme du verre.</p>",
                         [{"date": "matières plastiques", "evt": "les argiles : kaolin, ball clay, terre à feu, terre à grès, argiles communes, bentonite"},
                          {"date": "matières non plastiques", "evt": "les dégraissants : chamotte, sable, quartz, paille, sciure, feldspath"}], "Les deux familles de matières"),
    "mineraux-argiles": ("<h4>Voir l'invisible</h4><p>Les minéraux argileux sont si petits qu'on ne les voit qu'au microscope. Ce sont eux qui donnent à une argile sa plasticité : plus une argile contient de smectite, plus elle est plastique ; plus elle contient de kaolinite, moins elle l'est. C'est pour cela que le kaolin, fait surtout de kaolinite, a une plasticité faible.</p>"
                         "<h4>Une argile change selon le lieu</h4><p>Une argile n'est jamais un minéral pur : elle mélange plusieurs minéraux argileux et d'autres matières, comme du sable, du quartz ou des restes de plantes. Sa couleur et ses propriétés changent selon l'endroit où on l'extrait.</p>"
                         "<h4>Primaire ou secondaire</h4><p>L'argile <b>primaire</b> est restée sur place, là où la roche s'est transformée : c'est le kaolin. L'argile <b>secondaire</b> a été transportée par l'eau ou le vent, loin de son origine ; en voyageant, elle s'est mélangée à d'autres matières et elle est devenue plus plastique que l'argile primaire. La ball clay, la terre à feu, la terre à grès et les argiles communes sont des argiles secondaires.</p>", None, None),
    "principales-argiles": ("<h4>Choisir son argile</h4><p>On choisit une argile pour sa couleur après cuisson, sa plasticité et sa résistance à la chaleur. Pour une porcelaine blanche, on part du kaolin, que l'on rend plus facile à travailler avec de la ball clay, très plastique. Pour fabriquer les briques et les plaques qui garnissent le four, on prend la terre à feu, qui supporte environ 1500 °C sans fondre ni se déformer.</p>"
                            "<h4>La couleur dit quelque chose</h4><p>Une argile commune est rouge parce qu'elle contient du fer : plus il y a de fer, plus elle est rouge foncé. La terre à grès, beige à brun, devient dure et étanche à la cuisson (vitrifiée) : elle résiste au gel, c'est pourquoi on l'utilise pour les poteries de jardin et les carreaux.</p>"
                            "<h4>Un peu de bentonite</h4><p>La bentonite est extrêmement plastique : on n'en ajoute qu'un peu dans une pâte pour la rendre plus plastique. Dans un émail, elle empêche la poudre de tomber au fond du seau.</p>",
                            [{"date": "blanche", "evt": "kaolin"}, {"date": "blanc crème à gris clair", "evt": "ball clay"}, {"date": "beige à brun clair", "evt": "terre à feu"},
                             {"date": "beige à brun", "evt": "terre à grès"}, {"date": "rouge", "evt": "argiles communes"}], "Les argiles par couleur"),
    "degraissants-securite": ("<h4>Pourquoi dégraisser ?</h4><p>Une pâte trop plastique colle aux mains et aux outils. En séchant, elle perd beaucoup d'eau et se rétracte : elle risque de se fissurer ou de se déformer au four. Le dégraissant réduit sa plasticité : la pâte est moins collante, elle sèche mieux, se fissure moins et se déforme moins à la cuisson.</p>"
                              "<h4>Quatre familles</h4><p>Les dégraissants <b>simples</b> (chamotte, tessons broyés de poterie sans émail) rendent la pâte moins collante tout en la gardant solide. Les <b>siliceux</b> (sable, poudre de quartz, galets de mer broyés) résistent à la chaleur et renforcent la pièce cuite. Les <b>combustibles</b> (paille, papier, sciure de bois) brûlent à la cuisson et laissent de petits trous : la pièce est plus légère. Les <b>fondants</b> (feldspath) aident la pâte à fondre : la pièce devient dure et vitrifiée.</p>"
                              "<h4>Sécurité</h4><p>Certaines matières fondantes contiennent du plomb, qui est toxique. Il faut toujours les manipuler avec précaution : gants, masque, lavage des mains.</p>",
                              [{"date": "simples", "evt": "chamotte, tessons broyés"}, {"date": "siliceux", "evt": "sable, quartz, galets broyés"},
                               {"date": "combustibles", "evt": "paille, papier, sciure"}, {"date": "fondants", "evt": "feldspath"}], "Les quatre types de dégraissants"),
    "familles-recettes": ("<h4>La chaleur transforme la pâte</h4><p>Selon les matières utilisées et la température de cuisson, on obtient des produits différents. Plus la cuisson est chaude, plus la pâte devient dure et étanche. Une terre cuite, cuite vers 1000 °C, reste poreuse ; un grès, cuit vers 1280 °C, est vitrifié et étanche, avec ou sans émail.</p>"
                          "<h4>Lire une recette</h4><p>Chaque pâte a sa recette : on indique la part de chaque matière en pourcentage. Le total fait toujours 100 %. Pour préparer 10 kg de pâte à porcelaine (25 % de chaque matière), il faut 2,5 kg de kaolin, 2,5 kg de ball clay, 2,5 kg de feldspath et 2,5 kg de silice. Pour trouver une masse, on prend le pourcentage de la masse totale : 30 % de 20 kg, c'est 6 kg.</p>", None, None),
}
for l in LECONS["lecons"]:
    texte, frise, ftitre = PLUS[l["id"]]
    l["contenu"]["cm2"] += texte
    if frise:
        l["frise"], l["frise_titre"] = frise, ftitre
EVAL["qcm"]["CM2"] += [q("Une argile primaire est…", ["restée sur place", "transportée par le vent", "très plastique"], 0, 1),
                       q("Les combustibles laissent dans la pièce…", ["de l'émail", "de petits trous", "du fer"], 1, 1)]

if __name__ == "__main__":
    ecrire("enigmes.json", ENIGMES)
    ecrire("dialogues.json", DIALOGUES)
    ecrire("lecons.json", LECONS)
    ecrire("evaluations.json", EVAL)
    ecrire("lecons-a4.json", A4)
    n1 = sum(1 for s in ENIGMES["salles"] for e in s["enigmes"] if "niveaux" not in e)
    n2 = sum(len(s["enigmes"]) for s in ENIGMES["salles"])
    print(f"✔ {TITRE} : {n1} énigmes Essentiel, {n2} énigmes Expert, 5 leçons, évaluations écrites dans {os.path.relpath(DATA)}")
