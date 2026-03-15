"""All api routes"""

from flask import Blueprint, jsonify

from backend.models.colors import COLORS

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/colors")
def get_colors():
    """Returns list of colors with their descriptions"""
    return jsonify([c.to_dict() for c in COLORS])
