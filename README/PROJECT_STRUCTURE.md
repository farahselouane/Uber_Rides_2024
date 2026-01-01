# 🗂️ STRUCTURE DU PROJET UBER RIDES 2024

```
Projet1_Dash/
└── Uber_Rides_2024/
    ├── 📁 data/
    │   ├── raw/
    │   │   └── ride_bookings.csv (150k lignes)
    │   └── processed/
    │       └── ride_bookings_clean.csv (nettoyées) ⭐
    │
    ├── 📁 dashboard/ ⭐⭐⭐ MAIN APPLICATION
    │   ├── app.py (Application Dash principale)
    │   ├── __init__.py
    │   │
    │   ├── 📁 assets/
    │   │   └── style.css (Styles responsive)
    │   │
    │   └── 📁 pages/
    │       ├── __init__.py
    │       ├── overview.py (📈 Vue d'ensemble - 4 KPIs + 3 graphiques)
    │       ├── operations.py (⚙️ Opérations - 3 KPIs + 4 graphiques)
    │       ├── finance.py (💰 Finance - 3 KPIs + 4 graphiques)
    │       ├── home.py (Template)
    │       ├── analytics.py (Template)
    │       └── insights.py (Template)
    │
    ├── 📁 notebooks/ (Jupyter Analysis)
    │   └── Uber_Rides_2024_Project.ipynb (60 cellules, 5 PARTIE)
    │
    ├── 📁 src/ (Scripts utilitaires)
    │   ├── data_loader.py
    │   ├── data_cleaner.py
    │   ├── eda_analysis.py
    │   └── visualization.py
    │
    ├── 📁 config/
    │   └── settings.py
    │
    ├── 📁 .venv/ (Virtual Environment Python 3.13)
    │
    ├── 📄 requirements.txt (Dépendances Python)
    │
    ├── 🎬 start_dashboard.bat (Lancement Windows)
    ├── 🎬 start_dashboard.sh (Lancement Linux/Mac)
    ├── 🧪 test_dashboard.py (Tests de validation)
    │
    ├── 📖 DASHBOARD_README.md (Guide d'utilisation)
    ├── ⚙️ DASHBOARD_CONFIG.md (Configuration détaillée)
    ├── 📋 DEPLOYMENT_REPORT.md (Rapport de déploiement)
    ├── 📄 README.md (Readme du projet)
    └── 📄 PROJECT_STRUCTURE.md (Ce fichier)
```

---

## 📊 Vue détaillée du Dashboard

```
┌─────────────────────────────────────────────────────────┐
│          🎨 NAVBAR (violet gradient)                    │
│    📊 TABLEAU DE BORD UBER RIDES 2024                   │
│    [📈 Vue d'ensemble] [⚙️ Opérations] [💰 Finance]    │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│          🔍 FILTRES GLOBAUX (réactifs)                 │
│  [📅 Dates] [🚗 Véhicule] [💳 Paiement] [📊 Statut]  │
│  ✓ Données filtrées: XXXXX réservations                │
└─────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────┬──────────────────┬──────────────────┐
│  🎯 KPI CARDS    │  🎯 KPI CARDS    │  🎯 KPI CARDS    │
│  ▲ Metrique 1    │  ▲ Metrique 2    │  ▲ Metrique 3    │
│  12,345          │  87.5%           │  $1,234,567      │
└──────────────────┴──────────────────┴──────────────────┘
                           ↓
┌──────────────────┬──────────────────┬──────────────────┐
│   📈 GRAPHIQUE   │   📊 GRAPHIQUE   │   📉 GRAPHIQUE   │
│   (Line Chart)   │   (Bar Chart)    │   (Pie Chart)    │
│   Interactif     │   Interactif     │   Interactif     │
└──────────────────┴──────────────────┴──────────────────┘
```

---

## 🗺️ Pages du Dashboard

### PAGE 1: 📈 Vue d'ensemble (`/overview`)
```
KPI CARDS (4):
  1️⃣ Total réservations (ex: 150,000)
  2️⃣ Taux complétés (ex: 85.2%)
  3️⃣ Revenu total (ex: $2,345,678)
  4️⃣ Valeur moyenne (ex: $15.64)

GRAPHIQUES (3):
  📅 Évolution mensuelle (Line chart)
     → Tendance des réservations par mois
  
  📊 Distribution des statuts (Bar chart)
     → COMPLETED, CANCELLED BY CUSTOMER, etc.
  
  🚗 Top 5 véhicules (Bar chart horizontal)
     → Nombre de réservations par type
```

### PAGE 2: ⚙️ Analyse opérationnelle (`/operations`)
```
KPI CARDS (3):
  1️⃣ VTAT moyen (ex: 12.5 min)
  2️⃣ CTAT moyen (ex: 4.2 min)
  3️⃣ Taux annulation (ex: 14.8%)

GRAPHIQUES (4):
  🛣️ Distribution distances (Histogram)
     → Nombre de trajets par distance (km)
  
  ⏱️ Distance vs Durée (Scatter plot)
     → Corrélation entre distance et temps
  
  ✓ Taux de complétude (Pie chart)
     → Complétés vs Annulés vs Autres
  
  ❌ Raisons annulation (Bar chart)
     → Top 5 raisons d'annulation
```

### PAGE 3: 💰 Analyse financière (`/finance`)
```
KPI CARDS (3):
  1️⃣ Revenu total (ex: $2,345,678)
  2️⃣ Revenu confirmé (ex: $1,995,000)
  3️⃣ Valeur moyenne (ex: $15.64)

GRAPHIQUES (4):
  💰 Revenu par véhicule (Bar chart horizontal)
     → Revenu total par type (UberX, XL, etc.)
  
  💳 Revenu par paiement (Bar chart)
     → Revenu total par méthode (carte, portefeuille, etc.)
  
  📊 Distribution valeurs (Histogram)
     → Nombre de trajets par montant
  
  💹 Revenu vs Distance (Scatter plot)
     → Corrélation prix/distance
```

---

## 🎯 Filtres globaux (4)

| Filtre | Type | Options | Impact |
|--------|------|---------|--------|
| 📅 Dates | DatePickerRange | Début → Fin | ✓ Tous les KPIs & graphiques |
| 🚗 Véhicule | Dropdown | UberX, XL, Select, Premier | ✓ Tous les KPIs & graphiques |
| 💳 Paiement | Dropdown | Carte, Portefeuille, Espèces | ✓ Tous les KPIs & graphiques |
| 📊 Statut | Dropdown | COMPLETED, CANCELLED, etc. | ✓ Tous les KPIs & graphiques |

**Comportement**: Changements → Mise à jour instantanée de TOUS les KPIs et graphiques

---

## 🔄 Flux de données

```
CSV
 ↓
┌────────────────────────────────┐
│  app.py                        │
│  • Charge CSV au démarrage     │
│  • Stocke en DataFrame         │
└────────────────────────────────┘
 ↓
┌────────────────────────────────┐
│  Filtres globaux               │
│  • Date range                  │
│  • Vehicle type                │
│  • Payment method              │
│  • Booking status              │
└────────────────────────────────┘
 ↓ (Callback: update_filtered_data)
┌────────────────────────────────┐
│  dcc.Store (filtered-data)     │
│  • JSON de données filtrées    │
│  • Partagé avec toutes les pages
└────────────────────────────────┘
 ↓ (Callback: display_page)
┌────────────────────────────────┐
│  Pages (overview/ops/finance)  │
│  • Calcul KPIs                 │
│  • Génération graphiques       │
│  • Retour layout HTML          │
└────────────────────────────────┘
 ↓
┌────────────────────────────────┐
│  Navigateur                    │
│  • Affichage page              │
│  • Interactivité Plotly        │
│  • Navigation avec nav links   │
└────────────────────────────────┘
```

---

## 📊 KPIs calculés

### Vue d'ensemble
- `total_bookings`: `COUNT(*)`
- `completed_count`: `COUNT(booking_status == 'COMPLETED')`
- `completed_rate`: `completed_count / total * 100`
- `total_revenue`: `SUM(ride_value WHERE booking_status == 'COMPLETED')`
- `avg_ride_value`: `AVG(ride_value)`

### Opérations
- `vtat_avg`: `AVG(vtat WHERE booking_status == 'COMPLETED')`
- `ctat_avg`: `AVG(ctat WHERE booking_status IN [...])`
- `cancelled_count`: `COUNT(booking_status IN [...CANCELLED...])`
- `cancellation_rate`: `cancelled_count / total * 100`

### Finance
- `total_revenue`: `SUM(ride_value)`
- `completed_revenue`: `SUM(ride_value WHERE booking_status == 'COMPLETED')`
- `avg_ride_value`: `AVG(ride_value)`
- `revenue_by_vehicle`: `SUM(ride_value) GROUP BY vehicle_type`
- `revenue_by_payment`: `SUM(ride_value) GROUP BY payment_method`

---

## 🎨 Palette de couleurs

```
#667eea  ████████ Primaire (Navbar, KPI borders)
#764ba2  ████████ Secondaire (Gradient navbar)
#2ca02c  ████████ Succès (KPIs complétés, vert)
#d62728  ████████ Danger (Annulations, rouge)
#ff7f0e  ████████ Warning (Autres, orange)
#1f77b4  ████████ Info (Graphiques principaux)
#f5f7fa  ████████ Fond (Arrière-plan page)
#ffffff  ████████ Blanc (Cartes, containers)
#cccccc  ████████ Gris clair (Borders)
#333333  ████████ Texte dark
```

---

## 🔧 Technologies utilisées

```
Frontend:
  • Dash (Plotly) - Framework web interactif
  • Plotly - Visualisations interactives
  • CSS3 - Styles (Grid, Flexbox, responsive)
  • HTML5 - Markup

Backend:
  • Python 3.13 - Langage principal
  • Pandas - Data processing
  • NumPy - Calculs numériques
  • Werkzeug - Serveur dev

Données:
  • CSV - Format données
  • JSON - Sérialisation (dcc.Store)
  • Pandas DataFrame - Format interne
```

---

## 📈 Statistiques

| Catégorie | Nombre |
|-----------|--------|
| Fichiers Python | 8 |
| Lignes de code (total) | ~7,000 |
| Fichiers CSS | 1 |
| Lignes CSS | 287 |
| Pages du dashboard | 3 |
| KPIs affichés | 11 |
| Graphiques | 11 |
| Filtres | 4 |
| Données traitées | 150,000 réservations |
| Colonnes | 25 |

---

## 🚀 Démarrage rapide

### Méthode 1: Windows (Batch)
```batch
start_dashboard.bat
```

### Méthode 2: Linux/Mac (Shell)
```bash
chmod +x start_dashboard.sh
./start_dashboard.sh
```

### Méthode 3: Manuel
```bash
# Installer dépendances
pip install -r requirements.txt

# Lancer dashboard
cd dashboard
python app.py

# Accéder à http://localhost:8050
```

---

## 📚 Documentation fournie

| Fichier | Pages | Contenu |
|---------|-------|---------|
| DASHBOARD_README.md | 8 | Guide d'utilisation, installation, features |
| DASHBOARD_CONFIG.md | 7 | Configuration, stack tech, conventions |
| DEPLOYMENT_REPORT.md | 10 | Rapport complet, checklist, statistiques |
| PROJECT_STRUCTURE.md | 10 | Ce fichier - arborescence et architecture |

---

## ✅ Checklist de production

- [x] Code Python sans erreurs
- [x] Tous les imports fonctionnent
- [x] CSS responsive et complet
- [x] Données accessibles
- [x] Dépendances dans requirements.txt
- [x] Scripts de démarrage fournis
- [x] Tests de validation passent
- [x] Documentation complète

---

## 🎓 Notes de développement

### Points importants
1. **Données chargées une fois** au démarrage (performance)
2. **Filtres en temps réel** avec callbacks Dash
3. **dcc.Store** pour partager les données filtrées entre pages
4. **CSS responsive** adapté à tous les écrans
5. **KPIs dynamiques** calculés depuis les données filtrées

### À améliorer (future)
- Ajouter caching pour les graphiques
- Exporter en PDF/Excel
- Alertes sur les seuils
- Comparaison période précédente
- Prévisions ML

---

**Version**: 1.0  
**Créé**: 2 Janvier 2026  
**Status**: ✅ Production Ready
