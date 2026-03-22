"""
SQLit3 DB , SqlAlchemy migrations and Flask Admin setup
"""

from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
admin = Admin()
