"""
Simple Flask backend for testing frontend integration.
Provides a sample API route.
"""

import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from backend.admin import init_admin
from backend.constants.paths import SQLALCHEMY_DATABASE_URI
from backend.extensions import admin, db, migrate
from backend.routes.api import api
from backend.routes.task_item import task_items_bp

load_dotenv()
app = Flask(__name__)
CORS(app)  # allows frontend to fetch from a different port
app.register_blueprint(api)
app.register_blueprint(task_items_bp)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db.init_app(app)
migrate.init_app(app, db)
admin.init_app(app)
init_admin()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
