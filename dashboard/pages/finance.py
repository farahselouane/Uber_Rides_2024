import dash
from dash import html, dcc, Input, Output, callback
import pandas as pd
import plotly.graph_objects as go

# Charger les données
import os
DATA_PATH = os.path.join(os.path.dirname(__file__), '../../data/processed/ride_bookings_clean.csv')
df = pd.read_csv(DATA_PATH)
df['date'] = pd.to_datetime(df['date'])

# Enregistrer cette page avec Dash Pages
dash.register_page(__name__, path='/finance')

def apply_filters(df, filters):
    """Appliquer les filtres au dataframe"""
    filtered_df = df.copy()
    
    if filters.get('start_date') and filters.get('end_date'):
        start_dt = pd.to_datetime(filters['start_date'])
        end_dt = pd.to_datetime(filters['end_date'])
        filtered_df = filtered_df[
            (filtered_df['date'] >= start_dt) & 
            (filtered_df['date'] <= end_dt)
        ]
    
    if filters.get('vehicle_type') and filters['vehicle_type'] != 'ALL':
        filtered_df = filtered_df[filtered_df['vehicle_type'] == filters['vehicle_type']]
    
    if filters.get('payment_method') and filters['payment_method'] != 'ALL':
        filtered_df = filtered_df[filtered_df['payment_method'] == filters['payment_method']]
    
    if filters.get('booking_status') and filters['booking_status'] != 'ALL':
        filtered_df = filtered_df[filtered_df['booking_status'] == filters['booking_status']]
    
    return filtered_df

def create_empty_figure(title):
    """Créer une figure vide avec message"""
    fig = go.Figure()
    fig.add_annotation(
        text="Aucune donnée pour les filtres sélectionnés",
        showarrow=False,
        font=dict(size=14, color='gray')
    )
    fig.update_layout(
        title=title,
        height=420,
        xaxis_visible=False,
        yaxis_visible=False
    )
    return fig

layout = html.Div([
    html.H2('💰 Analyse financière', className='page-title'),
    
    # KPIs
    html.Div(
        className='kpi-grid',
        children=[
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='$0', id='finance-kpi-total-revenue'),
                    html.Div(className='kpi-label', children='Revenu total')
                ]
            ),
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='$0', id='finance-kpi-avg-value'),
                    html.Div(className='kpi-label', children='Valeur moyenne')
                ]
            ),
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='0', id='finance-kpi-completed'),
                    html.Div(className='kpi-label', children='Trajets complétés')
                ]
            ),
        ]
    ),
    
    # Graphiques
    html.Div(
        className='charts-grid',
        children=[
            html.Div(
                className='chart-container',
                children=dcc.Graph(id='finance-vehicle-revenue-chart')
            ),
            html.Div(
                className='chart-container',
                children=dcc.Graph(id='finance-payment-chart')
            ),
            html.Div(
                className='chart-container',
                children=dcc.Graph(id='finance-value-dist-chart')
            ),
            html.Div(
                className='chart-container',
                children=dcc.Graph(id='finance-distance-value-chart')
            ),
        ]
    ),
], style={'width': '100%', 'padding': '16px', 'boxSizing': 'border-box'})

@callback(
    [Output('finance-kpi-total-revenue', 'children'),
     Output('finance-kpi-avg-value', 'children'),
     Output('finance-kpi-completed', 'children'),
     Output('finance-vehicle-revenue-chart', 'figure'),
     Output('finance-payment-chart', 'figure'),
     Output('finance-value-dist-chart', 'figure'),
     Output('finance-distance-value-chart', 'figure')],
    Input('filters-store', 'data')
)
def update_finance(filters):
    if not filters:
        return ('$0', '$0', '0',
                create_empty_figure('🚗 Revenu par type véhicule'),
                create_empty_figure('💳 Revenu par mode paiement'),
                create_empty_figure('📊 Distribution des valeurs'),
                create_empty_figure('📈 Distance vs Valeur'))
    
    filtered_df = apply_filters(df, filters)
    
    # KPIs
    total_revenue = filtered_df['booking_value'].sum()
    avg_value = filtered_df['booking_value'].mean()
    completed = (filtered_df['booking_status'] == 'COMPLETED').sum()
    
    # Graphique 1: Revenu par type véhicule
    if len(filtered_df) > 0 and 'vehicle_type' in filtered_df.columns:
        revenue_by_vehicle = filtered_df.groupby('vehicle_type')['booking_value'].sum().sort_values(ascending=True)
        if len(revenue_by_vehicle) > 0:
            fig_vehicle = go.Figure(
                data=go.Bar(
                    y=revenue_by_vehicle.index,
                    x=revenue_by_vehicle.values,
                    orientation='h',
                    marker=dict(color='#1f77b4')
                )
            )
            fig_vehicle.update_layout(
                title='🚗 Revenu par type véhicule',
                xaxis_title='Revenu ($)',
                height=420,
                hovermode='y'
            )
        else:
            fig_vehicle = create_empty_figure('🚗 Revenu par type véhicule')
    else:
        fig_vehicle = create_empty_figure('🚗 Revenu par type véhicule')
    
    # Graphique 2: Revenu par mode paiement
    if len(filtered_df) > 0 and 'payment_method' in filtered_df.columns:
        revenue_by_payment = filtered_df.groupby('payment_method')['booking_value'].sum().sort_values(ascending=True)
        if len(revenue_by_payment) > 0:
            fig_payment = go.Figure(
                data=go.Bar(
                    y=revenue_by_payment.index,
                    x=revenue_by_payment.values,
                    orientation='h',
                    marker=dict(color='#2ca02c')
                )
            )
            fig_payment.update_layout(
                title='💳 Revenu par mode paiement',
                xaxis_title='Revenu ($)',
                height=420,
                hovermode='y'
            )
        else:
            fig_payment = create_empty_figure('💳 Revenu par mode paiement')
    else:
        fig_payment = create_empty_figure('💳 Revenu par mode paiement')
    
    # Graphique 3: Distribution des valeurs de réservation
    if len(filtered_df) > 0:
        fig_value_dist = go.Figure(
            data=go.Histogram(
                x=filtered_df['booking_value'],
                nbinsx=30,
                marker=dict(color='#ff7f0e')
            )
        )
        fig_value_dist.update_layout(
            title='📊 Distribution des valeurs de réservation',
            xaxis_title='Valeur ($)',
            yaxis_title='Nombre',
            height=420
        )
    else:
        fig_value_dist = create_empty_figure('📊 Distribution des valeurs')
    
    # Graphique 4: Scatter Distance vs Valeur
    if len(filtered_df) > 0:
        fig_scatter = go.Figure(
            data=go.Scatter(
                x=filtered_df['ride_distance'],
                y=filtered_df['booking_value'],
                mode='markers',
                marker=dict(
                    size=6,
                    color=filtered_df['booking_value'],
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title='Valeur ($)')
                ),
                text=filtered_df['vehicle_type'],
                hovertemplate='<b>%{text}</b><br>Distance: %{x:.1f}km<br>Valeur: $%{y:.2f}<extra></extra>'
            )
        )
        fig_scatter.update_layout(
            title='📈 Distance vs Valeur de réservation',
            xaxis_title='Distance (km)',
            yaxis_title='Valeur ($)',
            height=420,
            hovermode='closest'
        )
    else:
        fig_scatter = create_empty_figure('📈 Distance vs Valeur')
    
    return (
        f'${total_revenue:,.0f}',
        f'${avg_value:.2f}',
        f'{completed}',
        fig_vehicle,
        fig_payment,
        fig_value_dist,
        fig_scatter
    )
