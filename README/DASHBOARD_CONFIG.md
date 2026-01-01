# Configuration du Dashboard Uber Rides 2024

## 🎯 Résumé du projet

### Notebook (Jupyter)
- **Fichier**: `notebooks/Uber_Rides_2024_Project.ipynb`
- **Structure**: 60 cellules réparties dans 5 PARTIE sections
- **Contenu**:
  - PARTIE 1: Chargement, exploration et préparation des données
  - PARTIE 2: Analyse métier (KPIs, géographie, opérations, trajets incomplets)
  - PARTIE 3: 6 visualisations (évolution, distribution, box plot, etc.)
  - PARTIE 4: Architecture du dashboard
  - PARTIE 5: 6 recommandations data-driven

### Dashboard (Dash)
- **Dossier**: `dashboard/`
- **Fichiers**:
  - `app.py`: Application principale (routing, filtres, layout)
  - `pages/overview.py`: Vue d'ensemble (KPIs + 3 graphiques)
  - `pages/operations.py`: Analyse opérationnelle (KPIs + 4 graphiques)
  - `pages/finance.py`: Analyse financière (KPIs + 4 graphiques)
  - `assets/style.css`: Styles responsive
  - `requirements.txt`: Dépendances Python

## 📊 Fichiers de données

```
data/
├── raw/
│   └── ride_bookings.csv          # Données brutes (150,000 réservations)
└── processed/
    └── ride_bookings_clean.csv    # Données nettoyées (utilisées par le dashboard)
```

## 🚀 Démarrage rapide

### Option 1: Windows (fichier batch)
```bash
start_dashboard.bat
```

### Option 2: Linux/Mac (script shell)
```bash
chmod +x start_dashboard.sh
./start_dashboard.sh
```

### Option 3: Manuel
```bash
pip install -r requirements.txt
cd dashboard
python app.py
```

Puis accédez à: **http://localhost:8050**

## 🎨 Design & Features

### Couleurs
- Primaire: #667eea (bleu-violet)
- Succès: #2ca02c (vert)
- Danger: #d62728 (rouge)
- Secondaire: #ff7f0e (orange)
- Arrière-plan: #f5f7fa (gris clair)

### Filtres Globaux
- 📅 Plage de dates (DatePickerRange)
- 🚗 Type de véhicule (Dropdown multi)
- 💳 Méthode de paiement (Dropdown)
- 📊 Statut de réservation (Dropdown)

### Pages
1. 📈 **Vue d'ensemble** (`/overview`)
   - KPIs: Total, Taux complétés, Revenu, Valeur moyenne
   - Charts: Évolution mensuelle, Distribution statuts, Top véhicules

2. ⚙️ **Opérations** (`/operations`)
   - KPIs: VTAT, CTAT, Taux d'annulation
   - Charts: Distance, Durée vs Distance, Complétude, Raisons annulation

3. 💰 **Finance** (`/finance`)
   - KPIs: Revenu total, Revenu confirmé, Valeur moyenne
   - Charts: Par véhicule, Par paiement, Distribution, Revenu vs Distance

## 📈 Métriques clés

### KPIs de base
- **Total bookings**: Nombre de réservations
- **Completion rate**: % de réservations complétées
- **Cancellation rate**: % de réservations annulées
- **Total revenue**: Revenu total ($)
- **Avg ride value**: Valeur moyenne par trajet ($)

### KPIs opérationnels
- **VTAT (Vehicle Turn Around Time)**: Temps moyen entre trajets (minutes)
- **CTAT (Cancellation Time to Acceptance)**: Temps avant annulation (minutes)
- **Top cancellation reasons**: Raisons d'annulation les plus fréquentes

### KPIs financiers
- **Revenue by vehicle type**: Revenu par catégorie de véhicule
- **Revenue by payment method**: Revenu par méthode de paiement
- **Revenue vs distance correlation**: Relation prix/distance

## 🛠️ Stack technique

- **Framework**: Dash (Plotly)
- **Visualisations**: Plotly, Matplotlib
- **Data**: Pandas, NumPy
- **Web**: Python 3.13
- **CSS**: Responsive design (mobile-first)

## 📝 Conventions de code

- Noms de fichiers: `snake_case` (overview.py, finance.py)
- Noms de variables: `snake_case` (filtered_data, total_revenue)
- Noms de fonctions: `snake_case` (def layout(...))
- Noms de classes: `PascalCase` (Layout, Dashboard)
- Commentaires: En français avec emoji pour clarté

## 🔒 Structure des répertoires

```
Projet1_Dash/Uber_Rides_2024/
├── data/
│   ├── raw/
│   └── processed/
├── dashboard/              # ← Application Dash
│   ├── app.py
│   ├── assets/
│   │   └── style.css
│   └── pages/
│       ├── overview.py
│       ├── operations.py
│       └── finance.py
├── notebooks/              # ← Analysis Jupyter
│   └── Uber_Rides_2024_Project.ipynb
├── src/                    # Scripts utilitaires
├── config/
├── requirements.txt
├── DASHBOARD_README.md
├── start_dashboard.bat
└── start_dashboard.sh
```

## 🧪 Tests

Pour vérifier que tout est correctement configuré:
```bash
python test_dashboard.py
```

Cela va vérifier:
- ✓ Existence du fichier CSV
- ✓ Import des modules requis
- ✓ Chargement des données
- ✓ Import des pages du dashboard

## 🐛 Dépannage courant

| Problème | Solution |
|----------|----------|
| Port 8050 occupé | Modifier `app.py` ligne 179: `port=8051` |
| FileNotFoundError (CSV) | Vérifier le chemin: `../data/processed/ride_bookings_clean.csv` |
| ModuleNotFoundError | `pip install -r requirements.txt` |
| Pas de mise à jour des filtres | Vérifier la console pour les erreurs de callback |

## 📞 Support

Pour des problèmes:
1. Vérifier la console du navigateur (F12)
2. Vérifier la sortie du terminal Python
3. Exécuter `python test_dashboard.py`
4. Vérifier les fichiers de logs

---

**Dernière mise à jour**: 2024
**Status**: ✅ Prêt pour production
