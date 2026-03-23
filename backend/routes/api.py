"""All api routes"""

from flask import Blueprint, jsonify, request

from backend.models import DOMAINS, DomainType, Topic
from backend.serializers import TopicSerializer

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/domain-types")
def get_domain_types():
    """Returns list of domain types"""
    return jsonify([d.value for d in DomainType])


@api.route("/domains")
def get_domains():
    """Returns list of domains"""
    return jsonify([d.to_dict() for d in DOMAINS])


@api.route("/topics")
def get_topics():
    """Returns list of all task items"""
    query = Topic.query
    topic_id = request.args.get("id", type=int)
    if topic_id is not None:
        query = query.filter(Topic.id == topic_id)

    domain_key = request.args.get("domain", type=str)
    if domain_key is not None:
        query = query.filter(Topic.domain_key == domain_key)

    topics = query.order_by(Topic.domain_key, Topic.domain_sort_order, Topic.id).all()
    return jsonify([TopicSerializer.serialize(topic) for topic in topics])
