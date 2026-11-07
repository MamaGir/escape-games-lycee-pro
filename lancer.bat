@echo off
chcp 65001 >nul
title Escape Games pedagogiques - Serveur local
cls
echo.
echo  ============================================================
echo    ESCAPE GAMES PEDAGOGIQUES - CM1/CM2 - Serveur local
echo  ============================================================
echo.
echo  Verification de Python...
echo.

REM Tester python puis py (Windows)
python --version >nul 2>&1
if %errorlevel%==0 (
    set CMD=python
    goto :lancer
)
py --version >nul 2>&1
if %errorlevel%==0 (
    set CMD=py
    goto :lancer
)

echo  [ERREUR] Python n'est pas installe ou pas dans le PATH.
echo.
echo  Solutions :
echo    1. Installer Python : https://www.python.org/downloads/
echo       (cocher "Add Python to PATH" pendant l'installation)
echo    2. OU jouer en ligne : (adresse GitHub Pages du depot escape-games-lycee-pro)
echo.
pause
exit /b 1

:lancer
echo  Python detecte :
%CMD% --version
echo.
echo  ^>^> PORTAIL LYCEE PRO :
echo      http://127.0.0.1:8000/
echo.
echo  ^>^> LES FICHES DU FOUR (pates ceramiques) :
echo      Classique : http://127.0.0.1:8000/pates-ceramiques/
echo      Immersif  : http://127.0.0.1:8000/immersifs/pates-ceramiques/
echo      Enseignant: http://127.0.0.1:8000/pates-ceramiques/prof.html
echo.
echo  Fermez cette fenetre pour arreter le serveur.
echo.

REM Ouvrir le navigateur apres 2 secondes
start "" timeout /t 2 /nobreak >nul ^& start "" http://127.0.0.1:8000/

%CMD% serveur.py 8000
pause
