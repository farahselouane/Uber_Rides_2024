import dash
from dash import html, dcc, Input, Output, callback
import pandas as pd
import plotly.graph_objects as go
import os

# Charger les données
import os
DATA_PATH = os.path.join(os.path.dirname(__file__), '../../data/processed/ride_bookings_clean.csv')
df = pd.read_csv(DATA_PATH)
df['date'] = pd.to_datetime(df['date'])

# Enregistrer cette page avec Dash Pages
dash.register_page(__name__, path='/')

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
    html.H2('📈 Vue d\'ensemble', className='page-title'),
    
    # Cartes KPI
    html.Div(
        className='kpi-grid',
        id='overview-kpi-grid',
        children=[
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='0', id='overview-kpi-total'),
                    html.Div(className='kpi-label', children='Total réservations')
                ]
            ),
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='0%', id='overview-kpi-completion'),
                    html.Div(className='kpi-label', children='Taux complétés')
                ]
            ),
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='$0', id='overview-kpi-revenue'),
                    html.Div(className='kpi-label', children='Revenu total')
                ]
            ),
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='$0', id='overview-kpi-avg-value'),
                    html.Div(className='kpi-label', children='Valeur moyenne')
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
                children=dcc.Graph(id='overview-monthly-chart')
            ),
            html.Div(
                className='chart-container',
                children=dcc.Graph(id='overview-status-chart')
            ),
            html.Div(
                className='chart-container',
                children=dcc.Graph(id='overview-vehicle-chart')
            ),
        ]
    ),
], style={'width': '100%', 'padding': '16px', 'boxSizing': 'border-box'})

@callback(
    [Output('overview-kpi-total', 'children'),
     Output('overview-kpi-completion', 'children'),
     Output('overview-kpi-revenue', 'children'),
     Output('overview-kpi-avg-value', 'children'),
     Output('overview-monthly-chart', 'figure'),
     Output('overview-status-chart', 'figure'),
     Output('overview-vehicle-chart', 'figure')],
    Input('filters-store', 'data')
)
def update_overview(filters):
    if not filters:
        return ('0', '0%', '$0', '$0',
                create_empty_figure('📅 Évolution mensuelle'),
                create_empty_figure('📊 Distribution des statuts'),
                create_empty_figure('🚗 Top véhicules'))
    
    filtered_df = apply_filters(df, filters)
    
    # KPIs
    total = len(filtered_df)
    completed = (filtered_df['booking_status'] == 'COMPLETED').sum()
    completion_rate = (completed / total * 100) if total > 0 else 0
    revenue = filtered_df[filtered_df['booking_status'] == 'COMPLETED']['booking_value'].sum()
    avg_value = filtered_df['booking_value'].mean() if total > 0 else 0
    
    # Graphique 1: Évolution mensuelle
    if len(filtered_df) > 0:
        monthly = filtered_df.groupby(filtered_df['date'].dt.to_period('M')).size()
        monthly.index = monthly.index.astype(str)
        fig_monthly = go.Figure(
            data=go.Scatter(
                x=monthly.index,
                y=monthly.values,
                mode='lines+markers',
                line=dict(color='#1f77b4', width=2),
                marker=dict(size=8)
            )
        )
        fig_monthly.update_layout(
            title='📅 Évolution mensuelle des réservations',
            xaxis_title='Mois',
            yaxis_title='Nombre',
            height=420,
            hovermode='x unified'
        )
    else:
        fig_monthly = create_empty_figure('📅 Évolution mensuelle')
    
    # Graphique 2: Distribution des statuts
    if len(filtered_df) > 0:
        status_dist = filtered_df['booking_status'].value_counts()
        fig_status = go.Figure(
            data=go.Bar(
                x=status_dist.index,
                y=status_dist.values,
                marker=dict(color=['#2ca02c', '#d62728', '#ff7f0e', '#9467bd'][:len(status_dist)])
            )
        )
        fig_status.update_layout(
            title='📊 Distribution des statuts',
            xaxis_title='Statut',
            yaxis_title='Nombre',
            height=420,
            hovermode='x'
        )
    else:
        fig_status = create_empty_figure('📊 Distribution des statuts')
    
    # Graphique 3: Top véhicules
    if len(filtered_df) > 0:
        top_vehicles = filtered_df['vehicle_type'].value_counts().head(5)
        fig_vehicles = go.Figure(
            data=go.Bar(
                x=top_vehicles.values,
                y=top_vehicles.index,
                orientation='h',
                marker=dict(color='#1f77b4')
            )
        )
        fig_vehicles.update_layout(
            title='🚗 Top 5 véhicules',
            xaxis_title='Nombre',
            height=420,
            hovermode='y'
        )
    else:
        fig_vehicles = create_empty_figure('🚗 Top véhicules')
    
    return (
        f'{total:,}',
        f'{completion_rate:.1f}%',
        f'${revenue:,.0f}',
        f'${avg_value:.2f}',
        fig_monthly,
        fig_status,
        fig_vehicles
    )
