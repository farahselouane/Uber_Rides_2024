"""
Application Settings
Configuration variables, paths, constants, and environment setup
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data directories
DATA_RAW_DIR = PROJECT_ROOT / 'data' / 'raw'
DATA_PROCESSED_DIR = PROJECT_ROOT / 'data' / 'processed'

# File paths
RAW_DATA_FILE = DATA_RAW_DIR / 'ride_bookings.csv'
PROCESSED_DATA_FILE = DATA_PROCESSED_DIR / 'ride_bookings_clean.csv'

# Dash configuration
DASH_THEME = 'BOOTSTRAP'  # Can be BOOTSTRAP, DARKLY, etc.
DASH_DEBUG_MODE = os.getenv('DASH_DEBUG', True)
DASH_HOST = os.getenv('DASH_HOST', '127.0.0.1')
DASH_PORT = int(os.getenv('DASH_PORT', 8050))

# Data cleaning parameters
MISSING_VALUE_STRATEGY = 'smart'
OUTLIER_METHOD = 'iqr'
IQR_MULTIPLIER = 1.5

# Visualization settings
DEFAULT_TEMPLATE = 'plotly_white'
CHART_HEIGHT = 450
CHART_FONT_SIZE = 12

# Application metadata
APP_TITLE = "Uber Rides 2024 - Analytics Dashboard"
APP_DESCRIPTION = "Comprehensive data analytics dashboard for ride booking analysis"
APP_VERSION = "1.0.0"
