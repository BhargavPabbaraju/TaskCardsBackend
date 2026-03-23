"""
Path constants
"""

from pathlib import Path

SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

BACKEND_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACKEND_DIR / "data"
DAY_COMPOSITION_DIR = DATA_DIR / "day_compositions"
