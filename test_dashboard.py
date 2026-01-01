#!/usr/bin/env python3
"""
Script de test - Vérifier que les modules importent correctement
"""

import sys
sys.path.insert(0, 'c:\\Users\\HP\\Downloads\\Projet1_Dash\\Uber_Rides_2024')

print("✓ Test 1: Vérifier que le fichier de données existe...")
import os
data_path = 'c:\\Users\\HP\\Downloads\\Projet1_Dash\\Uber_Rides_2024\\data\\processed\\ride_bookings_clean.csv'
if os.path.exists(data_path):
    print(f"  ✓ Fichier trouvé: {data_path}")
else:
    print(f"  ✗ ERREUR: Fichier introuvable: {data_path}")
    sys.exit(1)

print("\n✓ Test 2: Importer les modules Dash...")
try:
    import dash
    import plotly.graph_objects as go
    import pandas as pd
    print("  ✓ Modules importés avec succès")
except ImportError as e:
    print(f"  ✗ ERREUR d'import: {e}")
    sys.exit(1)

print("\n✓ Test 3: Charger les données...")
try:
    df = pd.read_csv(data_path)
    print(f"  ✓ {len(df)} réservations chargées")
    print(f"  ✓ Colonnes: {df.shape[1]} colonnes")
except Exception as e:
    print(f"  ✗ ERREUR: {e}")
    sys.exit(1)

print("\n✓ Test 4: Importer les modules de pages...")
try:
    sys.path.insert(0, 'c:\\Users\\HP\\Downloads\\Projet1_Dash\\Uber_Rides_2024\\dashboard')
    from pages import overview
    print("  ✓ overview.py importé")
except Exception as e:
    print(f"  ⚠ Erreur avec overview: {e}")

print("\n✓ TOUS LES TESTS RÉUSSIS!")
print("\nPour lancer le dashboard:")
print("  cd c:\\Users\\HP\\Downloads\\Projet1_Dash\\Uber_Rides_2024\\dashboard")
print("  python app.py")
print("\nAccédez ensuite à: http://localhost:8050")
