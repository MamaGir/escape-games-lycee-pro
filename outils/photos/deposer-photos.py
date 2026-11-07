#!/usr/bin/env python3
"""Fabrique la planche « Six gisements d'argile » de la leçon 3 (jeu classique « Les fiches du four »).

Deux sources possibles :
  1. Photos libres (recommandé, le dépôt est public) : mettre six fichiers dans un dossier, nommés
        kaolin.jpg  ball-clay.jpg  terre-a-feu.jpg  terre-a-gres.jpg  argiles-communes.jpg  bentonite.jpg
     puis :  python outils/photos/deposer-photos.py --dossier <dossier> --credits "Auteur, licence, URL ; …"
  2. Photos du cours (.docx de l'enseignant) :
        python outils/photos/deposer-photos.py --docx "Les_pates_ceramiques_CAP1_simplifie.docx"
     Les images sont lues dans l'ordre du document (1 = kaolin, 2 = kaolin bis ignorée, 3 = ball clay,
     4 = terre à feu, 5 = terre à grès, 6 = argiles communes, 7 = bentonite). Vérifier la licence de ces
     photos AVANT de pousser le dépôt public (voir A-VERIFIER.md).

Écrit pates-ceramiques/assets/images/documents/gisements-argiles.jpg et complète CREDITS-medias.md.
Nécessite Pillow :  pip install pillow
"""
import argparse, io, os, re, sys, zipfile
from PIL import Image, ImageDraw, ImageFont

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SORTIE = os.path.join(RACINE, "pates-ceramiques", "assets", "images", "documents", "gisements-argiles.jpg")
CREDITS = os.path.join(RACINE, "pates-ceramiques", "assets", "medias", "CREDITS-medias.md")
ARGILES = [("kaolin", "Kaolin"), ("ball-clay", "Ball clay"), ("terre-a-feu", "Terre à feu"),
           ("terre-a-gres", "Terre à grès"), ("argiles-communes", "Argiles communes"), ("bentonite", "Bentonite")]
ORDRE_DOCX = [0, 2, 3, 4, 5, 6]          # index des images du .docx retenues, dans l'ordre d'ARGILES


def images_docx(chemin):
    with zipfile.ZipFile(chemin) as z:
        doc = z.read("word/document.xml").decode("utf-8")
        rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
        cible = dict(re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"', rels))
        ids = re.findall(r'r:embed="([^"]+)"', doc)
        return [Image.open(io.BytesIO(z.read("word/" + cible[i]))).convert("RGB") for i in ids]


def police(t):
    for f in ("C:/Windows/Fonts/calibrib.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        if os.path.exists(f):
            return ImageFont.truetype(f, t)
    return ImageFont.load_default()


def planche(imgs):
    W, H, M, B = 420, 280, 12, 44
    out = Image.new("RGB", (3 * W + 4 * M, 2 * (H + B) + 3 * M), "#F3F8FD")
    d, f = ImageDraw.Draw(out), police(26)
    for k, (im, (_, nom)) in enumerate(zip(imgs, ARGILES)):
        r = max(W / im.width, H / im.height)
        im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1))
        x0, y0 = (im.width - W) // 2, (im.height - H) // 2
        im = im.crop((x0, y0, x0 + W, y0 + H))
        x, y = M + (k % 3) * (W + M), M + (k // 3) * (H + B + M)
        out.paste(im, (x, y))
        d.rectangle([x, y + H, x + W, y + H + B], fill="#0F4C81")
        d.text((x + 12, y + H + 8), nom, fill="#FFFFFF", font=f)
    return out


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--dossier"); a.add_argument("--docx"); a.add_argument("--credits", default="")
    o = a.parse_args()
    if o.docx:
        toutes = images_docx(o.docx)
        if len(toutes) < 7:
            sys.exit(f"Le document contient {len(toutes)} images ; 7 attendues (voir l'en-tête du script).")
        imgs, source = [toutes[i] for i in ORDRE_DOCX], o.credits or "Photos du cours « Les pâtes céramiques » (licence à vérifier)"
    elif o.dossier:
        imgs = []
        for base, _ in ARGILES:
            f = next((os.path.join(o.dossier, base + e) for e in (".jpg", ".jpeg", ".png", ".webp") if os.path.exists(os.path.join(o.dossier, base + e))), None)
            if not f:
                sys.exit(f"Photo manquante : {base}.jpg dans {o.dossier}")
            imgs.append(Image.open(f).convert("RGB"))
        source = o.credits or "Photos libres (auteurs et licences à compléter)"
    else:
        sys.exit("Indiquer --dossier <dossier> ou --docx <fichier.docx>.")
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    planche(imgs).save(SORTIE, "JPEG", quality=82, optimize=True)
    with open(CREDITS, "a", encoding="utf-8") as f:
        f.write(f"\n- `assets/images/documents/gisements-argiles.jpg` (leçon 3, planche de six photos) : {source}\n")
    print("✔ planche écrite :", os.path.relpath(SORTIE, RACINE), "— crédits ajoutés à CREDITS-medias.md")


if __name__ == "__main__":
    main()
