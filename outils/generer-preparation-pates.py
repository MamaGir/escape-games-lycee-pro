#!/usr/bin/env python3
"""Génère les données du jeu « Panne à l'usine » (La préparation des pâtes céramiques, CAP).

Ne pas modifier les JSON à la main : éditer ce script puis relancer
    python outils/generer-preparation-pates.py
Niveaux : les clés internes restent « cm1 » / « cm2 » (format du moteur commun) ;
l'interface du lycée affiche « Essentiel » (cm1) et « Expert » (cm2) — voir commun/lycee-pro/libelles.js.
Source du contenu : cours « La préparation des pâtes céramiques » (CAP, version V9) de l'enseignant.
Aucun chiffre ni aucune étape n'est inventé : tout vient du cours (doutes : preparation-pates/A-VERIFIER.md).
Les données sont d'abord écrites au format du jeu classique (salles), puis converties en jeu immersif
par migrer-jeu.py + outils/immersif/completer-preparation-pates.py.
"""
import json, os

ICI = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(ICI), "preparation-pates", "assets", "data")
TITRE = "Panne à l'usine"
COURS = "Cours « La préparation des pâtes céramiques », CAP"


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


def photo(base, legende="Photo d'une machine de l'usine"):
    """Balise image (fichier dans assets/images/cartes/, photos fournies par l'enseignant)."""
    return (f'<img src="assets/images/cartes/{base}.jpg" alt="{legende}" '
            'style="display:block;margin:0 auto 6px;max-width:100%;max-height:170px;border-radius:8px"><br>')


# =====================================================================================
# SALLE 1 — Le laboratoire : les deux méthodes et le vocabulaire
# =====================================================================================
S1 = [
    en("1-1", "Le tableau des mots", "association",
       {"cm1": "Le tableau du laboratoire a perdu ses définitions. Relie chaque mot à sa définition : clique sur un mot, puis sur la bonne définition.",
        "cm2": "Six mots du métier ont perdu leur définition. Reconstitue les six paires."},
       "Barbotine : mélange liquide d'argile et d'eau. Défloculant : produit qui rend la barbotine plus fluide, sans ajouter d'eau. Filtre-presse : machine qui presse la barbotine pour retirer l'eau. Atomiseur : tour qui sèche la barbotine en gouttelettes pour faire des granules. Boudineuse-désaéreuse : machine qui enlève l'air de la pâte et la fait sortir en boudin. Banc de coulage : poste où l'on remplit les moules de barbotine.",
       {"cm1": ["Les définitions sont dans l'encadré « Mots à connaître » au début du cours.", "Le nom d'une machine dit souvent ce qu'elle fait : « filtre-presse ».", "La barbotine est liquide, comme une crème."],
        "cm2": ["Commence par les mots que tu es sûr de connaître.", "« Désaéreuse » : qui enlève l'air.", "Défloculant : plus fluide, mais sans ajouter d'eau."]},
       cm1={"paires": [
           {"g": "Barbotine", "d": "Mélange liquide d'argile et d'eau"},
           {"g": "Défloculant", "d": "Produit qui rend la barbotine plus fluide, sans ajouter d'eau"},
           {"g": "Filtre-presse", "d": "Machine qui presse la barbotine pour retirer l'eau"},
           {"g": "Atomiseur", "d": "Tour qui sèche la barbotine en gouttelettes pour faire des granules"}]},
       cm2={"paires": [
           {"g": "Barbotine", "d": "Mélange liquide d'argile et d'eau"},
           {"g": "Défloculant", "d": "Produit qui rend la barbotine plus fluide, sans ajouter d'eau"},
           {"g": "Filtre-presse", "d": "Machine qui presse la barbotine pour retirer l'eau"},
           {"g": "Atomiseur", "d": "Tour qui sèche la barbotine en gouttelettes pour faire des granules"},
           {"g": "Boudineuse-désaéreuse", "d": "Machine qui enlève l'air de la pâte et la fait sortir en boudin"},
           {"g": "Banc de coulage", "d": "Poste où l'on remplit les moules de barbotine"}]},
       lecon="deux-methodes", partie="encadré « Mots à connaître »"),

    en("1-2", "Préparer une pâte, c'est…", "plan",
       {"cm1": "Le panneau de consignes du laboratoire est incomplet. Place chaque action sur la bonne ligne : clique sur une étiquette, puis sur la case. Une étiquette est en trop.",
        "cm2": "Pour chaque but, retrouve l'action qui permet de l'atteindre. Deux étiquettes sont en trop."},
       "Préparer une pâte, c'est : ajouter des dégraissants (ils limitent les fissures et les déformations), épurer le mélange (enlever les impuretés), régler l'humidité (ni trop sèche, ni trop molle) et obtenir une pâte homogène (la même partout, sans grumeaux).",
       {"cm1": ["Relis la liste « Préparer une pâte, c'est » en haut de la partie I.", "Les dégraissants sont du sable ou de la chamotte.", "Homogène veut dire : la même partout."],
        "cm2": ["Chaque but correspond à une action de la partie I.", "Une impureté est enlevée quand on épure.", "Cuire et émailler ne sont pas des étapes de la préparation."]},
       cm1={"titre": "Préparer une pâte, c'est…", "colonnes": 2,
            "cases": [{"libelle": "Éviter les fissures et les déformations", "reponse": "Ajouter des dégraissants"},
                      {"libelle": "Enlever les impuretés", "reponse": "Épurer le mélange"},
                      {"libelle": "Ni trop sèche, ni trop molle", "reponse": "Régler l'humidité"},
                      {"libelle": "La même pâte partout, sans grumeaux", "reponse": "Obtenir une pâte homogène"}],
            "etiquettes": ["Ajouter des dégraissants", "Épurer le mélange", "Régler l'humidité", "Obtenir une pâte homogène", "Cuire la pièce"]},
       cm2={"titre": "Préparer une pâte, c'est…", "colonnes": 2,
            "cases": [{"libelle": "Les dégraissants (sable, chamotte) limitent les fissures et les déformations : que fait-on ?", "reponse": "Ajouter des dégraissants"},
                      {"libelle": "On retire les impuretés du mélange : que fait-on ?", "reponse": "Épurer le mélange"},
                      {"libelle": "La pâte ne doit pas être trop sèche, ni trop molle : que fait-on ?", "reponse": "Régler l'humidité"},
                      {"libelle": "On veut la même pâte partout, sans grumeaux : que cherche-t-on ?", "reponse": "Obtenir une pâte homogène"}],
            "etiquettes": ["Ajouter des dégraissants", "Épurer le mélange", "Régler l'humidité", "Obtenir une pâte homogène", "Cuire la pièce", "Émailler la pièce"]},
       lecon="deux-methodes", partie="partie I"),

    en("1-3", "Le carnet de Karim", "vraifaux",
       {"cm1": "Karim, le technicien du laboratoire, a noté quatre phrases dans son carnet. Pour chacune, dis si elle est vraie ou fausse.",
        "cm2": "Vérifie les cinq phrases du carnet de Karim : vraie ou fausse ?"},
       "La barbotine est un mélange liquide d'argile et d'eau. Par voie humide, on part d'une barbotine, avec beaucoup d'eau. Par voie sèche, on part de blocs d'argile sèche et l'on ajoute l'eau peu à peu.",
       {"cm1": ["Relis l'encadré des deux méthodes, partie I.", "Voie humide : beaucoup d'eau.", "Voie sèche : on part d'argile sèche."],
        "cm2": ["Relis la partie I : une phrase pour chaque méthode.", "Voie humide : on obtient un liquide.", "À la fin de la voie sèche, on extrude des pains de terre."]},
       cm1={"affirmations": [
           {"txt": "La barbotine est un mélange liquide d'argile et d'eau.", "vrai": True, "explication": "C'est sa définition."},
           {"txt": "Par voie humide, on part d'argile sèche.", "vrai": False, "explication": "On part d'une barbotine."},
           {"txt": "Par voie sèche, on ajoute l'eau peu à peu.", "vrai": True, "explication": "On part de blocs d'argile sèche."},
           {"txt": "Le défloculant rend la barbotine plus épaisse.", "vrai": False, "explication": "Il la rend plus fluide, sans ajouter d'eau."}]},
       cm2={"affirmations": [
           {"txt": "Par voie humide, on mélange l'argile avec beaucoup d'eau pour obtenir un liquide.", "vrai": True, "explication": "Ce liquide est la barbotine."},
           {"txt": "Par voie sèche, on met beaucoup d'eau dès le début.", "vrai": False, "explication": "On part de blocs d'argile sèche et on ajoute l'eau peu à peu."},
           {"txt": "Par voie sèche, on extrude ensuite des pains de terre.", "vrai": True, "explication": "La pâte sort en boudins."},
           {"txt": "Une pâte homogène est la même partout, sans grumeaux.", "vrai": True, "explication": "C'est l'un des buts de la préparation."},
           {"txt": "Les dégraissants favorisent les fissures et les déformations.", "vrai": False, "explication": "Ils les limitent."}]},
       lecon="deux-methodes", partie="partie I"),

    en("1-4", "La fiche des deux méthodes", "trous", {"cm2": "Complète la fiche de Karim avec les bonnes étiquettes. Deux étiquettes sont en trop."},
       "Par voie humide, on part d'une barbotine : on mélange l'argile avec beaucoup d'eau. Par voie sèche, on part de blocs d'argile sèche et on ajoute l'eau peu à peu, puis on extrude des pains de terre.",
       {"cm2": ["Une méthode part d'un liquide, l'autre de blocs.", "« Peu à peu » : l'eau n'arrive pas d'un coup.", "Les étiquettes en trop parlent de cuisson et d'émail."]},
       expert={"texte": "<p>Par voie [[humide]], on part d'une [[barbotine]] : l'argile est mélangée avec beaucoup d'[[eau]]. Par voie [[sèche]], on part de [[blocs]] d'argile sèche, on ajoute l'eau peu à peu, puis on extrude des [[pains]] de terre.</p>",
               "etiquettes": ["humide", "barbotine", "eau", "sèche", "blocs", "pains", "émail", "cuisson"]},
       lecon="deux-methodes", partie="partie I"),
]

# =====================================================================================
# SALLE 2 — La salle de broyage : les étapes communes 1 à 5 et leurs machines
# =====================================================================================
S2 = [
    en("2-1", "La recette brouillée", "ordre",
       {"cm1": "L'écran affiche la recette de la barbotine de coulage, mais les six étapes sont dans le désordre. Range-les de la première (en haut) à la dernière (en bas), puis vérifie.",
        "cm2": "Remets dans l'ordre les six étapes de la barbotine de coulage, sans l'aide des repères."},
       "Barbotine de coulage : pesée, ajout de l'eau et du défloculant, broyage Alsing, tamisage, délayage, transfert vers les moules. Les cinq premières étapes se ressemblent pour les autres produits de la voie humide.",
       {"cm1": ["On commence par peser les poudres.", "Le défloculant arrive avec l'eau.", "La barbotine finit dans les moules, envoyée par une pompe."],
        "cm2": ["Relis le tableau des trois procédés côte à côte.", "Le tamisage vient après le broyage.", "Le délayage précède le transfert."]},
       cm1={"items": [{"txt": "Pesée", "sous": "on pèse avec précision", "rang": 1},
                      {"txt": "Ajout de l'eau et du défloculant", "sous": "on obtient une barbotine fluide", "rang": 2},
                      {"txt": "Broyage Alsing", "sous": "le grand tambour qui tourne", "rang": 3},
                      {"txt": "Tamisage", "sous": "retient les grumeaux", "rang": 4},
                      {"txt": "Délayage", "sous": "on remue en continu", "rang": 5},
                      {"txt": "Transfert vers les moules", "sous": "par une pompe", "rang": 6}]},
       cm2={"items": [{"txt": "Pesée", "rang": 1}, {"txt": "Ajout de l'eau et du défloculant", "rang": 2}, {"txt": "Broyage Alsing", "rang": 3},
                      {"txt": "Tamisage", "rang": 4}, {"txt": "Délayage", "rang": 5}, {"txt": "Transfert vers les moules", "rang": 6}]},
       lecon="etapes-communes", partie="partie II, procédé de la barbotine de coulage"),

    en("2-2", "Les plaques tombées", "qcm",
       {"cm1": "Les plaques de trois machines sont tombées. Remets le bon nom sous chaque photo.",
        "cm2": "Quatre machines ont perdu leur plaque. Retrouve le nom de chacune à partir de sa photo."},
       "Le broyeur Alsing est un grand tambour qui tourne : il broie les matières avec l'eau. Le tamis à secousses retient les grumeaux et les grains trop gros. Le délayeur remue la barbotine en continu. La boudineuse malaxe la pâte, enlève l'air et la fait sortir en boudin.",
       {"cm1": ["Le broyeur est un grand tambour.", "Le tamis vibre.", "Le délayeur est une cuve avec un agitateur."],
        "cm2": ["La boudineuse fait sortir la pâte en boudins.", "Le tamis retient les grumeaux.", "Le délayeur garde la barbotine bien mélangée."]},
       cm1={"questions": [
           {"q": photo("q-alsing") + "Quelle est cette machine ?", "options": ["Broyeur Alsing", "Délayeur", "Atomiseur"], "bonne": 0, "explication": "Grand tambour qui tourne et broie les matières avec l'eau."},
           {"q": photo("q-tamis") + "Quelle est cette machine ?", "options": ["Filtre-presse", "Tamis à secousses", "Silo"], "bonne": 1, "explication": "Il vibre et retient les grumeaux et les grains trop gros."},
           {"q": photo("q-delayeur") + "Quelle est cette machine ?", "options": ["Délayeur", "Banc de coulage", "Broyeur Alsing"], "bonne": 0, "explication": "Une cuve qui remue la barbotine en continu."}]},
       cm2={"questions": [
           {"q": photo("q-alsing") + "Quelle est cette machine ?", "options": ["Broyeur Alsing", "Délayeur", "Atomiseur", "Concasseur"], "bonne": 0, "explication": "Grand tambour qui tourne et broie les matières avec l'eau."},
           {"q": photo("q-tamis") + "Quelle est cette machine ?", "options": ["Filtre-presse", "Boudineuse", "Tamis à secousses", "Silo"], "bonne": 2, "explication": "Il retient les grumeaux et les grains trop gros."},
           {"q": photo("q-delayeur") + "Quelle est cette machine ?", "options": ["Banc de coulage", "Délayeur", "Broyeur Alsing", "Pompe"], "bonne": 1, "explication": "La barbotine y est remuée en continu pour rester bien mélangée."},
           {"q": photo("q-boudineuse") + "Quelle est cette machine ?", "options": ["Atomiseur", "Filtre-presse", "Boudineuse", "Délayeur"], "bonne": 2, "explication": "Elle malaxe la pâte, enlève l'air et la fait sortir en boudin."}]},
       lecon="etapes-communes", partie="partie II, photos des équipements"),

    en("2-3", "Le rôle de chaque machine", "association",
       {"cm1": "Relie chaque machine à ce qu'elle fait dans la salle de broyage.",
        "cm2": "Relie chaque équipement à son rôle exact dans les étapes communes."},
       "Le broyeur Alsing broie les matières premières avec l'eau. Le tamis à secousses retient les grumeaux et les grains trop gros. Le délayeur remue la barbotine en continu pour garder la même consistance. La pompe envoie la barbotine d'une machine à l'autre.",
       {"cm1": ["Chaque étape du cours explique ce que fait la machine.", "Le tamis retient ce qui est trop gros.", "La pompe déplace la barbotine."],
        "cm2": ["Relis les étapes 3, 4 et 5 de la partie II.", "« Même consistance partout » : le délayeur.", "La pompe est utilisée au tamisage et au transfert."]},
       cm1={"paires": [{"g": "Broyeur Alsing", "d": "Broie les matières avec l'eau"},
                       {"g": "Tamis à secousses", "d": "Retient les grumeaux et les grains trop gros"},
                       {"g": "Délayeur", "d": "Remue la barbotine pour qu'elle reste bien mélangée"},
                       {"g": "Pompe", "d": "Envoie la barbotine d'une machine à l'autre"}]},
       cm2={"paires": [{"g": "Broyeur Alsing", "d": "Grand tambour qui broie les matières avec l'eau : les grains deviennent très fins"},
                       {"g": "Tamis à secousses", "d": "Retient les grumeaux et les grains trop gros"},
                       {"g": "Délayeur", "d": "Remue la barbotine en continu pour garder la même consistance partout"},
                       {"g": "Pompe", "d": "Envoie la barbotine sur le tamis, puis vers la suite du procédé"},
                       {"g": "Défloculant", "d": "Ajouté en petite quantité pour rendre la barbotine plus fluide"}]},
       lecon="etapes-communes", partie="partie II, étapes 3 à 5"),

    en("2-4", "Le cadenas du broyeur", "code", {"cm2": "Le cadenas de l'armoire du broyeur a deux molettes. Trouve les deux nombres dans le cours."},
       "Les étapes 1 à 5 se ressemblent pour les trois produits de la voie humide : 5 étapes communes. La barbotine de coulage compte 6 étapes au total.",
       {"cm2": ["Le premier nombre compte les étapes qui se ressemblent (en gris dans le tableau).", "Le second nombre est le total des étapes de la barbotine de coulage.", "Relis « À retenir » sous le tableau des trois procédés."]},
       expert={"champs": [{"libelle": "Nombre d'étapes communes aux trois produits", "valeur": "5", "longueur": 1},
                          {"libelle": "Nombre d'étapes de la barbotine de coulage", "valeur": "6", "longueur": 1}]},
       lecon="etapes-communes", partie="partie II, tableau des trois procédés"),
]

# =====================================================================================
# SALLE 3 — Le hall de production : les trois produits de la voie humide
# =====================================================================================
S3 = [
    en("3-1", "Le tri des chariots", "tri",
       {"cm1": "Trois chariots attendent : pâtes plastiques, barbotine de coulage, poudres atomisées. Range chaque étiquette dans le chariot où elle intervient.",
        "cm2": "Après les étapes communes, les opérations ont été déchargées en vrac. Range les dix étiquettes dans le bon chariot."},
       "Pâtes plastiques : filtre-presse, boudineuse-désaéreuse, extrusion (colombin). Barbotine de coulage : défloculant avec l'eau, transfert vers les moules, banc de coulage. Poudres atomisées : atomiseur, pulvérisation par une tête centrifuge, air chaud d'environ 400 °C, stockage dans un silo.",
       {"cm1": ["Pâtes plastiques : on retire l'eau, puis l'air, et la pâte sort en boudin.", "Coulage : on remplit des moules.", "Poudres : on sèche très vite et on stocke."],
        "cm2": ["Relis le tableau des trois procédés côte à côte.", "Le défloculant est ajouté pour la barbotine de coulage.", "L'air chaud et le silo vont avec l'atomiseur."]},
       cm1={"colonnes": [{"id": "pla", "titre": "Pâtes plastiques"}, {"id": "cou", "titre": "Barbotine de coulage"}, {"id": "pou", "titre": "Poudres atomisées"}],
            "cartes": [{"txt": "Filtre-presse", "col": "pla"}, {"txt": "Boudineuse-désaéreuse", "col": "pla"},
                       {"txt": "Banc de coulage", "col": "cou"}, {"txt": "Remplissage des moules", "col": "cou"},
                       {"txt": "Atomiseur", "col": "pou"}, {"txt": "Silo de stockage", "col": "pou"}]},
       cm2={"colonnes": [{"id": "pla", "titre": "Pâtes plastiques"}, {"id": "cou", "titre": "Barbotine de coulage"}, {"id": "pou", "titre": "Poudres atomisées"}],
            "cartes": [{"txt": "Filtre-presse", "col": "pla"}, {"txt": "Boudineuse-désaéreuse", "col": "pla"}, {"txt": "Colombin (boudin)", "col": "pla"},
                       {"txt": "Défloculant ajouté à l'eau", "col": "cou"}, {"txt": "Banc de coulage", "col": "cou"}, {"txt": "Remplissage des moules", "col": "cou"},
                       {"txt": "Atomiseur", "col": "pou"}, {"txt": "Pulvérisation (tête centrifuge)", "col": "pou"},
                       {"txt": "Air chaud (environ 400 °C)", "col": "pou"}, {"txt": "Silo de stockage", "col": "pou"}]},
       lecon="trois-produits", partie="partie II, les 3 procédés côte à côte"),

    en("3-2", "Les commandes clients", "qcm",
       {"cm1": "Trois clients ont laissé une commande. Choisis le bon produit pour chacun.",
        "cm2": "Quatre clients ont laissé une commande. Livre le bon produit à chacun."},
       "Barbotine de coulage : liquide bien fluide, pour remplir les moules. Pâte plastique : ferme et malléable, pour modeler et tourner. Poudre atomisée : petits granules secs, pour le pressage industriel.",
       {"cm1": ["Liquide : pense au coulage.", "Pâte ferme : on la modèle ou on la tourne.", "Granules secs : pour une presse."],
        "cm2": ["Relis les trois cartes de la partie II.", "Un moule en plâtre se remplit avec un liquide.", "Le pressage industriel utilise des petits granules secs."]},
       cm1={"questions": [
           {"q": "Je veux remplir des moules en plâtre.", "options": ["Barbotine", "Pâte plastique", "Poudre atomisée"], "bonne": 0, "explication": "La barbotine de coulage est un liquide bien fluide."},
           {"q": "Je veux modeler ou tourner une pièce à la main.", "options": ["Barbotine", "Pâte plastique", "Poudre atomisée"], "bonne": 1, "explication": "Pâte ferme et malléable."},
           {"q": "Je veux presser des pièces avec une machine, en industrie.", "options": ["Barbotine", "Pâte plastique", "Poudre atomisée"], "bonne": 2, "explication": "Petits granules secs, pour le pressage industriel."}]},
       cm2={"questions": [
           {"q": "Je veux remplir des moules en plâtre.", "options": ["Barbotine", "Pâte plastique", "Poudre atomisée"], "bonne": 0, "explication": "La barbotine de coulage est un liquide bien fluide."},
           {"q": "Je veux modeler ou tourner une pièce à la main.", "options": ["Barbotine", "Pâte plastique", "Poudre atomisée"], "bonne": 1, "explication": "Pâte ferme et malléable."},
           {"q": "Je veux presser des pièces avec une machine, en industrie.", "options": ["Barbotine", "Pâte plastique", "Poudre atomisée"], "bonne": 2, "explication": "Petits granules secs, pour le pressage industriel."},
           {"q": "Je veux un liquide bien fluide qui remplit régulièrement les moules.", "options": ["Barbotine", "Pâte plastique", "Poudre atomisée"], "bonne": 0, "explication": "C'est le rôle de la barbotine de coulage, rendue fluide par le défloculant."}]},
       lecon="trois-produits", partie="partie II, les trois produits"),

    en("3-3", "Les huit étapes des pâtes plastiques", "ordre",
       {"cm1": "Une pâte plastique passe par huit étapes. Range-les de la première (en haut) à la dernière (en bas).",
        "cm2": "Remets dans l'ordre les huit étapes de la préparation des pâtes plastiques, sans repères."},
       "Pâtes plastiques en 8 étapes : pesée, ajout de l'eau, broyage, tamisage, délayage, filtration (filtre-presse), désaération (boudineuse-désaéreuse), extrusion (tête d'extrusion, souvent en colombin).",
       {"cm1": ["Les cinq premières étapes sont les étapes communes.", "On retire l'eau avant d'enlever l'air.", "La pâte sort en boudin à la fin."],
        "cm2": ["Après le délayage vient la filtration.", "Le filtre-presse précède la boudineuse.", "L'extrusion est la dernière étape."]},
       cm1={"items": [{"txt": "Pesée", "sous": "étape commune", "rang": 1},
                      {"txt": "Ajout de l'eau", "sous": "on obtient une barbotine", "rang": 2},
                      {"txt": "Broyage", "sous": "broyeur Alsing", "rang": 3},
                      {"txt": "Tamisage", "sous": "tamis à secousses", "rang": 4},
                      {"txt": "Délayage", "sous": "délayeur", "rang": 5},
                      {"txt": "Filtration", "sous": "filtre-presse : on retire l'eau", "rang": 6},
                      {"txt": "Désaération", "sous": "boudineuse : on retire l'air", "rang": 7},
                      {"txt": "Extrusion", "sous": "la pâte sort en boudin", "rang": 8}]},
       cm2={"items": [{"txt": "Pesée", "rang": 1}, {"txt": "Ajout de l'eau", "rang": 2}, {"txt": "Broyage", "rang": 3}, {"txt": "Tamisage", "rang": 4},
                      {"txt": "Délayage", "rang": 5}, {"txt": "Filtration (filtre-presse)", "rang": 6}, {"txt": "Désaération (boudineuse)", "rang": 7},
                      {"txt": "Extrusion", "rang": 8}]},
       lecon="trois-produits", partie="partie II, 1. Les pâtes plastiques"),

    en("3-4", "L'étape de trop", "intrus", {"cm2": "Sur le chariot de la barbotine de coulage, une étape n'a rien à y faire : trouve l'intrus."},
       "La barbotine de coulage n'est pas filtrée : on ne retire pas l'eau, car elle doit rester très fluide. La filtration au filtre-presse appartient aux pâtes plastiques.",
       {"cm2": ["Une seule étape sert à retirer l'eau.", "La barbotine de coulage doit rester fluide.", "Cette machine presse la barbotine entre des toiles."]},
       expert={"cartes": [{"txt": "Broyage Alsing", "sous": "étape 3", "intrus": False},
                          {"txt": "Tamisage", "sous": "étape 4", "intrus": False},
                          {"txt": "Délayage", "sous": "étape 5", "intrus": False},
                          {"txt": "Filtration (filtre-presse)", "sous": "on retire l'eau", "intrus": True},
                          {"txt": "Transfert vers les moules", "sous": "étape 6", "intrus": False}]},
       lecon="trois-produits", partie="partie II, 2. La barbotine de coulage"),
]

# =====================================================================================
# SALLE 4 — La tour d'atomisation : machines du hall, poudres et entreprises
# =====================================================================================
S4 = [
    en("4-1", "Les machines du hall", "qcm",
       {"cm1": "Trois grandes machines du hall n'ont plus de plaque. Rends-leur leur nom.",
        "cm2": "Cinq grandes machines du hall n'ont plus de plaque. Rends-leur leur nom."},
       "Le filtre-presse presse la barbotine entre des toiles pour retirer l'eau. L'atomiseur est une grande tour qui sèche la barbotine pulvérisée. Le silo stocke la poudre sèche. La pompe envoie la barbotine d'une machine à l'autre. Le banc de coulage sert à remplir les moules.",
       {"cm1": ["Le silo stocke la poudre.", "L'atomiseur est une tour.", "Le filtre-presse presse la barbotine entre des plaques."],
        "cm2": ["La pompe envoie la barbotine d'une machine à l'autre.", "Le banc de coulage sert à remplir les moules.", "Relis les photos des procédés dans la partie II."]},
       cm1={"questions": [
           {"q": photo("q-filtre") + "Quelle est cette machine ?", "options": ["Filtre-presse", "Silo", "Atomiseur"], "bonne": 0, "explication": "Elle presse la barbotine entre des toiles pour retirer l'eau."},
           {"q": photo("q-atomiseur") + "Quelle est cette machine ?", "options": ["Silo", "Atomiseur", "Banc de coulage"], "bonne": 1, "explication": "Une grande tour qui sèche la barbotine pulvérisée avec de l'air chaud."},
           {"q": photo("q-silo") + "Quelle est cette machine ?", "options": ["Silo", "Pompe", "Filtre-presse"], "bonne": 0, "explication": "La poudre sèche y est stockée."}]},
       cm2={"questions": [
           {"q": photo("q-coulage") + "Quelle est cette installation ?", "options": ["Banc de coulage", "Filtre-presse", "Silo", "Pompe"], "bonne": 0, "explication": "Le poste où l'on place les moules pour les remplir de barbotine."},
           {"q": photo("q-filtre") + "Quelle est cette machine ?", "options": ["Atomiseur", "Filtre-presse", "Boudineuse", "Délayeur"], "bonne": 1, "explication": "Elle presse la barbotine entre des toiles pour retirer l'eau."},
           {"q": photo("q-pompe") + "Quel est cet équipement ?", "options": ["Silo", "Tamis à secousses", "Pompe", "Concasseur"], "bonne": 2, "explication": "Elle envoie la barbotine d'une machine à l'autre."},
           {"q": photo("q-atomiseur") + "Quelle est cette machine ?", "options": ["Atomiseur", "Broyeur Alsing", "Silo", "Banc de coulage"], "bonne": 0, "explication": "Une tour où la barbotine pulvérisée est séchée par de l'air chaud."},
           {"q": photo("q-silo") + "Quel est cet équipement ?", "options": ["Délayeur", "Atomiseur", "Filtre-presse", "Silo"], "bonne": 3, "explication": "La poudre sèche est évacuée vers un silo pour être stockée."}]},
       lecon="atomisation-machines", partie="partie II, photos des équipements"),

    en("4-2", "La tour d'atomisation", "ordre",
       {"cm1": "Sur l'écran de l'atomiseur, les cinq dernières étapes des poudres atomisées se sont mélangées. Range-les de la première (en haut) à la dernière (en bas).",
        "cm2": "Sur l'écran de l'atomiseur, les dix étapes des poudres atomisées se sont mélangées. Remets-les dans l'ordre, des cinq étapes communes jusqu'au stockage."},
       "Poudres atomisées en 10 étapes : pesée, ajout de l'eau, broyage, tamisage, délayage, transfert vers l'atomiseur, pulvérisation (gouttelettes), séchage (air chaud, environ 400 °C), granules, stockage dans un silo.",
       {"cm1": ["Après le délayage, une pompe envoie la barbotine vers l'atomiseur.", "Une tête centrifuge fait des gouttelettes.", "Les granules sont stockés à la fin."],
        "cm2": ["Les cinq premières étapes sont les étapes communes.", "Pulvérisation avant séchage : d'abord les gouttelettes.", "L'eau s'évapore très vite : il reste des granules."]},
       cm1={"items": [{"txt": "Transfert vers l'atomiseur", "sous": "une pompe envoie la barbotine", "rang": 1},
                      {"txt": "Pulvérisation", "sous": "tête centrifuge : gouttelettes", "rang": 2},
                      {"txt": "Séchage", "sous": "air chaud, environ 400 °C", "rang": 3},
                      {"txt": "Granules", "sous": "l'eau s'évapore très vite", "rang": 4},
                      {"txt": "Stockage", "sous": "dans un silo", "rang": 5}]},
       cm2={"items": [{"txt": "Pesée", "rang": 1}, {"txt": "Ajout de l'eau", "rang": 2}, {"txt": "Broyage", "rang": 3}, {"txt": "Tamisage", "rang": 4},
                      {"txt": "Délayage", "rang": 5}, {"txt": "Transfert vers l'atomiseur", "rang": 6}, {"txt": "Pulvérisation", "rang": 7},
                      {"txt": "Séchage", "rang": 8}, {"txt": "Granules", "rang": 9}, {"txt": "Stockage", "rang": 10}]},
       lecon="atomisation-machines", partie="partie II, 3. Les poudres atomisées"),

    en("4-3", "Le cahier du chef", "vraifaux",
       {"cm1": "Le cahier de consignes du chef d'atelier contient des erreurs. Pour chaque phrase, dis si elle est vraie ou fausse.",
        "cm2": "Six phrases du cahier du chef d'atelier : trouve les erreurs et lis les corrections."},
       "Le défloculant rend la barbotine plus fluide. Dans l'atomiseur, les gouttelettes sont séchées par de l'air chaud. La boudineuse-désaéreuse enlève l'air de la pâte. Le filtre-presse retire l'eau de la barbotine.",
       {"cm1": ["Défloculant : plus fluide.", "Atomiseur : de l'air chaud.", "Filtre-presse : il presse pour retirer l'eau."],
        "cm2": ["Relis l'encadré « Mots à connaître ».", "Le filtre-presse retire l'eau, il n'en ajoute pas.", "La boudineuse-désaéreuse enlève l'air."]},
       cm1={"affirmations": [
           {"txt": "Dans l'atomiseur, les gouttelettes sont séchées par de l'air chaud.", "vrai": True, "explication": "Environ 400 °C."},
           {"txt": "Le filtre-presse ajoute de l'eau à la pâte.", "vrai": False, "explication": "Il enlève l'excès d'eau de la barbotine."},
           {"txt": "La boudineuse-désaéreuse enlève l'air de la pâte.", "vrai": True, "explication": "Elle malaxe aussi la pâte et la fait sortir en boudin."},
           {"txt": "Le défloculant rend la barbotine plus épaisse.", "vrai": False, "explication": "Il la rend plus fluide, sans ajouter d'eau."}]},
       cm2={"affirmations": [
           {"txt": "La barbotine est un mélange d'argile et d'eau.", "vrai": True, "explication": "Un mélange liquide, de la consistance d'une crème."},
           {"txt": "Le défloculant rend la barbotine plus épaisse.", "vrai": False, "explication": "Correction : il la rend plus fluide, sans ajouter d'eau."},
           {"txt": "Dans l'atomiseur, les gouttelettes sont séchées par de l'air chaud.", "vrai": True, "explication": "Courant d'air chaud d'environ 400 °C."},
           {"txt": "Par voie sèche, on met beaucoup d'eau dès le début.", "vrai": False, "explication": "Correction : on ajoute l'eau peu à peu."},
           {"txt": "La boudineuse-désaéreuse enlève l'air de la pâte.", "vrai": True, "explication": "Sans bulles d'air, on évite les défauts à la cuisson."},
           {"txt": "Le filtre-presse ajoute de l'eau à la pâte.", "vrai": False, "explication": "Correction : il enlève l'excès d'eau de la barbotine."}]},
       lecon="atomisation-machines", partie="encadré « Mots à connaître » et partie II"),

    en("4-4", "Les trois entreprises", "qcm", {"cm2": "Trois entreprises visitent l'usine. Elles travaillent par voie humide, mais pas avec les mêmes produits. Réponds à chaque question."},
       "Par voie humide, une entreprise peut fabriquer un seul produit, deux ou trois. Elle n'utilise que les équipements utiles à ses produits, mais toutes commencent par les étapes communes.",
       {"cm2": ["Chaque entreprise ne suit que le procédé de ses produits.", "Les étapes 1 à 5 se ressemblent pour tous les produits de la voie humide.", "Relis la phrase en gras sous le tableau : « une entreprise peut ne faire qu'un seul de ces produits »."]},
       expert={"questions": [
           {"q": "L'entreprise A ne fabrique que de la barbotine de coulage. A-t-elle besoin d'un atomiseur ?", "options": ["Oui", "Non"], "bonne": 1, "explication": "L'atomiseur sert seulement aux poudres atomisées."},
           {"q": "L'entreprise B ne fabrique que des pâtes plastiques. A-t-elle besoin d'un filtre-presse ?", "options": ["Oui", "Non"], "bonne": 0, "explication": "La filtration fait partie du procédé des pâtes plastiques."},
           {"q": "L'entreprise C ne fabrique que des poudres atomisées. A-t-elle besoin d'un banc de coulage ?", "options": ["Oui", "Non"], "bonne": 1, "explication": "Le banc de coulage sert à remplir les moules de barbotine."},
           {"q": "Les trois entreprises commencent-elles toutes par peser les poudres et ajouter de l'eau ?", "options": ["Oui", "Non"], "bonne": 0, "explication": "Les étapes 1 à 5 se ressemblent pour les trois produits."},
           {"q": "Une entreprise qui travaille par voie humide doit-elle fabriquer obligatoirement les trois produits ?", "options": ["Oui", "Non"], "bonne": 1, "explication": "Elle peut en fabriquer un seul, deux ou trois."}]},
       lecon="atomisation-machines", partie="partie II et synthèse"),
]

# =====================================================================================
# SALLE 5 — L'atelier voie sèche : partir d'argile sèche, et la sécurité
# =====================================================================================
S5 = [
    en("5-1", "Le cahier de l'atelier", "trous",
       {"cm1": "Le cahier de l'atelier est taché : il manque un mot dans chaque phrase. Place les mots dans les trous.",
        "cm2": "Il manque un mot dans chaque phrase du cahier. Attention : une étiquette est en trop."},
       "Voie sèche : concassage (on casse les gros blocs), mouillage (on humidifie l'argile), mélange de l'argile et de l'eau, désaération dans la boudineuse-désaéreuse, extrusion (la pâte sort en boudins).",
       {"cm1": ["Suis l'ordre du cours : concassage, mouillage, mélange, désaération, extrusion.", "On casse d'abord les gros blocs.", "À la fin, la pâte sort en boudins."],
        "cm2": ["Étape 4 : la machine enlève l'air.", "Mouiller, c'est humidifier.", "Une étiquette appartient à la voie humide."]},
       cm1={"texte": "<p>Étape 1 : le [[concassage]] de l'argile (on casse les gros blocs).<br>Étape 2 : le [[mouillage]] (on humidifie l'argile).<br>Étape 3 : le [[mélange]] de l'argile et de l'eau.<br>Étape 4 : la [[boudineuse-désaéreuse]], qui enlève l'air de la pâte.<br>Étape 5 : l'[[extrusion]] : la pâte sort en boudins.</p>",
            "etiquettes": ["concassage", "mouillage", "mélange", "boudineuse-désaéreuse", "extrusion"]},
       cm2={"texte": "<p>Étape 1 : le [[concassage]] de l'argile (on casse les gros blocs).<br>Étape 2 : le [[mouillage]] (on humidifie l'argile).<br>Étape 3 : le [[mélange]] de l'argile et de l'eau, pour obtenir une pâte homogène.<br>Étape 4 : le passage dans la [[boudineuse-désaéreuse]], qui enlève l'air de la pâte.<br>Étape 5 : l'[[extrusion]] : la pâte sort en boudins.</p>",
            "etiquettes": ["concassage", "mouillage", "mélange", "boudineuse-désaéreuse", "extrusion", "tamisage"]},
       lecon="voie-seche-securite", partie="partie III"),

    en("5-2", "Humide, sèche ou les deux", "tri",
       {"cm1": "Les étiquettes du magasin sont mélangées. Range chacune dans la bonne colonne : voie humide, voie sèche ou les deux.",
        "cm2": "Range les neuf étiquettes : voie humide, voie sèche ou les deux méthodes."},
       "Voie humide : broyeur Alsing, atomiseur, filtre-presse, départ d'une barbotine. Voie sèche : concasseur, mélangeur, départ de blocs d'argile sèche. Les deux méthodes : boudineuse-désaéreuse et tête d'extrusion.",
       {"cm1": ["Deux machines servent dans les deux méthodes : celle qui enlève l'air et celle qui fait sortir le boudin.", "Le concasseur casse des blocs secs.", "L'Alsing travaille avec l'eau."],
        "cm2": ["Relis le tableau « Les deux méthodes » de la synthèse.", "Le mélangeur n'apparaît qu'en voie sèche.", "La boudineuse-désaéreuse est dans les deux colonnes du tableau des machines."]},
       cm1={"colonnes": [{"id": "hum", "titre": "Voie humide"}, {"id": "sec", "titre": "Voie sèche"}, {"id": "les", "titre": "Les deux"}],
            "cartes": [{"txt": "Broyeur Alsing", "col": "hum"}, {"txt": "Atomiseur", "col": "hum"},
                       {"txt": "Concasseur", "col": "sec"}, {"txt": "Mélangeur", "col": "sec"},
                       {"txt": "Boudineuse-désaéreuse", "col": "les"}, {"txt": "Tête d'extrusion", "col": "les"}]},
       cm2={"colonnes": [{"id": "hum", "titre": "Voie humide"}, {"id": "sec", "titre": "Voie sèche"}, {"id": "les", "titre": "Les deux"}],
            "cartes": [{"txt": "Broyeur Alsing", "col": "hum"}, {"txt": "Atomiseur", "col": "hum"}, {"txt": "On part d'une barbotine", "col": "hum"}, {"txt": "Filtre-presse", "col": "hum"},
                       {"txt": "Concasseur", "col": "sec"}, {"txt": "Mélangeur", "col": "sec"}, {"txt": "On part de blocs d'argile sèche", "col": "sec"},
                       {"txt": "Boudineuse-désaéreuse", "col": "les"}, {"txt": "Tête d'extrusion", "col": "les"}]},
       lecon="voie-seche-securite", partie="synthèse, tableau des deux méthodes"),

    en("5-3", "Le dernier verrou", "intrus",
       {"cm1": "Avant d'ouvrir les sacs de poudre, il faut les bons réflexes. Un seul de ces gestes est dangereux : trouve-le.",
        "cm2": "Les poudres de matières premières sont fines et volatiles. Un seul de ces gestes est dangereux : trouve l'intrus."},
       "Les poudres sont fines et volatiles : elles se mettent en suspension dans l'air. On porte un masque anti-poussières, on ouvre les sacs avec précaution et on évite de respirer la poudre. Souffler sur de la poudre renversée la met en suspension dans l'air.",
       {"cm1": ["Une poudre volatile se soulève facilement.", "Trois gestes protègent.", "Un geste fait voler la poudre."],
        "cm2": ["Une poudre volatile se met en suspension dans l'air.", "Les bons gestes évitent de soulever la poudre et de la respirer.", "L'intrus envoie la poudre dans l'air."]},
       cm1={"cartes": [{"txt": "Porter un masque anti-poussières", "intrus": False}, {"txt": "Ouvrir les sacs avec précaution", "intrus": False},
                       {"txt": "Souffler sur la poudre renversée pour nettoyer", "intrus": True}, {"txt": "Éviter de respirer la poudre", "intrus": False}]},
       cm2={"cartes": [{"txt": "Porter un masque anti-poussières", "sous": "protège les poumons", "intrus": False},
                       {"txt": "Ouvrir les sacs avec précaution", "sous": "sans soulever la poudre", "intrus": False},
                       {"txt": "Éviter de respirer la poudre", "sous": "poudre fine et volatile", "intrus": False},
                       {"txt": "Ouvrir le sac d'un coup sec, en hauteur", "sous": "pour gagner du temps", "intrus": True},
                       {"txt": "Garder le masque pour peser", "sous": "même pour une petite quantité", "intrus": False}]},
       lecon="voie-seche-securite", partie="partie II, étape 1 (pesée : poudres fines et volatiles)"),

    en("5-4", "La voie sèche dans l'ordre", "ordre", {"cm2": "Le tableau de la voie sèche est tombé. Remets dans l'ordre les cinq étapes, du concassage à l'extrusion."},
       "Voie sèche : concassage (concasseur), mouillage, mélange, désaération (boudineuse-désaéreuse), extrusion. On obtient des pains de terre.",
       {"cm2": ["On commence par casser les gros blocs.", "L'eau est ajoutée avant le mélange.", "L'extrusion est la dernière étape : la pâte sort en boudins."]},
       expert={"items": [{"txt": "Concassage", "rang": 1}, {"txt": "Mouillage", "rang": 2}, {"txt": "Mélange", "rang": 3},
                         {"txt": "Désaération", "rang": 4}, {"txt": "Extrusion", "rang": 5}]},
       lecon="voie-seche-securite", partie="partie III"),
]

TITRES = ["Le laboratoire", "La salle de broyage", "Le hall de production", "La tour d'atomisation", "L'atelier voie sèche"]
SOUS = ["Les deux méthodes et le vocabulaire", "Les étapes communes et leurs machines", "Les trois produits de la voie humide",
        "Les poudres atomisées, les machines du hall, les entreprises", "Partir d'argile sèche, et la sécurité"]
ENIGMES = {
    "metadata": {
        "jeu": TITRE, "version": 1,
        "differenciation": "Essentiel (clé cm1) : 3 énigmes par salle (15). Expert (clé cm2) : 4 énigmes par salle (20). Le champ \"niveaux\": [\"CM2\"] réserve une énigme au niveau Expert.",
        "types": ["qcm", "vraifaux", "association", "ordre", "tri", "trous", "code", "intrus", "plan"],
        "sources": COURS + " (version V9, document de l'enseignant). Points à confirmer : A-VERIFIER.md.",
        "media": "Photos des machines : assets/images/cartes/q-*.jpg (fournies par l'enseignant), insérées dans les questions des énigmes 2-2 et 4-1."
    },
    "salles": [{"num": i + 1, "titre": f"{TITRES[i]} — {SOUS[i]}", "enigmes": s} for i, s in enumerate([S1, S2, S3, S4, S5])]
}

# =====================================================================================
# DIALOGUES (personnages inventés)
# =====================================================================================
P = {"nadia": ("Nadia", "Technicienne de maintenance, elle accueille les stagiaires et guide l'équipe"),
     "karim": ("Karim", "Technicien du laboratoire"),
     "elodie": ("Élodie", "Conductrice de la salle de broyage"),
     "hugo": ("Hugo", "Responsable du hall de production"),
     "sofiane": ("Sofiane", "Conducteur de l'atomiseur"),
     "samia": ("Samia", "Responsable de l'atelier voie sèche")}
MOTS = ["BARBOTINE", "DÉLAYAGE", "PRODUITS", "ATOMISEUR", "EXTRUSION"]
DECORS = ["laboratoire", "broyage", "hall", "atomisation", "voie-seche"]
LIEUX = ["Le laboratoire de l'usine Terres et Feux", "La salle de broyage, derrière le laboratoire", "Le hall de production de l'usine",
         "La tour d'atomisation, au fond du hall", "L'atelier voie sèche, au bout du bâtiment"]
DESCR = ["Une paillasse, une balance de précision, des sacs de poudre numérotés. Au mur, le tableau des mots du métier.",
         "Un grand tambour tourne doucement, un tamis vibre au-dessus d'une cuve où la barbotine est remuée en continu.",
         "Trois chariots attendent côte à côte, devant un filtre-presse, un banc de coulage et une rangée de moules.",
         "Une tour métallique domine le hall. À côté, un silo, des tuyaux, et un écran où défilent les étapes.",
         "Des blocs d'argile sèche, un concasseur, un mélangeur et une boudineuse-désaéreuse alignés."]
SENS = [["À voir : la balance et le tableau des mots", "À entendre : le bourdonnement des néons", "À sentir : la poussière d'argile"],
        ["À voir : le tambour qui tourne", "À entendre : le tamis qui vibre", "À toucher : une barbotine épaisse comme une crème"],
        ["À voir : les trois chariots", "À entendre : la pompe qui ronronne", "À sentir : l'argile humide"],
        ["À voir : la tour et son silo", "À entendre : le souffle de l'air chaud", "À sentir : la chaleur qui monte"],
        ["À voir : les blocs d'argile sèche", "À entendre : le concasseur", "À sentir : la poussière fine dans l'air"]]
INTRO = [("karim", "Entrez, ne touchez à rien. Quand la ligne s'est arrêtée, le chef a verrouillé le coffre de relance. Pour l'ouvrir, il faut cinq mots : un par salle. Le premier est ici. Mais d'abord, montrez-moi que vous connaissez le vocabulaire et les deux méthodes de préparation : voie humide et voie sèche."),
         ("elodie", "Ici, on prépare la barbotine : on pèse, on ajoute l'eau, on broie, on tamise, on délaie. Ces étapes se ressemblent pour tous les produits de la voie humide. Les plaques de mes machines sont tombées et la recette est brouillée. Remettez de l'ordre, et je vous donne le deuxième mot."),
         ("hugo", "Bienvenue dans le hall. Après les étapes communes, le procédé change selon le produit : pâtes plastiques, barbotine de coulage ou poudres atomisées. Trois chariots, des commandes de clients qui attendent. Montrez-moi que vous savez qui fait quoi."),
         ("sofiane", "L'atomiseur est à l'arrêt, et c'est lui qui a déclenché la panne. Avant de le relancer, je dois être sûr que vous connaissez la tour, le silo, les machines du hall, et que vous savez qu'une usine ne fabrique pas forcément les trois produits."),
         ("samia", "Dernière salle. Ici, on ne part pas d'une barbotine mais de blocs d'argile sèche. L'eau, on la met peu à peu. Et attention : les poudres sont fines et volatiles. Prouvez-moi que vous connaissez la voie sèche et les bons gestes, et le coffre s'ouvrira.")]
REUSSITE = [("karim", "Bien. Le mot écrit sur ma fiche est <b>BARBOTINE</b> : le liquide de départ de toute la voie humide. Passez à la salle de broyage, Élodie vous attend."),
            ("elodie", "Les machines ont retrouvé leur nom et la recette est en ordre. Mon mot est <b>DÉLAYAGE</b> : on remue la barbotine sans s'arrêter. Hugo vous attend dans le hall."),
            ("hugo", "Les commandes partent chez les bons clients. Mon mot est <b>PRODUITS</b> : trois produits, trois procédés. Sofiane vous attend à la tour d'atomisation."),
            ("sofiane", "La tour peut repartir. Mon mot est <b>ATOMISEUR</b>. Il reste la dernière salle, celle de la voie sèche : Samia vous attend.")]
FIN = ("nadia", "Samia vous a donné le dernier mot : <b>EXTRUSION</b>. Vous avez les cinq mots ! Tapez-les dans le coffre de relance, dans l'ordre des salles, et la ligne repartira avant la fermeture. N'oubliez pas : cette usine est un exemple, ailleurs les machines et les étapes peuvent être différentes.")

DIALOGUES = {
    "metadata": {"jeu": TITRE, "sujet": "La préparation des pâtes céramiques : voie humide et voie sèche, étapes communes, pâtes plastiques, barbotine de coulage, poudres atomisées, équipements — CAP Décoration sur céramique",
                 "niveaux": ["Essentiel", "Expert"], "sources": COURS},
    "personnages": {k: {"nom": v[0], "role": v[1]} for k, v in P.items()},
    "intro_accueil": "Bonjour, je suis Nadia, technicienne de maintenance de l'usine Terres et Feux. Vendredi, 16 h 50 : la ligne de préparation des pâtes s'est arrêtée d'un coup. Le chef d'atelier est parti en laissant le coffre de relance verrouillé, les écrans sont noirs et les plaques des machines sont tombées. Vous êtes en stage : traversez les cinq salles, résolvez les énigmes, récupérez les cinq mots du coffre et relancez la production avant la fermeture. On commence par le laboratoire ?",
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
    {"id": "deux-methodes", "salle": 1, "icone": "I", "titre": "Les deux méthodes de préparation", "duree": "3 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Dire ce que veut dire préparer une pâte", "Distinguer la voie humide et la voie sèche", "Connaître le vocabulaire de base"],
     "contenu": {
         "cm1": "<h4>Préparer une pâte</h4><p>Une <b>pâte céramique</b> est un mélange d'argile, d'eau et d'autres matières. Pour la travailler, il faut la <b>préparer</b> : ajouter des <b>dégraissants</b>, enlever les impuretés, régler l'humidité et obtenir une pâte <b>homogène</b>.</p><h4>Deux méthodes</h4><p><b>Voie humide</b> : on part d'une <b>barbotine</b>, un liquide d'argile et de beaucoup d'eau.<br><b>Voie sèche</b> : on part de <b>blocs d'argile sèche</b> et on ajoute l'eau peu à peu.</p>",
         "cm2": "<h4>Préparer une pâte, c'est…</h4><ul><li>ajouter des <b>dégraissants</b> (sable, chamotte…), qui limitent les fissures et les déformations ;</li><li><b>épurer</b> le mélange : enlever les impuretés ;</li><li><b>régler l'humidité</b> : ni trop sèche, ni trop molle ;</li><li>obtenir une pâte <b>homogène</b> : la même partout, sans grumeaux.</li></ul><h4>Deux méthodes</h4><p>Par <b>voie humide</b>, on mélange l'argile avec beaucoup d'eau : on obtient un liquide, la <b>barbotine</b>. On la transforme ensuite en pâtes plastiques, en barbotine de coulage ou en poudres atomisées.</p><p>Par <b>voie sèche</b>, on part de blocs d'argile sèche et on ajoute l'eau peu à peu. On extrude ensuite des pains de terre.</p><div class='encadre'>Le <b>défloculant</b> est un produit, ajouté en petite quantité, qui rend la barbotine plus fluide sans ajouter d'eau.</div><p>Une entreprise ne fait pas forcément tout : chacune choisit ses produits et ses équipements.</p>"},
     "lexique": [{"mot": "barbotine", "def": "mélange liquide d'argile et d'eau, de la consistance d'une crème"},
                 {"mot": "dégraissants", "def": "matières ajoutées à l'argile pour éviter les fissures et les déformations"},
                 {"mot": "défloculant", "def": "produit qui rend la barbotine plus fluide, sans ajouter d'eau"},
                 {"mot": "homogène", "def": "la même partout, sans grumeaux"}],
     "frise": [{"date": "voie humide", "evt": "on part d'une barbotine (beaucoup d'eau)"}, {"date": "voie sèche", "evt": "on part d'argile sèche (eau ajoutée peu à peu)"}],
     "frise_titre": "Les deux méthodes",
     "document": {"type": "text", "titre": "Une pâte céramique", "contenu": "Pâte céramique : mélange d'argile et d'autres matières, prêt à être mis en forme.", "source": COURS + ", « Mots à connaître »."},
     "sources": COURS + ", encadré « Mots à connaître » et partie I."},
    {"id": "etapes-communes", "salle": 2, "icone": "II", "titre": "Les étapes communes de la voie humide", "duree": "3 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Citer dans l'ordre les cinq étapes communes", "Associer chaque étape à sa machine", "Ordonner la barbotine de coulage"],
     "contenu": {
         "cm1": "<h4>Cinq étapes qui se ressemblent</h4><ol><li><b>Pesée</b> des poudres.</li><li><b>Ajout de l'eau</b> : on obtient la barbotine.</li><li><b>Broyage</b> dans un broyeur Alsing.</li><li><b>Tamisage</b> sur un tamis à secousses.</li><li><b>Délayage</b> dans un délayeur.</li></ol><p>Pour la barbotine de coulage, une 6e étape : le <b>transfert vers les moules</b>.</p>",
         "cm2": "<h4>De la poudre à la barbotine</h4><ol><li><b>Pesée</b> : on pèse avec précision les matières premières en poudre, fines et volatiles. La recette dépend des qualités voulues pour la pièce finie.</li><li><b>Ajout de l'eau</b> : on obtient un liquide, la barbotine. Pour le coulage, on ajoute aussi du <b>défloculant</b>.</li><li><b>Broyage</b> : dans un <b>broyeur Alsing</b>, grand tambour qui tourne, les grains deviennent très fins.</li><li><b>Tamisage</b> : une pompe envoie la barbotine sur un <b>tamis à secousses</b>, qui retient les grumeaux et les grains trop gros.</li><li><b>Délayage</b> : la barbotine est remuée en continu dans un <b>délayeur</b> pour garder la même consistance partout.</li></ol><div class='encadre'>Les étapes 1 à 5 se ressemblent : c'est la suite qui change selon le produit voulu.</div><p>Barbotine de coulage : <b>6 étapes</b>. La 6e est le transfert vers les moules, par une pompe, sur le banc de coulage.</p>"},
     "lexique": [{"mot": "broyeur Alsing", "def": "grand tambour qui tourne et broie les matières premières avec l'eau"},
                 {"mot": "délayage", "def": "on remue doucement et longtemps la barbotine pour qu'elle reste bien mélangée"},
                 {"mot": "tamis à secousses", "def": "il retient les grumeaux et les grains trop gros"}],
     "frise": [{"date": "1", "evt": "pesée"}, {"date": "2", "evt": "ajout de l'eau"}, {"date": "3", "evt": "broyage Alsing"}, {"date": "4", "evt": "tamisage"}, {"date": "5", "evt": "délayage"}],
     "frise_titre": "Les cinq étapes communes",
     "sources": COURS + ", partie II."},
    {"id": "trois-produits", "salle": 3, "icone": "III", "titre": "Les trois produits de la voie humide", "duree": "4 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Citer les trois produits et leur usage", "Dire ce qui change après les étapes communes", "Ordonner les étapes des pâtes plastiques"],
     "contenu": {
         "cm1": "<ul><li><b>Pâtes plastiques</b> : pâte ferme et malléable, pour modeler et tourner. 8 étapes : on retire l'eau (filtre-presse), l'air (boudineuse-désaéreuse), puis la pâte sort en boudin.</li><li><b>Barbotine de coulage</b> : liquide bien fluide, pour remplir les moules. 6 étapes.</li><li><b>Poudres atomisées</b> : petits granules secs, pour le pressage industriel. 10 étapes.</li></ul>",
         "cm2": "<p>Après les étapes communes, le procédé change selon le produit.</p><ul><li><b>Pâtes plastiques</b> (pâte ferme et malléable, pour modeler et tourner), <b>8 étapes</b> : après le délayage, la <b>filtration</b> au filtre-presse (sous pression, l'eau traverse les toiles et la terre reste), la <b>désaération</b> dans la boudineuse-désaéreuse (on malaxe et on enlève les bulles d'air), puis l'<b>extrusion</b> par une tête d'extrusion, souvent en colombin.</li><li><b>Barbotine de coulage</b> (liquide bien fluide, pour le coulage en moule), <b>6 étapes</b> : avec du défloculant, puis transfert vers les moules sur le banc de coulage.</li><li><b>Poudres atomisées</b> (petits granules secs, pour le pressage industriel), <b>10 étapes</b> : transfert, pulvérisation, séchage, granules, stockage.</li></ul><div class='encadre'>Je veux remplir des moules : barbotine. Modeler ou tourner : pâte plastique. Presser avec une machine : poudre atomisée.</div>"},
     "lexique": [{"mot": "filtre-presse", "def": "machine qui presse la barbotine entre des toiles pour retirer l'eau"},
                 {"mot": "boudineuse-désaéreuse", "def": "machine qui malaxe la pâte, enlève l'air et la fait sortir en boudin"},
                 {"mot": "extrusion", "def": "action de faire sortir la pâte par une ouverture pour former un boudin"},
                 {"mot": "banc de coulage", "def": "poste où l'on place les moules pour les remplir de barbotine"}],
     "frise": [{"date": "plastiques", "evt": "filtration, désaération, extrusion (8 étapes)"}, {"date": "coulage", "evt": "transfert vers les moules (6 étapes)"}, {"date": "poudres", "evt": "transfert, pulvérisation, séchage, granules, stockage (10 étapes)"}],
     "frise_titre": "Après les étapes communes",
     "sources": COURS + ", partie II."},
    {"id": "atomisation-machines", "salle": 4, "icone": "IV", "titre": "L'atomiseur, les machines du hall, les entreprises", "duree": "3 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Expliquer l'atomisation étape par étape", "Reconnaître les équipements du hall", "Comprendre qu'une entreprise choisit ses produits"],
     "contenu": {
         "cm1": "<h4>L'atomisation</h4><p>On sèche très vite la barbotine pour obtenir une poudre. Après les étapes communes : <b>transfert</b> par une pompe vers l'<b>atomiseur</b>, <b>pulvérisation</b> en gouttelettes, <b>séchage</b> par de l'air chaud, <b>granules</b>, <b>stockage</b> dans un silo.</p><h4>Les machines</h4><p>Filtre-presse, pompe, banc de coulage, atomiseur, silo.</p><div class='encadre'>Une entreprise peut ne faire qu'un seul produit, ou deux, ou trois.</div>",
         "cm2": "<h4>Les poudres atomisées en 10 étapes</h4><p>Après le délayage (étape 5) :</p><ol start='6'><li><b>Transfert</b> : une pompe envoie la barbotine vers l'atomiseur.</li><li><b>Pulvérisation</b> : une tête centrifuge, qui tourne très vite, la pulvérise en petites gouttelettes.</li><li><b>Séchage</b> : un courant d'air chaud, environ <b>400 °C</b>, sèche les gouttelettes dans l'atomiseur.</li><li><b>Granules</b> : l'eau s'évapore très vite, il reste de petits grains solides.</li><li><b>Stockage</b> : la poudre sèche est évacuée vers un <b>silo</b>.</li></ol><h4>Les équipements du hall</h4><p>Le <b>banc de coulage</b> remplit les moules ; le <b>filtre-presse</b> retire l'eau ; la <b>pompe</b> envoie la barbotine d'une machine à l'autre ; l'<b>atomiseur</b> est la grande tour de séchage ; le <b>silo</b> stocke la poudre.</p><div class='encadre'>Les procédés du cours sont des exemples : une entreprise peut ne fabriquer qu'un seul de ces produits, ou deux, ou trois. Elle n'utilise que les équipements utiles.</div>"},
     "lexique": [{"mot": "atomiseur", "def": "grande tour qui sèche la barbotine pulvérisée en fines gouttelettes avec de l'air chaud"},
                 {"mot": "granules", "def": "petits grains solides qui restent quand l'eau s'évapore"},
                 {"mot": "silo", "def": "réservoir où la poudre sèche est stockée"}],
     "frise": [{"date": "6", "evt": "transfert vers l'atomiseur"}, {"date": "7", "evt": "pulvérisation"}, {"date": "8", "evt": "séchage (≈ 400 °C)"}, {"date": "9", "evt": "granules"}, {"date": "10", "evt": "stockage (silo)"}],
     "frise_titre": "Les étapes de l'atomisation",
     "document": {"type": "text", "titre": "Extrait du cours", "contenu": "Une entreprise peut ne faire qu'un seul de ces produits, ou deux, ou trois.", "source": COURS + ", synthèse."},
     "sources": COURS + ", partie II (3. Les poudres atomisées) et synthèse."},
    {"id": "voie-seche-securite", "salle": 5, "icone": "V", "titre": "La voie sèche et la sécurité", "duree": "3 min", "niveau": "Essentiel · Expert",
     "objectifs": ["Citer dans l'ordre les cinq étapes de la voie sèche", "Comparer voie humide et voie sèche", "Adopter les bons gestes avec les poudres"],
     "contenu": {
         "cm1": "<h4>Cinq étapes</h4><ol><li><b>Concassage</b> : on casse les gros blocs.</li><li><b>Mouillage</b> : on humidifie l'argile.</li><li><b>Mélange</b> de l'argile et de l'eau.</li><li><b>Désaération</b> : la boudineuse enlève l'air.</li><li><b>Extrusion</b> : la pâte sort en boudins.</li></ol><div class='encadre'>Les poudres sont fines et volatiles : masque, gestes lents, on évite de les respirer.</div>",
         "cm2": "<h4>La voie sèche : un seul produit</h4><p>On part d'argile sèche, on ajoute l'eau peu à peu, puis on extrude des pains de terre.</p><ol><li><b>Concassage</b> (concasseur) : on casse les gros blocs en petits morceaux, le mélange sera plus homogène.</li><li><b>Mouillage</b> : on humidifie l'argile, l'eau doit être bien répartie.</li><li><b>Mélange</b> : on mélange longuement l'argile et l'eau pour obtenir une pâte homogène.</li><li><b>Désaération</b> : la boudineuse-désaéreuse forme des boudins et enlève l'air. Sans bulles d'air, on évite les défauts à la cuisson.</li><li><b>Extrusion</b> : la pâte sort en boudins, que l'on peut façonner, couper, et transformer en objets.</li></ol><h4>Voie humide ou voie sèche ?</h4><p>Machines de la voie humide : broyeur Alsing, tamis, délayeur, filtre-presse, boudineuse-désaéreuse, atomiseur. Voie sèche : concasseur, mélangeur, boudineuse-désaéreuse. La boudineuse-désaéreuse sert dans les deux méthodes.</p><div class='encadre'>Les matières premières en poudre sont fines et volatiles : on les pèse avec précision, avec précaution.</div>"},
     "lexique": [{"mot": "concassage", "def": "on casse les gros blocs d'argile en morceaux plus petits"},
                 {"mot": "mouillage", "def": "on humidifie l'argile : l'eau doit être bien répartie"},
                 {"mot": "extrusion", "def": "la pâte sort par une ouverture, en boudins"}],
     "frise": [{"date": "1", "evt": "concassage"}, {"date": "2", "evt": "mouillage"}, {"date": "3", "evt": "mélange"}, {"date": "4", "evt": "désaération"}, {"date": "5", "evt": "extrusion"}],
     "frise_titre": "Les cinq étapes de la voie sèche",
     "document": {"type": "text", "titre": "Extrait du cours", "contenu": "La voie sèche part d'argile sèche. On ajoute peu à peu de l'eau pour obtenir une pâte façonnable, puis on extrude des pains de terre.", "source": COURS + ", partie III."},
     "sources": COURS + ", partie III et synthèse."}
]}


# ---- Compléments Expert (texte fidèle au cours) ----
PLUS = {
    "deux-methodes": "<h4>Pourquoi préparer ?</h4><p>Une argile brute ne se travaille pas telle quelle. Il faut limiter les fissures et les déformations avec des dégraissants, retirer les impuretés, trouver la bonne humidité et obtenir une pâte identique partout : sans grumeaux, elle se comportera de la même façon à chaque geste. La méthode choisie dépend du produit voulu : la voie humide part d'un liquide et permet trois produits, la voie sèche part de blocs et donne des pains de terre.</p>",
    "etapes-communes": "<h4>Pourquoi ces cinq étapes ?</h4><p>La pesée fixe la recette. L'eau transforme les poudres en barbotine. Le broyage rend les grains très fins, le tamisage retire ce qui est trop gros, et le délayage garde la barbotine bien mélangée. Une pompe déplace la barbotine d'une machine à l'autre, par exemple vers le tamis. Pour la barbotine de coulage, le défloculant la rend très fluide sans ajouter d'eau, afin qu'elle remplisse bien les moules.</p>",
    "trois-produits": "<h4>Trois procédés côte à côte</h4><p>Les cinq premières étapes sont les mêmes ; seule la suite change. Pour la pâte plastique, on doit enlever l'eau (filtre-presse), puis l'air (boudineuse-désaéreuse), avant de former le boudin. Pour le coulage, la barbotine reste liquide : une pompe l'envoie dans des tuyaux jusqu'aux moules du banc de coulage. Pour les poudres, on sèche très vite la barbotine pour obtenir de petits grains que l'on stocke.</p>",
    "atomisation-machines": "<h4>Une usine est un exemple</h4><p>Dans la réalité, une entreprise peut ne fabriquer qu'un seul produit, ou deux, ou trois. Elle choisit ses produits et ses équipements : pas d'atomiseur si elle ne fait que de la barbotine de coulage, pas de banc de coulage si elle ne fait que des poudres. En revanche, toutes celles qui travaillent par voie humide commencent par peser, ajouter de l'eau, broyer, tamiser et délayer.</p>",
    "voie-seche-securite": "<h4>Pourquoi concasser, mouiller, mélanger ?</h4><p>Casser les gros blocs permet un mélange plus homogène. Humidifier l'argile avec une eau bien répartie évite les zones trop sèches. Un long mélange donne une pâte homogène, puis la boudineuse-désaéreuse enlève l'air : sans bulles d'air, on évite les défauts à la cuisson. Les boudins peuvent alors être façonnés, coupés, et transformés en objets en céramique.</p>",
}
for l in LECONS["lecons"]:
    l["contenu"]["cm2"] += PLUS[l["id"]]

# =====================================================================================
# ÉVALUATIONS
# =====================================================================================
def q(t, o, b, pts=None):
    d = {"q": t, "options": o, "bonne": b}
    if pts:
        d["pts"] = pts
    return d


EVAL = {
    "metadata": {"sujet": "La préparation des pâtes céramiques", "niveaux": ["Essentiel", "Expert"],
                 "programme": "CAP Décoration sur céramique — technologie des matériaux : la préparation des pâtes céramiques.", "sources": COURS},
    "quizz_final": {
        "CM1": [q("La barbotine est un mélange liquide…", ["d'argile et d'eau", "de verre et de sable", "d'émail et de colle"], 0),
                q("Par voie sèche, on part…", ["d'une barbotine", "de blocs d'argile sèche", "de granules"], 1),
                q("Quelle machine broie les matières avec l'eau ?", ["le broyeur Alsing", "le silo", "le tamis"], 0),
                q("Quel produit sert à remplir des moules ?", ["la poudre atomisée", "la pâte plastique", "la barbotine de coulage"], 2),
                q("Quelle machine enlève l'air de la pâte ?", ["la boudineuse-désaéreuse", "l'atomiseur", "le filtre-presse"], 0)],
        "CM2": [q("Que fait le défloculant ?", ["il rend la barbotine plus fluide sans ajouter d'eau", "il sèche la barbotine", "il filtre la barbotine"], 0),
                q("Combien d'étapes pour les poudres atomisées ?", ["6", "8", "10"], 2),
                q("Que fait le filtre-presse ?", ["il enlève l'air", "il presse la barbotine pour retirer l'eau", "il sèche les gouttelettes"], 1),
                q("Quelle machine sert dans les deux méthodes ?", ["le concasseur", "la boudineuse-désaéreuse", "l'atomiseur"], 1),
                q("Une entreprise par voie humide doit-elle fabriquer les trois produits ?", ["oui, toujours", "non, un, deux ou trois", "oui, mais seulement par voie sèche"], 1)]},
    "qcm": {
        "CM1": [q("Les étapes 1 à 5 de la voie humide…", ["se ressemblent", "sont toutes différentes", "n'existent pas"], 0, 1),
                q("Après le délayage, la barbotine de coulage…", ["est séchée", "est envoyée vers les moules", "est concassée"], 1, 1),
                q("Où stocke-t-on la poudre sèche ?", ["dans un silo", "dans un délayeur", "dans un tamis"], 0, 1),
                q("Le tamis à secousses retient…", ["l'eau", "les grumeaux et les grains trop gros", "l'air"], 1, 1),
                q("Quel produit sert à modeler et à tourner ?", ["la pâte plastique", "la barbotine", "la poudre atomisée"], 0, 1),
                q("Par voie sèche, la première étape est…", ["le concassage", "le séchage", "la pesée de l'eau"], 0, 1),
                q("L'atomiseur est…", ["une tour qui sèche des gouttelettes", "un poste de moulage", "un broyeur"], 0, 1),
                q("Combien d'étapes pour les pâtes plastiques ?", ["8", "3", "20"], 0, 1),
                q("La boudineuse fait sortir la pâte…", ["en boudin", "en granules", "en liquide"], 0, 1),
                q("Une pâte homogène est…", ["la même partout", "pleine de grumeaux", "très sèche"], 0, 1)],
        "CM2": [q("Quelle est la température de l'air chaud dans l'atomiseur ?", ["environ 400 °C", "environ 40 °C", "environ 4000 °C"], 0, 1),
                q("Que produit la pulvérisation ?", ["de petites gouttelettes", "des boudins", "des blocs"], 0, 1),
                q("Qu'est-ce qu'un colombin ?", ["un boudin de pâte", "une poudre", "un moule"], 0, 1),
                q("Par voie sèche, l'eau est…", ["ajoutée peu à peu", "ajoutée en grande quantité d'un coup", "retirée au filtre-presse"], 0, 1),
                q("Pourquoi désaérer la pâte ?", ["pour éviter les défauts à la cuisson", "pour la rendre liquide", "pour la colorer"], 0, 1),
                q("Quel équipement envoie la barbotine d'une machine à l'autre ?", ["la pompe", "le silo", "le concasseur"], 0, 1),
                q("Les poudres de matières premières sont…", ["fines et volatiles", "lourdes et collantes", "liquides"], 0, 1),
                q("Combien d'étapes pour la barbotine de coulage ?", ["6", "8", "10"], 0, 1),
                q("Le banc de coulage sert à…", ["remplir les moules de barbotine", "sécher les granules", "casser les blocs"], 0, 1),
                q("Quelles machines servent en voie sèche ?", ["concasseur, mélangeur, boudineuse-désaéreuse", "Alsing, tamis, atomiseur", "filtre-presse, silo, pompe"], 0, 1),
                q("Que retient le tamis à secousses ?", ["les grumeaux et les grains trop gros", "l'air de la pâte", "le défloculant"], 0, 1),
                q("Que se passe-t-il quand l'eau s'évapore très vite dans l'atomiseur ?", ["il reste de petits grains, les granules", "la barbotine devient plus fluide", "la pâte devient ferme"], 0, 1)]},
    "questions_fermees": {
        "CM1": [{"q": "La barbotine est un mélange d'argile et d'eau.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Par voie humide, on part de blocs d'argile sèche.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Le filtre-presse retire l'eau de la barbotine.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Le silo sert à sécher la barbotine.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Cite les cinq étapes communes de la voie humide.", "type": "court", "rep": "pesée, ajout de l'eau, broyage, tamisage, délayage", "pts": 2},
                {"q": "Cite les trois produits de la voie humide.", "type": "court", "rep": "pâtes plastiques, barbotine de coulage, poudres atomisées", "pts": 1},
                {"q": "Cite une machine de la voie sèche.", "type": "court", "rep": "concasseur, mélangeur ou boudineuse-désaéreuse", "pts": 1},
                {"q": "Que fait la boudineuse-désaéreuse ?", "type": "court", "rep": "elle enlève l'air de la pâte et la fait sortir en boudin", "pts": 1}],
        "CM2": [{"q": "Le défloculant rend la barbotine plus épaisse.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Une entreprise peut ne fabriquer qu'un seul produit par voie humide.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Par voie sèche, on ajoute l'eau peu à peu.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Dans l'atomiseur, l'air chaud est à environ 40 °C.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Décris, dans l'ordre, les étapes de la barbotine de coulage.", "type": "court", "rep": "pesée, ajout de l'eau et du défloculant, broyage Alsing, tamisage, délayage, transfert vers les moules", "pts": 2},
                {"q": "Décris les trois dernières étapes des pâtes plastiques.", "type": "court", "rep": "filtration (filtre-presse), désaération (boudineuse-désaéreuse), extrusion", "pts": 2},
                {"q": "Quelle est la différence entre voie humide et voie sèche ?", "type": "court", "rep": "voie humide : on part d'une barbotine (beaucoup d'eau) ; voie sèche : on part de blocs d'argile sèche et on ajoute l'eau peu à peu", "pts": 2},
                {"q": "Pourquoi une entreprise n'utilise-t-elle pas toutes les machines ?", "type": "court", "rep": "elle choisit ses produits et n'utilise que les équipements utiles à ses produits", "pts": 1}]},
    "etudes_documents": {
        "CM1": [{"titre": "Le procédé de la barbotine de coulage", "document": {"contenu": "Pesée (avec défloculant) → Ajout de l'eau → Broyage Alsing → Tamisage → Délayage → Transfert vers les moules.", "source": COURS + ", partie II."},
                 "questions": [{"q": "Combien d'étapes ?", "type": "court", "rep": "6", "pts": 1},
                               {"q": "Quelle est la dernière étape ?", "type": "court", "rep": "le transfert vers les moules", "pts": 1},
                               {"q": "Quelle machine broie les matières ?", "type": "court", "rep": "le broyeur Alsing", "pts": 1}]},
                {"titre": "La voie sèche", "document": {"contenu": "Concassage → Mouillage → Mélange → Désaération (boudineuse-désaéreuse) → Extrusion.", "source": COURS + ", partie III."},
                 "questions": [{"q": "Par quelle étape commence-t-on ?", "type": "court", "rep": "le concassage", "pts": 1},
                               {"q": "Quelle machine enlève l'air ?", "type": "court", "rep": "la boudineuse-désaéreuse", "pts": 1}]}],
        "CM2": [{"titre": "Les poudres atomisées", "document": {"contenu": "Pesée → Eau → Broyage → Tamisage → Délayage → Transfert → Pulvérisation (tête centrifuge) → Séchage (air chaud, environ 400 °C) → Granules → Stockage (silo).", "source": COURS + ", partie II."},
                 "questions": [{"q": "Combien d'étapes comporte ce procédé ?", "type": "court", "rep": "10", "pts": 1},
                               {"q": "Quelles sont les étapes communes à tous les produits de la voie humide ?", "type": "court", "rep": "les cinq premières : pesée, eau, broyage, tamisage, délayage", "pts": 2},
                               {"q": "Explique le rôle de la tête centrifuge et de l'air chaud.", "type": "court", "rep": "la tête centrifuge pulvérise la barbotine en gouttelettes ; l'air chaud (environ 400 °C) les sèche", "pts": 2}]},
                {"titre": "Les deux méthodes", "document": {"contenu": "Voie humide : on part de poudres mélangées à beaucoup d'eau (barbotine) ; machines : broyeur Alsing, tamis, délayeur, filtre-presse, boudineuse-désaéreuse, atomiseur. Voie sèche : on part de blocs d'argile sèche ; machines : concasseur, mélangeur, boudineuse-désaéreuse.", "source": COURS + ", synthèse."},
                 "questions": [{"q": "Quelle machine est utilisée dans les deux méthodes ?", "type": "court", "rep": "la boudineuse-désaéreuse", "pts": 1},
                               {"q": "Pourquoi un atomiseur est-il inutile en voie sèche ?", "type": "court", "rep": "il sèche une barbotine, qu'on n'obtient pas en voie sèche", "pts": 1}]}]},
    "fiches_preparatoires": [
        {"salle": i + 1, "titre": f"{TITRES[i]} — {SOUS[i]}", "objectifs": LECONS["lecons"][i]["objectifs"],
         "vocabulaire": LECONS["lecons"][i]["lexique"][:4], "contexte": DESCR[i]} for i in range(5)]
}

# =====================================================================================
# LEÇONS A4 (schémas dessinés par script, jamais par IA)
# =====================================================================================
def svg_chaine(titre, etapes, couleur="#0F4C81"):
    """Schéma en chaîne : une case par étape, flèches entre les cases (dessiné par script)."""
    n = len(etapes)
    larg = 380
    cw = (larg - 20 - (n - 1) * 14) / n
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {larg} 130" role="img" aria-label="{titre}" font-family="Segoe UI, Helvetica, Arial, sans-serif">',
         f'<rect width="{larg}" height="130" fill="#f3f8fd"/>',
         f'<text x="{larg/2}" y="20" font-size="12" font-weight="bold" text-anchor="middle" fill="#0b2a4a">{titre}</text>']
    for k, (nom, mach) in enumerate(etapes):
        x = 10 + k * (cw + 14)
        s.append(f'<rect x="{x:.1f}" y="40" width="{cw:.1f}" height="60" rx="6" fill="#ffffff" stroke="{couleur}" stroke-width="2"/>'
                 f'<text x="{x + cw/2:.1f}" y="58" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#0b2a4a">{k+1}. {nom}</text>'
                 f'<text x="{x + cw/2:.1f}" y="76" font-size="7" text-anchor="middle" fill="{couleur}">{mach}</text>')
        if k < n - 1:
            s.append(f'<path d="M{x + cw + 2:.1f} 70 l10 0 m-4 -4 l4 4 l-4 4" fill="none" stroke="#C2410C" stroke-width="2"/>')
    s.append('</svg>')
    return "".join(s)


def svg_trois_produits():
    lignes = [("Pâtes plastiques", "filtration, désaération, extrusion", 8), ("Barbotine de coulage", "transfert vers les moules", 6),
              ("Poudres atomisées", "transfert, pulvérisation, séchage, granules, stockage", 10)]
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 190" role="img" aria-label="Les trois produits de la voie humide" font-family="Segoe UI, Helvetica, Arial, sans-serif">',
         '<rect width="380" height="190" fill="#f3f8fd"/>',
         '<rect x="10" y="12" width="360" height="26" rx="5" fill="#9fb0c0"/><text x="190" y="29" font-size="11" font-weight="bold" text-anchor="middle" fill="#0b2a4a">Étapes communes : pesée, eau, broyage, tamisage, délayage</text>']
    for k, (n, d, nb) in enumerate(lignes):
        y = 54 + k * 44
        s.append(f'<path d="M30 {y-14} l0 8 m-4 -4 l4 4 l4 -4" fill="none" stroke="#C2410C" stroke-width="2"/>'
                 f'<rect x="10" y="{y}" width="360" height="34" rx="5" fill="#ffffff" stroke="#0F4C81" stroke-width="2"/>'
                 f'<text x="20" y="{y+15}" font-size="11" font-weight="bold" fill="#0b2a4a">{n} ({nb} étapes)</text>'
                 f'<text x="20" y="{y+28}" font-size="9" fill="#0F4C81">{d}</text>')
    s.append('</svg>')
    return "".join(s)


A4 = {"_commentaire": "Généré par outils/generer-preparation-pates.py — ne pas modifier à la main.",
      "jeu": {"titre": TITRE, "matiere": "Technologie céramique", "theme": "La préparation des pâtes céramiques", "couleur": "#0F4C81", "accent": "#C2410C", "couleur_pale": "#DCEEFF", "accent_pale": "#FFE9DB"},
      "lecons": {
          "deux-methodes": {"competence": "Expliquer ce qu'est préparer une pâte et distinguer voie humide et voie sèche.", "visuels": []},
          "etapes-communes": {"competence": "Citer dans l'ordre les cinq étapes communes et leurs machines.",
                              "visuels": [{"type": "svg", "titre": "Les cinq étapes communes", "legende": "De la poudre à la barbotine.",
                                           "svg": svg_chaine("Les étapes communes de la voie humide", [("Pesée", "balance"), ("Eau", "barbotine"), ("Broyage", "Alsing"), ("Tamisage", "tamis"), ("Délayage", "délayeur")]),
                                           "etiquette": "Schéma", "source": COURS + ", partie II."}]},
          "trois-produits": {"competence": "Citer les trois produits de la voie humide, leur procédé et leur usage.",
                             "visuels": [{"type": "svg", "titre": "Les trois produits", "legende": "Après les étapes communes, le procédé change.", "svg": svg_trois_produits(),
                                          "etiquette": "Schéma", "source": COURS + ", partie II."}]},
          "atomisation-machines": {"competence": "Expliquer l'atomisation ; reconnaître les équipements du hall.",
                                   "visuels": [{"type": "svg", "titre": "L'atomisation", "legende": "Des gouttelettes aux granules.",
                                                "svg": svg_chaine("Les dernières étapes des poudres atomisées", [("Transfert", "pompe"), ("Pulvérisation", "tête centrifuge"), ("Séchage", "air chaud"), ("Granules", "grains secs"), ("Stockage", "silo")]),
                                                "etiquette": "Schéma", "source": COURS + ", partie II."}]},
          "voie-seche-securite": {"competence": "Citer dans l'ordre les étapes de la voie sèche ; adopter les bons gestes avec les poudres.",
                                  "visuels": [{"type": "svg", "titre": "La voie sèche", "legende": "De l'argile sèche aux pains de terre.",
                                               "svg": svg_chaine("La voie sèche", [("Concassage", "concasseur"), ("Mouillage", "eau"), ("Mélange", "mélangeur"), ("Désaération", "boudineuse"), ("Extrusion", "boudin")]),
                                               "etiquette": "Schéma", "source": COURS + ", partie III."}]}}}

if __name__ == "__main__":
    ecrire("enigmes.json", ENIGMES)
    ecrire("dialogues.json", DIALOGUES)
    ecrire("lecons.json", LECONS)
    ecrire("evaluations.json", EVAL)
    ecrire("lecons-a4.json", A4)
    n1 = sum(1 for s in ENIGMES["salles"] for e in s["enigmes"] if "niveaux" not in e)
    n2 = sum(len(s["enigmes"]) for s in ENIGMES["salles"])
    print(f"✔ {TITRE} : {n1} énigmes Essentiel, {n2} énigmes Expert, 5 leçons, évaluations écrites dans {os.path.relpath(DATA)}")
