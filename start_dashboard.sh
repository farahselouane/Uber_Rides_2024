#!/bin/bash
# Script de lancement du dashboard Uber Rides 2024
# ================================================

echo
echo "======================================"
echo "  TABLEAU DE BORD UBER RIDES 2024"
echo "======================================"
echo

cd dashboard

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "ERREUR: Python n'est pas installé"
    exit 1
fi

# Vérifier si les dépendances sont installées
python3 -c "import dash" 2>/dev/null
if [ $? -ne 0 ]; then
    echo
    echo "⚠️  Installation des dépendances requises..."
    pip3 install -r ../requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERREUR: Impossible d'installer les dépendances"
        exit 1
    fi
fi

echo
echo "✓ Lancement du dashboard..."
echo "✓ Allez à: http://localhost:8050"
echo
echo "Appuyez sur Ctrl+C pour arrêter le dashboard"
echo

# Lancer l'application
python3 app.py
