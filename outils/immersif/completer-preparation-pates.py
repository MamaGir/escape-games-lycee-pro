#!/usr/bin/env python3
"""Complète les brouillons de la variante immersive « Panne à l'usine » après migrer-jeu.py.

    python outils/immersif/completer-preparation-pates.py <dossier de la variante>   (ex. immersifs/preparation-pates)

Écrit : décors dessinés de secours (js/decors-secours.js, 16:9, dessinés par script — aucune image IA),
zones cliquables nommées (decors-fx.json), et pour chaque énigme : personnage émetteur, problème narratif, enjeu,
raison du savoir ici, réaction du décor, réplique du personnage pour chaque grade ; puis les réglages propres au lycée
(libellés Essentiel / Expert, plaques bleues, jauge « Pression »).
Relancer ensuite : python <variante>/outils/embarquer-donnees.py et node <variante>/tests/test-immersif.js
"""
import json, os, re, sys

DEST = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "immersifs/preparation-pates")
DATA = os.path.join(DEST, "assets", "data")
DECORS = ["laboratoire", "broyage", "hall", "atomisation", "voie-seche"]
PERSO = ["karim", "elodie", "hugo", "sofiane", "samia"]

# ------------------------------------------------------------------------------------------------
# Décors dessinés (800 × 450). Chaque objet cliquable (zone) est dessiné à l'endroit de sa zone.
# ------------------------------------------------------------------------------------------------
def R(x, y, w, h, f, s=None, rx=0, sw=2, op=None):
    a = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}"'
    if s:
        a += f' stroke="{s}" stroke-width="{sw}"'
    if op:
        a += f' opacity="{op}"'
    return a + "/>"


def C(cx, cy, rx, ry, f, s=None, sw=2):
    a = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{f}"'
    if s:
        a += f' stroke="{s}" stroke-width="{sw}"'
    return a + "/>"


def T(x, y, t, size=12, f="#0b2a4a", w="bold", anc="middle"):
    return f'<text x="{x}" y="{y}" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="{size}" font-weight="{w}" text-anchor="{anc}" fill="{f}">{t}</text>'


def L(x1, y1, x2, y2, s="#0b2a4a", sw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{s}" stroke-width="{sw}" stroke-linecap="round"/>'


def PG(pts, f, s=None, sw=2):
    a = f'<polygon points="{pts}" fill="{f}"'
    if s:
        a += f' stroke="{s}" stroke-width="{sw}"'
    return a + "/>"


def G(dy, items):
    """Décale un groupe d'objets vers le bas (le bandeau du jeu cache le haut de l'image)."""
    return '<g transform="translate(0,%d)">' % dy + "".join(items) + "</g>"


def fond(mur, sol, y_sol=330, bande="#cfd9e2"):
    """Mur, bande de plinthe, sol, néons du plafond."""
    return [R(0, 0, 800, y_sol, mur), R(0, y_sol - 14, 800, 14, bande), R(0, y_sol, 800, 450 - y_sol, sol),
            R(0, y_sol, 800, 3, "#8fa0b0"),
            R(70, 14, 190, 10, "#ffffff", "#c9d6e0", 3, 1), R(300, 14, 190, 10, "#ffffff", "#c9d6e0", 3, 1), R(540, 14, 190, 10, "#ffffff", "#c9d6e0", 3, 1)]


def decor_laboratoire():
    o = fond("#e9f2f8", "#c9d6e0", 340)
    # 1 — tableau des mots (mur gauche)
    o += [R(40, 70, 260, 130, "#ffffff", "#0F4C81", 4, 4), T(170, 96, "Mots du métier", 14, "#0F4C81")]
    for k, mot in enumerate(["Barbotine", "Défloculant", "Filtre-presse", "Atomiseur"]):
        o += [R(56 + (k % 2) * 124, 110 + (k // 2) * 40, 112, 28, "#DCEEFF", "#7FA9CF", 4, 1), T(112 + (k % 2) * 124, 129 + (k // 2) * 40, mot, 11)]
    # 2 — panneau « Préparer une pâte, c'est… »
    o += [R(340, 80, 140, 130, "#fff7ec", "#C2410C", 4, 3), T(410, 102, "Préparer une pâte", 11, "#C2410C")]
    for k in range(4):
        o += [R(354, 114 + k * 22, 112, 14, "#ffe9db", None, 3), L(358, 121 + k * 22, 440, 121 + k * 22, "#C2410C", 1)]
    # 4 — fiche des deux méthodes épinglée
    o += [R(660, 90, 100, 120, "#ffffff", "#0b2a4a", 2, 2), C(710, 96, 4, 4, "#C2410C"), T(710, 122, "Deux méthodes", 10, "#0F4C81")]
    for k in range(5):
        o += [L(672, 138 + k * 14, 748, 138 + k * 14, "#9fb0c0", 1)]
    # paillasse, balance, carnet, sacs
    o += [R(20, 300, 760, 40, "#e6edf3", "#7FA9CF", 3, 3), R(30, 340, 14, 70, "#9aaab8"), R(756, 340, 14, 70, "#9aaab8"),
          R(340, 340, 120, 70, "#b8c6d3", "#7FA9CF", 3, 2)]
    o += [R(110, 276, 100, 24, "#9aaab8", None, 3), R(130, 252, 60, 26, "#f3f8fd", "#0b2a4a", 3, 2), T(160, 270, "0,00 kg", 10)]  # balance
    o += [R(560, 282, 70, 18, "#ffffff", "#0F4C81", 2, 2), L(572, 288, 620, 288, "#7FA9CF", 1), L(572, 294, 610, 294, "#7FA9CF", 1)]  # carnet de Karim
    o += [R(250, 270, 56, 30, "#d8c3a5", "#8a6d43", 3, 2), R(660, 262, 56, 38, "#d8c3a5", "#8a6d43", 3, 2), R(716, 272, 44, 28, "#e0cfb6", "#8a6d43", 3, 2)]  # sacs
    o += [C(400, 300, 22, 6, "#c9d6e0")]
    return o


def decor_broyage():
    o = fond("#dfe7ee", "#b9c5d0", 340)
    # 1 — écran mural de la recette
    ecran = [R(300, 50, 200, 110, "#0b2540", "#9fb0c0", 6, 4), T(400, 76, "RECETTE", 13, "#9FD3FF")]
    for k in range(4):
        ecran += [R(318, 90 + k * 17, 164, 11, "#1F4A75", None, 3), L(324, 96 + k * 17, 330 + (k * 23) % 90 + 40, 96 + k * 17, "#BFE3FF", 2)]
    o += [G(24, ecran)]
    # 2 — panneau des plaques (une plaque est tombée de travers)
    pan = [R(40, 60, 230, 120, "#ffffff", "#0F4C81", 4, 3), T(155, 80, "Plaques des machines", 11, "#0F4C81")]
    for k in range(3):
        pan += [R(52 + k * 72, 92, 62, 30, "#e3e9ef", "#7a8896", 3, 2), L(58 + k * 72, 102, 100 + k * 72, 102, "#9fb0c0", 2), L(58 + k * 72, 112, 88 + k * 72, 112, "#9fb0c0", 2)]
    pan += ['<g transform="rotate(-14 160 156)">' + R(128, 140, 62, 30, "#e3e9ef", "#7a8896", 3, 2) + L(134, 150, 176, 150, "#9fb0c0", 2) + L(134, 160, 164, 160, "#9fb0c0", 2) + '</g>']
    o += [G(24, pan)]
    # broyeur Alsing : grand tambour couché
    o += [R(50, 270, 70, 20, "#7a8896"), R(190, 270, 70, 20, "#7a8896"), R(40, 204, 240, 72, "#8fa2b6", "#4b5b6b", 34, 4),
          L(70, 214, 70, 268, "#b9c8d8", 3), L(130, 210, 130, 272, "#b9c8d8", 3), L(190, 210, 190, 272, "#b9c8d8", 3), L(250, 214, 250, 268, "#b9c8d8", 3),
          T(160, 250, "ALSING", 14, "#2b3a4a")]
    # pompe et tuyaux
    o += [R(300, 296, 56, 38, "#2f75b5", "#0F4C81", 6, 3), C(328, 315, 11, 11, "#9FD3FF", "#0F4C81"), L(280, 315, 300, 315, "#5a6b7b", 6), L(356, 315, 430, 270, "#5a6b7b", 6)]
    # 3 — tamis à secousses sur châssis + délayeur (cuve)
    o += [R(420, 214, 110, 14, "#9aaab8"), L(432, 228, 428, 310, "#5a6b7b", 4), L(518, 228, 522, 310, "#5a6b7b", 4),
          PG("414,214 536,214 520,184 430,184", "#c7d3de", "#4b5b6b", 3), L(430, 198, 520, 198, "#7a8896", 2),
          R(570, 160, 100, 150, "#cfdbe6", "#4b5b6b", 8, 4), R(576, 218, 88, 86, "#d9c7a8", None, 6), L(620, 130, 620, 210, "#4b5b6b", 5),
          R(606, 122, 28, 14, "#e6743c", None, 3), L(598, 258, 642, 258, "#8a6d43", 3)]
    # 4 — armoire à cadenas
    o += [R(718, 150, 66, 190, "#b9c5d0", "#4b5b6b", 4, 3), L(751, 150, 751, 340, "#4b5b6b", 2), C(738, 250, 5, 5, "#f3f8fd"), C(764, 250, 5, 5, "#f3f8fd"),
          R(735, 264, 32, 26, "#e6a23c", "#8a5a10", 4, 2), f'<path d="M740 264 v-10 a11 11 0 0 1 22 0 v10" fill="none" stroke="#8a5a10" stroke-width="3"/>']
    return o


def decor_hall():
    o = fond("#e3eaf1", "#c3ced8", 340)
    # 2 — panneau des commandes clients
    o += [R(30, 70, 150, 130, "#fff7ec", "#C2410C", 4, 3), T(105, 92, "Commandes", 12, "#C2410C")]
    for k in range(3):
        o += [R(44 + k * 44, 106, 38, 84, "#ffffff", "#e6a23c", 2, 2), L(50 + k * 44, 120, 76 + k * 44, 120, "#9fb0c0", 1), L(50 + k * 44, 132, 72 + k * 44, 132, "#9fb0c0", 1), L(50 + k * 44, 144, 70 + k * 44, 144, "#9fb0c0", 1)]
    # 3 — filtre-presse (empilement de plaques) + boudineuse
    o += [R(400, 226, 230, 14, "#5a6b7b"), R(400, 160, 18, 84, "#4b5b6b"), R(612, 160, 18, 84, "#4b5b6b")]
    for k in range(9):
        o += [R(424 + k * 20, 168, 14, 62, "#9fb8d0", "#4b5b6b", 2, 2)]
    o += [R(420, 262, 190, 30, "#c7d3de", "#4b5b6b", 8, 3), L(420, 277, 400, 277, "#4b5b6b", 4), R(372, 269, 30, 16, "#d9c7a8", None, 4), R(610, 252, 36, 44, "#8fa2b6", "#4b5b6b", 4, 2)]
    # 1 — trois chariots
    for k, (nom, c) in enumerate([("Pâtes plastiques", "#d9c7a8"), ("Coulage", "#e6edf3"), ("Poudres", "#f1e7c8")]):
        x = 20 + k * 125
        o += [R(x, 284, 108, 38, "#5a6b7b", "#2b3a4a", 4, 3), R(x + 8, 264, 92, 22, c, "#4b5b6b", 3, 2), C(x + 20, 332, 9, 9, "#2b3a4a"), C(x + 88, 332, 9, 9, "#2b3a4a"),
              T(x + 54, 308, nom, 10, "#ffffff")]
    # 4 — banc de coulage et moules
    o += [R(656, 284, 134, 12, "#5a6b7b"), L(666, 296, 666, 338, "#4b5b6b", 5), L(780, 296, 780, 338, "#4b5b6b", 5), L(676, 236, 676, 284, "#4b5b6b", 5), L(736, 236, 736, 284, "#4b5b6b", 5)]
    for k in range(4):
        o += [PG(f"{664+k*30},284 {690+k*30},284 {686+k*30},250 {668+k*30},250", "#f3f8fd", "#7a8896", 2), R(670 + k * 30, 244, 14, 8, "#2f75b5")]
    o += [L(676, 238, 736, 238, "#2f75b5", 6)]
    return o


def decor_atomisation():
    o = fond("#dde5ed", "#bcc8d3", 340)
    # 1 — panneau des plaques manquantes
    pl = [R(30, 60, 130, 120, "#ffffff", "#0F4C81", 4, 3), T(95, 82, "Plaques", 12, "#0F4C81")]
    for k in range(5):
        pl += [R(42 + (k % 3) * 38, 94 + (k // 3) * 40, 32, 30, "#f3f8fd", "#9fb0c0", 3, 2, 0.9), T(58 + (k % 3) * 38, 114 + (k // 3) * 40, "?", 14, "#C2410C")]
    o += [G(20, pl)]
    # 2 — tour d'atomisation
    o += [PG("300,60 470,60 490,120 280,120", "#aebdca", "#4b5b6b", 4), R(300, 120, 170, 140, "#b9c8d6", "#4b5b6b", 4, 4), PG("280,260 490,260 410,330 360,330", "#aebdca", "#4b5b6b", 4),
          R(350, 330, 70, 14, "#4b5b6b"), L(385, 20, 385, 60, "#4b5b6b", 6), C(385, 90, 18, 8, "#e6743c"), R(320, 150, 130, 70, "#0b2540", "#9fb0c0", 4, 3),
          T(385, 170, "10 étapes", 11, "#9FD3FF")]
    for k in range(3):
        o += [L(340 + k * 45, 186, 340 + k * 45, 208, "#BFE3FF", 2), C(340 + k * 45, 212, 3, 3, "#BFE3FF")]
    # 3 — cahier du chef sur un bureau
    o += [R(30, 300, 190, 14, "#e6edf3", "#7FA9CF", 3, 2), L(40, 314, 40, 400, "#9aaab8", 6), L(210, 314, 210, 400, "#9aaab8", 6),
          R(60, 274, 100, 28, "#f3f8fd", "#0b2a4a", 3, 2), L(110, 276, 110, 300, "#0b2a4a", 2), L(70, 286, 100, 286, "#9fb0c0", 1), L(120, 286, 150, 286, "#9fb0c0", 1), T(110, 270, "Cahier du chef", 9, "#0b2a4a")]
    # silo
    o += [R(530, 140, 80, 150, "#cfdbe6", "#4b5b6b", 6, 4), PG("530,290 610,290 585,330 555,330", "#aebdca", "#4b5b6b", 3), PG("530,140 570,100 610,140", "#aebdca", "#4b5b6b", 3),
          L(500, 230, 530, 230, "#5a6b7b", 8), T(570, 220, "SILO", 14, "#2b3a4a")]
    # 4 — panneau des trois entreprises
    vi = [R(620, 70, 150, 120, "#ffffff", "#C2410C", 4, 3), T(695, 92, "Visiteurs", 12, "#C2410C")]
    for k, ab in enumerate("ABC"):
        vi += [C(645 + k * 48, 138, 18, 18, "#DCEEFF", "#0F4C81"), T(645 + k * 48, 144, ab, 16, "#0F4C81")]
    o += [G(14, vi)]
    return o


def decor_voie_seche():
    o = fond("#e6dfd2", "#c7bfb0", 340, "#d6cdbb")
    # 2 — tableau des étiquettes
    tb = [R(40, 60, 260, 120, "#ffffff", "#8a6d43", 4, 4)]
    for k, (t, c) in enumerate([("Voie humide", "#DCEEFF"), ("Voie sèche", "#f1e7c8"), ("Les deux", "#ffe9db")]):
        tb += [R(52 + k * 82, 72, 76, 22, c, "#8a6d43", 3, 1), T(90 + k * 82, 88, t, 9)]
        for j in range(3):
            tb += [R(56 + k * 82, 104 + j * 22, 68, 16, "#f3f8fd", "#9fb0c0", 3, 1)]
    o += [G(22, tb)]
    # 4 — plaque de procédé tombée de travers
    o += [G(18, ['<g transform="rotate(-6 410 100)">' + R(330, 62, 160, 70, "#ffffff", "#8a6d43", 4, 3) + T(410, 84, "Voie sèche", 12, "#8a6d43") +
          "".join(R(340 + k * 30, 98 + (k % 2) * 4, 26, 22, "#f1e7c8", "#8a6d43", 3, 1) for k in range(5)) + '</g>'])]
    # concasseur : trémie
    o += [PG("170,190 320,190 290,260 200,260", "#8f8068", "#5c4f3a", 4), R(200, 260, 90, 62, "#a39478", "#5c4f3a", 4, 4), L(245, 200, 245, 255, "#5c4f3a", 3),
          T(245, 300, "Concasseur", 10, "#ffffff")]
    for k in range(5):
        o += [PG(f"{190+k*24},176 {206+k*24},172 {212+k*24},190 {188+k*24},190", "#b09b78", "#5c4f3a", 2)]
    # mélangeur : cuve
    o += [R(330, 232, 140, 90, "#9fb0bf", "#4b5b6b", 14, 4), R(340, 224, 120, 14, "#7a8896"), L(400, 242, 400, 314, "#4b5b6b", 4), L(354, 272, 446, 272, "#4b5b6b", 4), T(400, 312, "Mélangeur", 10, "#2b3a4a")]
    # boudineuse + boudin
    o += [R(480, 252, 90, 70, "#b9c8d6", "#4b5b6b", 8, 4), R(570, 270, 36, 30, "#8fa2b6", "#4b5b6b", 4, 3), R(606, 280, 40, 14, "#d9c7a8", "#8a6d43", 7, 2), T(525, 292, "Boudineuse", 9, "#2b3a4a")]
    # 3 — sacs de poudre, masque accroché et coffre de relance
    o += [R(650, 292, 40, 32, "#e0cfb6", "#8a6d43", 3, 2), R(690, 302, 34, 22, "#d8c3a5", "#8a6d43", 3, 2),
          '<path d="M656 220 q18 -14 36 0 l-7 20 q-11 8 -22 0 z" fill="#f3f8fd" stroke="#0F4C81" stroke-width="2"/>',
          R(728, 262, 58, 64, "#3a4a5c", "#1c2733", 6, 4), R(736, 272, 42, 8, "#e6a23c"), C(757, 302, 8, 8, "#e6a23c", "#8a5a10"), T(757, 256, "Coffre", 10, "#2b3a4a")]
    # 1 — cahier de l'atelier sur un pupitre
    o += [R(25, 300, 110, 12, "#e6edf3", "#7FA9CF", 3, 2), L(34, 312, 34, 400, "#9aaab8", 6), L(126, 312, 126, 400, "#9aaab8", 6),
          R(40, 264, 80, 34, "#f3f8fd", "#0b2a4a", 3, 2), L(80, 266, 80, 296, "#0b2a4a", 2), L(46, 278, 74, 278, "#9fb0c0", 1), L(86, 278, 114, 278, "#9fb0c0", 1)]
    return o


DECOR_FN = {"laboratoire": decor_laboratoire, "broyage": decor_broyage, "hall": decor_hall, "atomisation": decor_atomisation, "voie-seche": decor_voie_seche}


def ecrire_decors():
    out = ["/* Décors dessinés de secours (16:9) — générés par outils/immersif/completer-preparation-pates.py (dessin par script, aucune image IA).",
           "   Une image déposée dans assets/images/decors/<id>.webp|.jpg|.png les remplace. */",
           "var VML = window.VML || (window.VML = {});", "VML.SVG_DECORS = VML.SVG_DECORS || {};"]
    for d in DECORS:
        svg = ('<svg class="decor-svg" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" '
               'style="position:absolute;inset:0;width:100%;height:100%">' + "".join(DECOR_FN[d]()) + "</svg>")
        out.append(f"VML.SVG_DECORS[{json.dumps(d)}] = {json.dumps(svg, ensure_ascii=False)};")
    with open(os.path.join(DEST, "js", "decors-secours.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")


# Zones : (libellé, x, y, w, h, description) en % de l'image 16:9 ; l'ordre suit les énigmes 1 à 4 de la salle.
ZONES = {
    "laboratoire": [("Le tableau des mots", 5, 15, 33, 30, "Le tableau du laboratoire : les mots sont là, les définitions ont disparu."),
                    ("Le panneau des consignes", 42, 17, 18.5, 30, "Un panneau « Préparer une pâte » dont les lignes sont incomplètes."),
                    ("Le carnet de Karim", 67, 59, 13, 11, "Le carnet de notes du technicien, posé sur la paillasse."),
                    ("La fiche des deux méthodes", 82, 19, 13.5, 29, "Une fiche épinglée au mur, à moitié effacée.")],
    "broyage": [("L'écran de la recette", 36.5, 15.3, 26.5, 26, "L'écran de la salle affiche une recette dont les étapes sont mélangées."),
                ("Le panneau des plaques", 4.5, 17.8, 29.5, 28, "Les plaques des machines : l'une est tombée de travers, les autres sont illisibles."),
                ("Le tamis et le délayeur", 51.5, 28, 33, 49, "Le tamis à secousses sur son châssis et la cuve du délayeur."),
                ("L'armoire à cadenas", 89.5, 33, 8.5, 43, "Une armoire fermée par un cadenas à deux molettes.")],
    "hall": [("Les trois chariots", 2.5, 57.5, 46, 17, "Trois chariots attendent, leurs étiquettes mélangées."),
             ("Les commandes clients", 3.5, 15, 19.5, 30, "Des bons de commande punaisés sur un panneau."),
             ("Le filtre-presse", 49.5, 34, 29.5, 40, "Un empilement de plaques filtrantes et la boudineuse dessous."),
             ("Le banc de coulage", 81, 52, 17.5, 22, "Des moules en plâtre alignés sur le banc de coulage.")],
    "atomisation": [("Le panneau des plaques", 3.5, 17.4, 17.5, 29, "Cinq plaques de machines, toutes illisibles."),
                    ("La tour d'atomisation", 35, 5, 27, 70, "La grande tour, avec son écran qui affiche les étapes."),
                    ("Le cahier du chef", 7, 60, 14, 9, "Le cahier du chef d'atelier, ouvert sur son bureau."),
                    ("Le panneau des visiteurs", 77, 18.1, 19, 27, "Trois entreprises, A, B et C, visitent l'usine.")],
    "voie-seche": [("Le cahier de l'atelier", 4, 56, 16, 12, "Le cahier de l'atelier, taché, sur son pupitre."),
                   ("Le tableau des colonnes", 5, 17.9, 33, 27, "Des étiquettes à ranger : voie humide, voie sèche ou les deux."),
                   ("Les sacs, le masque et le coffre", 80.5, 48, 18, 26, "Des sacs de poudre fine, un masque accroché au mur, et le coffre de relance."),
                   ("La plaque tombée", 40.5, 15, 22, 22, "La plaque du procédé, tombée de travers.")]
}

# Narration : par énigme (id) → (problème, enjeu, pourquoi ici, effet, réaction, réplique Essentiel, réplique Expert)
N = {
 "e1-1": ("Le tableau du laboratoire a perdu ses définitions : les mots sont encore là.", "Sans le vocabulaire, personne ne peut lire les consignes de la ligne.",
          "On ne conduit pas une ligne dont on ne connaît pas le vocabulaire.", "eclat", "Les définitions réapparaissent en face de chaque mot.",
          "Commencez par les mots du métier : reliez chaque mot à sa définition.", "Six mots, six définitions. À l'usine, on parle juste."),
 "e1-2": ("Le panneau « Préparer une pâte » est incomplet : il manque les actions.", "Une pâte mal préparée se fissure ou se déforme.",
          "Préparer une pâte, c'est la base de tout le chapitre.", "ouverture", "Le panneau se remplit, ligne par ligne.",
          "Remettez chaque action sur la bonne ligne du panneau.", "Pour chaque but, retrouvez l'action qui l'atteint. Deux étiquettes sont des pièges."),
 "e1-3": ("Karim a noté des phrases dans son carnet, mais certaines sont fausses.", "Une fausse règle dans le carnet, et la ligne repart mal.",
          "Le carnet du laboratoire sert de référence à toute l'équipe.", "calme", "Une coche verte s'allume à côté de chaque phrase vérifiée.",
          "Mon carnet contient des erreurs : vrai ou faux ?", "Vérifiez mes cinq phrases : je ne garde que les vraies."),
 "e1-4": ("La fiche des deux méthodes est à moitié effacée.", "Sans cette fiche, les stagiaires confondent voie humide et voie sèche.",
          "La fiche résume les deux méthodes de préparation.", "lumiere", "La fiche se complète et rejoint le mur.",
          "", "La fiche a des trous, et deux étiquettes sont des pièges. À vous."),
 "e2-1": ("L'écran de la recette de la barbotine de coulage affiche les étapes dans le désordre.", "Dans le mauvais ordre, la barbotine est inutilisable.",
          "L'ordre des étapes est la base du procédé.", "lumiere", "L'écran remet les étapes dans l'ordre, l'une après l'autre.",
          "Remettez les six étapes dans l'ordre, de la pesée au transfert.", "Six étapes, sans repères cette fois."),
 "e2-2": ("Les plaques des machines sont tombées par terre.", "Sans nom, on ne sait plus quelle machine fait quoi.",
          "Reconnaître une machine, c'est comprendre son rôle dans le procédé.", "eclat", "Chaque plaque se remet sur sa machine avec un petit déclic.",
          "Remettez le bon nom sous chaque photo.", "Quatre machines, quatre noms. Regardez bien les photos."),
 "e2-3": ("Le panneau des rôles est effacé : machines et fonctions sont dissociées.", "Mal associée, une machine est mal utilisée.",
          "Chaque machine a un rôle précis dans les étapes communes.", "ouverture", "Les machines s'illuminent, chacune avec son rôle.",
          "Reliez chaque machine à ce qu'elle fait.", "Cinq éléments, cinq rôles. Soyez précis."),
 "e2-4": ("L'armoire du broyeur est fermée par un cadenas à deux molettes.", "Sans les deux nombres, l'armoire reste verrouillée.",
          "Les nombres d'étapes sont des repères du procédé.", "ouverture", "Le cadenas s'ouvre avec un déclic.",
          "", "Deux molettes : deux nombres du cours."),
 "e3-1": ("Les opérations ont été déchargées en vrac devant trois chariots.", "Un chariot mal chargé, et le mauvais produit part chez le client.",
          "Savoir qui fait quoi, c'est connaître les trois procédés.", "ouverture", "Chaque chariot se remplit avec les bonnes opérations.",
          "Rangez chaque étiquette dans le chariot où elle intervient.", "Dix étiquettes, trois chariots : sans erreur."),
 "e3-2": ("Quatre bons de commande attendent une réponse.", "Un mauvais produit, et la commande revient.",
          "Chaque produit a son usage : c'est ainsi qu'on le choisit.", "lumiere", "Les bons de commande se tamponnent « validé ».",
          "Pour chaque commande, quel produit livrer ?", "Quatre clients exigeants : répondez en professionnel."),
 "e3-3": ("Les huit étapes des pâtes plastiques sont mélangées sur le filtre-presse.", "Dans le mauvais ordre, la pâte reste molle ou pleine d'air.",
          "Les pâtes plastiques ont le procédé le plus long de la voie humide, après les poudres.", "eclat", "Le filtre-presse se remet en route, étape après étape.",
          "Remettez les huit étapes dans l'ordre.", "Huit étapes, sans repères."),
 "e3-4": ("Une étape s'est glissée dans le procédé de la barbotine de coulage.", "Si l'intrus reste, on retire l'eau d'une barbotine qui doit rester fluide.",
          "La barbotine de coulage doit rester très fluide.", "calme", "L'étape en trop disparaît du banc de coulage.",
          "", "Une étape n'a rien à faire dans la barbotine de coulage. Laquelle ?"),
 "e4-1": ("Cinq plaques de machines du hall sont illisibles.", "Sans plaque, on ne reconnaît plus les machines du hall.",
          "Reconnaître les équipements du hall fait partie du cours.", "eclat", "Chaque plaque se remet sur sa machine.",
          "Rendez leur nom aux trois machines.", "Cinq machines du hall, cinq noms."),
 "e4-2": ("L'écran de l'atomiseur affiche des étapes mélangées.", "Dans le mauvais ordre, l'atomiseur ne redémarre pas.",
          "L'atomisation suit un ordre précis, des gouttelettes aux granules.", "lumiere", "L'écran se remet dans l'ordre et l'atomiseur ronronne.",
          "Remettez les cinq dernières étapes dans l'ordre.", "Dix étapes à remettre dans l'ordre, des étapes communes jusqu'au stockage."),
 "e4-3": ("Le cahier de consignes du chef d'atelier contient des erreurs.", "Une consigne fausse, et c'est toute la ligne qui est mal réglée.",
          "Le cahier du chef reprend les définitions du cours.", "calme", "Les phrases fausses sont barrées en rouge.",
          "Trouvez si chaque phrase du cahier est vraie ou fausse.", "Six phrases du chef : trouvez les erreurs et lisez les corrections."),
 "e4-4": ("Trois entreprises visitent l'usine, mais elles ne fabriquent pas les mêmes produits.", "Une mauvaise réponse, et le visiteur repart avec une fausse idée.",
          "Une entreprise choisit ses produits et ses équipements.", "ouverture", "Les badges A, B et C se valident l'un après l'autre.",
          "", "Trois entreprises, cinq questions."),
 "e5-1": ("Le cahier de l'atelier est taché : il manque un mot dans chaque phrase.", "Sans le cahier, personne ne sait comment fonctionne la voie sèche.",
          "La voie sèche suit cinq étapes précises.", "ouverture", "Les mots réapparaissent sous les taches.",
          "Remplissez le cahier avec les bons mots.", "Il manque un mot dans chaque phrase. Une étiquette est en trop."),
 "e5-2": ("Les étiquettes du tableau sont mélangées : voie humide, voie sèche ou les deux ?", "Un équipement mal classé, et on commande la mauvaise machine.",
          "Comparer les deux méthodes, c'est le cœur de la synthèse.", "eclat", "Chaque étiquette se colle dans sa colonne.",
          "Rangez chaque étiquette dans la bonne colonne.", "Neuf étiquettes, trois colonnes."),
 "e5-3": ("Le coffre est dans la pièce où l'on ouvre les sacs de poudre fine et volatile.", "Un mauvais geste, et la poudre se retrouve dans l'air.",
          "Les poudres sont fines et volatiles : la sécurité passe avant tout.", "calme", "Le voyant du coffre passe au vert.",
          "Un seul de ces gestes est dangereux. Lequel ?", "Trouvez le geste qui ne protège pas."),
 "e5-4": ("La plaque du procédé est tombée de travers : les cinq étapes sont mélangées.", "Dans le mauvais ordre, la pâte garde ses bulles d'air.",
          "L'ordre des étapes de la voie sèche est le dernier verrou du coffre.", "lumiere", "La plaque se redresse, les étapes dans l'ordre.",
          "", "Cinq étapes, du concassage à l'extrusion."),
}


def lire(n):
    with open(os.path.join(DATA, n), encoding="utf-8") as f:
        return json.load(f)


def ecrire(n, d):
    with open(os.path.join(DATA, n), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


def lycee():
    """Réglages propres au lycée : libellés Essentiel / Expert, plaques bleues, jauge, écran des pages."""
    for page, prof in (("index.html", 2), ("prof.html", 2)):
        p = os.path.join(DEST, page)
        h = open(p, encoding="utf-8").read()
        balise = '<script src="../../commun/lycee-pro/libelles.js?l1"></script>\n'
        if "libelles.js" not in h:
            h = h.replace("</body>", balise + "</body>", 1)
        h = h.replace("Réserve d'air (décor, sans effet sur les points)", "Pression de la ligne (décor, sans effet sur les points)")
        h = h.replace("Réserve d'air : un décor, elle ne retire aucun point", "Pression de la ligne : un décor qui baisse un peu à chaque indice, sans retirer aucun point")
        h = h.replace('<span class="jauge-lib">Air <b', '<span class="jauge-lib">Pression <b')
        h = h.replace('placeholder="ex. : Les Hublots"', 'placeholder="ex. : Les Tamis"')
        h = h.replace("Votre grade à bord", "Votre niveau")
        h = h.replace("La jauge d'air est un décor : elle ne retire aucun point.", "La jauge de pression est un décor : elle ne retire aucun point.")
        h = h.replace(">Embarquer</button>", ">Commencer</button>")
        h = h.replace("Reprendre la plongée", "Reprendre la partie")
        open(p, "w", encoding="utf-8", newline="\n").write(h)
    pa = os.path.join(DEST, "js", "app.js")
    a = open(pa, encoding="utf-8").read()
    a = a.replace("L'équipage au complet", "Les notions clés, avec des repères")
    open(pa, "w", encoding="utf-8", newline="\n").write(a)
    p = os.path.join(DEST, "css", "theme.css")
    c = open(p, encoding="utf-8").read()
    if "plaque-haut" not in c:
        c += ("/* Plaques de dialogue et cadres : bleu nuit du CAP (au lieu du bois du modèle) */\n:root{\n"
              "  --plaque-haut: rgba(14,47,82,.96); --plaque-bas: rgba(6,24,43,.97);\n"
              "  --cadre-haut: rgba(14,47,82,.94); --cadre-bas: rgba(6,24,43,.96);\n  --laiton-profond: #0F4C81;\n}\n")
        open(p, "w", encoding="utf-8", newline="\n").write(c)


def rapport():
    txt = """# Rapport de migration — Panne à l'usine

Données sources : `preparation-pates/assets/data/` (générées par `outils/generer-preparation-pates.py`, **non modifiées** par la migration).
Variante immersive : `immersifs/preparation-pates/`.

- 5 salles, 15 énigmes Essentiel (grade matelot) / 20 énigmes Expert (grade timonier).
- Le moteur est une copie de celui de « Vingt mille lieues » ; seuls `js/jeu-config.js`, `css/theme.css`, `js/decors-secours.js` et `assets/data/*.json` sont propres à ce jeu.

## Complété (dépôt lycée pro)

- Thème : `outils/immersif/theme-preparation-pates.json` (grades Essentiel / Expert, palette du CAP, jauge « Pression »).
- `python outils/immersif/completer-preparation-pates.py immersifs/preparation-pates` : décors dessinés 16:9 (par script, aucune image IA), 20 zones nommées, problème narratif, enjeu, réaction du décor et répliques des deux grades pour les 20 énigmes ; libellés Essentiel / Expert.
- Photos des machines dans `assets/images/cartes/` (énigmes 2-2 et 4-1), fournies par l'enseignant : licence à vérifier (voir `preparation-pates/A-VERIFIER.md`).

## Reste facultatif

- Images de décor et portraits (`medias.csv`) : à produire seulement avec l'accord de l'enseignant ; recaler les zones avec `outils/caler-effets.html` si une image est déposée.
- Grades supplémentaires (mousse, lieutenant, second).

## Vérifier

```
node immersifs/preparation-pates/tests/test-immersif.js
```
"""
    with open(os.path.join(DEST, "MIGRATION-RAPPORT.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)


def main():
    ecrire_decors()
    fx = lire("decors-fx.json")
    for d in DECORS:
        z = []
        for k, (lib, x, y, w, h, desc) in enumerate(ZONES[d]):
            z.append({"id": f"objet-{k+1}", "libelle": lib, "x": x, "y": y, "w": w, "h": h, "description": desc})
        fx["decors"][d]["zones"] = z
        fx["decors"][d]["ambiance"] = ["vent"]
        fx["decors"][d].pop("_brouillon", None)
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
            en["liberte_ou_anachronisme"] = "Usine et personnages inventés ; toutes les données techniques viennent du cours. Le cours précise que les procédés présentés sont des exemples."
            en["niveau_variantes"] = "Essentiel (grade matelot) : repères et étapes en moins. Expert (grade timonier) : sans repères, procédés complets, plus de machines."
            if "matelot" in en and d1:
                en["matelot"]["dialogue"] = d1
            if "timonier" in en and d2:
                en["timonier"]["dialogue"] = d2
            en["_brouillon"] = [b for b in en.get("_brouillon", []) if b == "zones" and False]
            if not en["_brouillon"]:
                en.pop("_brouillon")
    ecrire("enigmes.json", e)
    lycee()
    rapport()
    print("✔ brouillons complétés : 5 décors 16:9, 20 zones, 20 énigmes (narration, réactions, répliques), réglages lycée.")


if __name__ == "__main__":
    main()
