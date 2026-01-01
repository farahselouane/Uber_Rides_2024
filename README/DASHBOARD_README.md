# 📊 DASHBOARD UBER RIDES 2024

Dashboard interactif multi-pages pour l'analyse des données Uber Rides 2024.

## 🚀 Installation & Lancement

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancer le dashboard
```bash
cd dashboard
python app.py
```

### 3. Accéder au dashboard
Ouvrez votre navigateur et allez à: **http://localhost:8050**

## 📑 Pages disponibles

### 📈 **Vue d'ensemble**
- **4 KPIs**: Total réservations, Taux complétés, Revenu total, Valeur moyenne
- **3 Graphiques**:
  - Évolution mensuelle des réservations
  - Distribution des statuts de réservation
  - Top 5 types de véhicules

### ⚙️ **Analyse opérationnelle**
- **3 KPIs**: VTAT moyen, CTAT moyen, Taux d'annulation
- **4 Graphiques**:
  - Distribution des distances de trajet
  - Relation Distance vs Durée
  - Taux de complétude
  - Top raisons d'annulation

### 💰 **Analyse financière**
- **3 KPIs**: Revenu total, Revenu confirmé, Valeur moyenne
- **4 Graphiques**:
  - Revenu par type de véhicule
  - Revenu par méthode de paiement
  - Distribution des valeurs de trajet
  - Relation Revenu vs Distance

## 🔍 Filtres globaux

Tous les graphiques et KPIs se mettent à jour en temps réel selon les filtres:

- **Plage de dates**: Sélectionner la période d'analyse
- **Type de véhicule**: Filtrer par UberX, UberXL, UberSelect, etc.
- **Méthode de paiement**: Filtrer par carte, portefeuille, espèces
- **Statut de réservation**: Filtrer par COMPLETED, CANCELLED, etc.

## 📊 Architecture technique

```
dashboard/
├── app.py                 # Application principale Dash
├── assets/
│   └── style.css         # Styles CSS
├── pages/
│   ├── __init__.py
│   ├── overview.py       # Page vue d'ensemble
│   ├── operations.py     # Page opérations
│   ├── finance.py        # Page finance
│   ├── home.py           # (Template)
│   ├── analytics.py      # (Template)
│   └── insights.py       # (Template)
└── requirements.txt
```

## 🔧 Configuration

Les données sont chargées depuis: `../data/processed/ride_bookings_clean.csv`

Assurez-vous que ce fichier existe avant de lancer le dashboard.

## 📋 Dépendances principales

- **dash**: Framework web interactif
- **plotly**: Visualisations interactives
- **pandas**: Traitement des données
- **numpy**: Calculs numériques

## 💡 Notes

- Le dashboard utilise un design responsive qui s'adapte à tous les écrans
- Les données sont stockées en JSON dans un composant dcc.Store pour des mises à jour rapides
- Le routing utilise dcc.Location pour la navigation multi-pages
- Les couleurs utilisent une palette cohérente (bleu #1f77b4, vert #2ca02c, rouge #d62728, orange #ff7f0e)

## 🚨 Dépannage

**Erreur: "FileNotFoundError: Le fichier ../data/processed/ride_bookings_clean.csv n'existe pas"**
→ Vérifiez que le fichier CSV existe au bon endroit

**Erreur: "ModuleNotFoundError: No module named 'dash'"**
→ Installez les dépendances: `pip install -r requirements.txt`

**Le port 8050 est déjà utilisé**
→ Modifiez app.py ligne 179: `app.run_server(port=8051, ...)`

---

**Créé pour le projet Uber Rides 2024 - M203 Module**
