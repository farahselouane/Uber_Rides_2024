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
dash.register_page(__name__, path='/operations')

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
    html.H2('⚙️ Analyse opérationnelle', className='page-title'),
    
    # KPIs
    html.Div(
        className='kpi-grid',
        children=[
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='0m', id='ops-kpi-vtat'),
                    html.Div(className='kpi-label', children='VTAT moyen')
                ]
            ),
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='0m', id='ops-kpi-ctat'),
                    html.Div(className='kpi-label', children='CTAT moyen')
                ]
            ),
            html.Div(
                className='kpi-card',
                children=[
                    html.Div(className='kpi-value', children='0%', id='ops-kpi-cancel-rate'),
                    html.Div(className='kpi-label', children='Taux annulation')
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
                children=dcc.Graph(id='ops-cancel-reasons-chart')
            ),
            html.Div(
                className='chart-container',
                children=dcc.Graph(id='ops-hour-chart')
            ),
            html.Div(
                className='chart-container',
                children=dcc.Graph(id='ops-distance-chart')
            ),
            html.Div(
                className='chart-container',
                children=dcc.Graph(id='ops-incomplete-chart')
            ),
        ]
    ),
], style={'width': '100%', 'padding': '16px', 'boxSizing': 'border-box'})

@callback(
    [Output('ops-kpi-vtat', 'children'),
     Output('ops-kpi-ctat', 'children'),
     Output('ops-kpi-cancel-rate', 'children'),
     Output('ops-cancel-reasons-chart', 'figure'),
     Output('ops-hour-chart', 'figure'),
     Output('ops-distance-chart', 'figure'),
     Output('ops-incomplete-chart', 'figure')],
    Input('filters-store', 'data')
)
def update_operations(filters):
    if not filters:
        return ('0m', '0m', '0%',
                create_empty_figure('❌ Raisons annulation client'),
                create_empty_figure('⏰ Réservations par heure'),
                create_empty_figure('🛣️ Distribution distances'),
                create_empty_figure('📍 Trajets incomplets'))
    
    filtered_df = apply_filters(df, filters)
    
    # KPIs
    total = len(filtered_df)
    vtat_avg = filtered_df[filtered_df['booking_status'] == 'COMPLETED']['vtat'].mean() if 'vtat' in filtered_df.columns and total > 0 else 0
    ctat_avg = filtered_df[filtered_df['booking_status'].isin(['CANCELLED BY CUSTOMER', 'CANCELLED BY DRIVER'])]['ctat'].mean() if 'ctat' in filtered_df.columns and total > 0 else 0
    
    cancelled = filtered_df['booking_status'].isin(['CANCELLED BY CUSTOMER', 'CANCELLED BY DRIVER', 'NO DRIVER FOUND']).sum()
    cancel_rate = (cancelled / total * 100) if total > 0 else 0
    
    # Graphique 1: Raisons annulation client
    if 'cancellation_reason' in filtered_df.columns and len(filtered_df) > 0:
        cancel_by_cust = filtered_df[filtered_df['booking_status'] == 'CANCELLED BY CUSTOMER']['cancellation_reason'].value_counts().head(5)
        if len(cancel_by_cust) > 0:
            fig_reasons = go.Figure(
                data=go.Bar(
                    x=cancel_by_cust.values,
                    y=cancel_by_cust.index,
                    orientation='h',
                    marker=dict(color='#d62728')
                )
            )
            fig_reasons.update_layout(
                title='❌ Top raisons annulation client',
                xaxis_title='Nombre',
                height=420,
                hovermode='y'
            )
        else:
            fig_reasons = create_empty_figure('❌ Raisons annulation client')
    else:
        fig_reasons = create_empty_figure('❌ Raisons annulation client')
    
    # Graphique 2: Réservations par heure
    if len(filtered_df) > 0 and 'request_time' in filtered_df.columns:
        df_copy = filtered_df.copy()
        df_copy['hour'] = pd.to_datetime(df_copy['request_time']).dt.hour
        hourly = df_copy.groupby('hour').size()
        fig_hour = go.Figure(
            data=go.Bar(
                x=hourly.index,
                y=hourly.values,
                marker=dict(color='#ff7f0e')
            )
        )
        fig_hour.update_layout(
            title='⏰ Réservations par heure',
            xaxis_title='Heure du jour',
            yaxis_title='Nombre',
            height=420
        )
    else:
        fig_hour = create_empty_figure('⏰ Réservations par heure')
    
    # Graphique 3: Distribution distances
    if len(filtered_df) > 0 and 'ride_distance' in filtered_df.columns:
        fig_distance = go.Figure(
            data=go.Histogram(
                x=filtered_df['ride_distance'],
                nbinsx=30,
                marker=dict(color='#2ca02c')
            )
        )
        fig_distance.update_layout(
            title='🛣️ Distribution des distances',
            xaxis_title='Distance (km)',
            yaxis_title='Nombre',
            height=420
        )
    else:
        fig_distance = create_empty_figure('🛣️ Distribution distances')
    
    # Graphique 4: Trajets incomplets
    if len(filtered_df) > 0:
        incomplete = filtered_df[~filtered_df['booking_status'].isin(['COMPLETED', 'CANCELLED BY CUSTOMER', 'CANCELLED BY DRIVER', 'NO DRIVER FOUND'])].shape[0]
        completed_count = (filtered_df['booking_status'] == 'COMPLETED').sum()
        cancelled_count = cancelled
        
        incomplete_data = pd.Series({
            'Complétés': completed_count,
            'Annulés': cancelled_count,
            'Autres': incomplete
        })
        
        fig_incomplete = go.Figure(
            data=go.Pie(
                labels=incomplete_data.index,
                values=incomplete_data.values,
                marker=dict(colors=['#2ca02c', '#d62728', '#ff7f0e'])
            )
        )
        fig_incomplete.update_layout(
            title='📍 État des réservations',
            height=420
        )
    else:
        fig_incomplete = create_empty_figure('📍 Trajets incomplets')
    
    return (
        f'{vtat_avg:.1f}m',
        f'{ctat_avg:.1f}m',
        f'{cancel_rate:.1f}%',
        fig_reasons,
        fig_hour,
        fig_distance,
        fig_incomplete
    )
