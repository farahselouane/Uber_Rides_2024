"""
Visualization Module
Contains reusable functions for creating Plotly visualizations
Used by the Dash dashboard and standalone analysis scripts
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import Optional, Dict, List


def create_time_series_plot(df: pd.DataFrame, 
                            date_col: str, 
                            value_col: str,
                            title: str = "Time Series") -> go.Figure:
    """
    Create interactive time series line plot.
    
    Args:
        df: Input DataFrame
        date_col: Name of datetime column
        value_col: Name of value column to plot
        title: Plot title
        
    Returns:
        Plotly Figure object
    """
    pass


def create_distribution_plot(df: pd.DataFrame,
                            column: str,
                            plot_type: str = 'histogram') -> go.Figure:
    """
    Create distribution plot (histogram or KDE).
    
    Args:
        df: Input DataFrame
        column: Column to visualize
        plot_type: 'histogram' or 'kde'
        
    Returns:
        Plotly Figure object
    """
    pass


def create_correlation_heatmap(df: pd.DataFrame) -> go.Figure:
    """
    Create correlation heatmap for numerical columns.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Plotly Figure object
    """
    pass


def create_categorical_summary(df: pd.DataFrame,
                               category_col: str,
                               value_col: str,
                               plot_type: str = 'bar') -> go.Figure:
    """
    Create categorical summary plot (bar, box, violin, etc.).
    
    Args:
        df: Input DataFrame
        category_col: Categorical column
        value_col: Numerical value column
        plot_type: Type of plot
        
    Returns:
        Plotly Figure object
    """
    pass


def create_geographic_plot(df: pd.DataFrame,
                          lat_col: str,
                          lon_col: str,
                          color_col: Optional[str] = None) -> go.Figure:
    """
    Create geographic scatter map (if location data available).
    
    Args:
        df: Input DataFrame with geographic data
        lat_col: Latitude column name
        lon_col: Longitude column name
        color_col: Optional column for color coding
        
    Returns:
        Plotly Figure object
    """
    pass


def create_dashboard_card(metric_value: float,
                         metric_name: str,
                         metric_unit: str = "") -> Dict:
    """
    Create data for KPI card display.
    
    Args:
        metric_value: Numerical metric value
        metric_name: Name of the metric
        metric_unit: Unit of measurement
        
    Returns:
        Dictionary with formatted metric data
    """
    pass
