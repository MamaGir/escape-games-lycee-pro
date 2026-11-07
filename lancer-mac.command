#!/bin/bash
# ============================================================
# ESCAPE GAMES LYCEE PRO (CAP) - Lancement (macOS / Linux)
# ============================================================
cd "$(dirname "$0")"
echo ""
echo "  ============================================================"
echo "    ESCAPE GAMES LYCÉE PRO (CAP) - Serveur local"
echo "  ============================================================"
echo ""

if ! command -v python3 &> /dev/null; then
    echo "  [ERREUR] Python 3 n'est pas installé."
    echo "  Installez-le depuis https://www.python.org/downloads/"
    echo "  Ou jouez en ligne : https://mamagir.github.io/escape-games-lycee-pro/"
    echo ""
    read -p "Appuyez sur Entrée pour quitter..."
    exit 1
fi

echo "  Python détecté :"
python3 --version
echo ""
echo "  >> PORTAIL           http://127.0.0.1:8000/"
echo "  >> ESPACE ENSEIGNANT http://127.0.0.1:8000/enseignant.html"
echo "  >> VÉRIFICATION      http://127.0.0.1:8000/verifier.html"
echo "  >> ÉLÈVES (même réseau) : adresses affichées par le serveur ci-dessous."
echo ""
echo "  Fermez cette fenêtre pour arrêter le serveur."
echo ""

( sleep 2; open "http://127.0.0.1:8000/" 2>/dev/null || xdg-open "http://127.0.0.1:8000/" 2>/dev/null ) &
python3 serveur.py 8000
