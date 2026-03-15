"""
Simple Flask backend for testing frontend integration.
Provides a sample API route.
"""

from flask import Flask
from flask_cors import CORS

from backend.routes.api import api

app = Flask(__name__)
CORS(app)  # allows frontend to fetch from a different port
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
