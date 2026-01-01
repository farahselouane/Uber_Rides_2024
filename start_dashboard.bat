@echo off
REM Script de lancement du dashboard Uber Rides 2024
REM ================================================

echo.
echo ======================================
echo   TABLEAU DE BORD UBER RIDES 2024
echo ======================================
echo.

cd dashboard

REM Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERREUR: Python n'est pas installé ou non accessible
    pause
    exit /b 1
)

REM Vérifier si les dépendances sont installées
python -c "import dash" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Installation des dépendances requises...
    pip install -r ../requirements.txt
    if %errorlevel% neq 0 (
        echo ERREUR: Impossible d'installer les dépendances
        pause
        exit /b 1
    )
)

echo.
echo ✓ Lancement du dashboard...
echo ✓ Allez à: http://localhost:8050
echo.
echo Appuyez sur Ctrl+C pour arrêter le dashboard
echo.

REM Lancer l'application
python app.py

pause
