"""All api routes"""

from flask import Blueprint, jsonify

from backend.models import DomainType

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/domain-types")
def get_domain_types():
    """Returns list of domain types"""
    return jsonify([d.value for d in DomainType])
