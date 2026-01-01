import dash
from dash import dcc, html, Input, Output, State, callback
import pandas as pd
import os

# Charger les données une seule fois au démarrage
DATA_PATH = '../data/processed/ride_bookings_clean.csv'
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Le fichier {DATA_PATH} n'existe pas. Vérifiez le chemin.")

df = pd.read_csv(DATA_PATH)
df['date'] = pd.to_datetime(df['date'])

# Convertir les dates pour les filtres
min_date = df['date'].min().strftime('%Y-%m-%d')
max_date = df['date'].max().strftime('%Y-%m-%d')

# Initialiser l'app Dash avec Pages
app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[],
    pages_folder='pages'
)

# Définir le layout principal
app.layout = html.Div([
    # Navbar
    html.Div(
        className='navbar',
        children=[
            html.Div(
                className='navbar-container',
                children=[
                    html.H1('📊 TABLEAU DE BORD UBER RIDES 2024', className='navbar-title'),
                    html.Div(
                        className='navbar-links',
                        children=[
                            dcc.Link('📈 Vue d\'ensemble', href='/', className='nav-link'),
                            dcc.Link('⚙️ Opérations', href='/operations', className='nav-link'),
                            dcc.Link('💰 Finance', href='/finance', className='nav-link'),
                        ]
                    )
                ]
            )
        ]
    ),
    
    # Section des filtres
    html.Div(
        className='filter-section',
        children=[
            html.H3('🔍 FILTRES', className='filter-title'),
            html.Div(
                className='filter-grid',
                children=[
                    # Filtre date
                    html.Div(
                        className='filter-item',
                        children=[
                            html.Label('Plage de dates:', className='filter-label'),
                            dcc.DatePickerRange(
                                id='date-range-filter',
                                start_date=min_date,
                                end_date=max_date,
                                display_format='YYYY-MM-DD',
                                style={'width': '100%'}
                            )
                        ]
                    ),
                    # Filtre type de véhicule
                    html.Div(
                        className='filter-item',
                        children=[
                            html.Label('Type de véhicule:', className='filter-label'),
                            dcc.Dropdown(
                                id='vehicle-type-filter',
                                options=[{'label': 'Tous', 'value': 'ALL'}] + [
                                    {'label': v, 'value': v} for v in sorted(df['vehicle_type'].unique())
                                ],
                                value='ALL',
                                multi=False
                            )
                        ]
                    ),
                    # Filtre méthode de paiement
                    html.Div(
                        className='filter-item',
                        children=[
                            html.Label('Méthode de paiement:', className='filter-label'),
                            dcc.Dropdown(
                                id='payment-method-filter',
                                options=[{'label': 'Tous', 'value': 'ALL'}] + [
                                    {'label': str(p), 'value': str(p)} for p in sorted(df['payment_method'].dropna().unique())
                                ],
                                value='ALL',
                                multi=False
                            )
                        ]
                    ),
                    # Filtre statut de réservation
                    html.Div(
                        className='filter-item',
                        children=[
                            html.Label('Statut de réservation:', className='filter-label'),
                            dcc.Dropdown(
                                id='booking-status-filter',
                                options=[{'label': 'Tous', 'value': 'ALL'}] + [
                                    {'label': s, 'value': s} for s in sorted(df['booking_status'].unique())
                                ],
                                value='ALL',
                                multi=False
                            )
                        ]
                    ),
                ]
            ),
            # Texte de résumé
            html.Div(
                id='filter-summary',
                className='filter-summary',
                children='Données filtrées: 0 réservations'
            )
        ]
    ),
    
    # Page container (Dash Pages)
    html.Div(
        id='page-container',
        className='page-content',
        children=dash.page_container
    ),
    
    # Store pour les filtres
    dcc.Store(id='filters-store', data={
        'start_date': min_date,
        'end_date': max_date,
        'vehicle_type': 'ALL',
        'payment_method': 'ALL',
        'booking_status': 'ALL'
    })
], style={'width': '100%', 'minHeight': '100vh'})

# Callback pour mettre à jour le store des filtres
@callback(
    [Output('filters-store', 'data'),
     Output('filter-summary', 'children')],
    [Input('date-range-filter', 'start_date'),
     Input('date-range-filter', 'end_date'),
     Input('vehicle-type-filter', 'value'),
     Input('payment-method-filter', 'value'),
     Input('booking-status-filter', 'value')]
)
def update_filters(start_date, end_date, vehicle_type, payment_method, booking_status):
    # Appliquer les filtres pour compter
    filtered_df = df.copy()
    
    if start_date and end_date:
        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)
        filtered_df = filtered_df[
            (filtered_df['date'] >= start_dt) & 
            (filtered_df['date'] <= end_dt)
        ]
    
    if vehicle_type and vehicle_type != 'ALL':
        filtered_df = filtered_df[filtered_df['vehicle_type'] == vehicle_type]
    
    if payment_method and payment_method != 'ALL':
        filtered_df = filtered_df[filtered_df['payment_method'] == payment_method]
    
    if booking_status and booking_status != 'ALL':
        filtered_df = filtered_df[filtered_df['booking_status'] == booking_status]
    
    count = len(filtered_df)
    summary_text = f"✓ Données filtrées: {count:,} réservations"
    
    filters = {
        'start_date': start_date,
        'end_date': end_date,
        'vehicle_type': vehicle_type,
        'payment_method': payment_method,
        'booking_status': booking_status
    }
    
    return filters, summary_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
