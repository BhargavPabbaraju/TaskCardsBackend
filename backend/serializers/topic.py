from backend.models import DOMAIN_BY_KEY, Topic


class TopicSerializer:
    """Topic Serializer"""

    @classmethod
    def serialize(cls, topic: Topic) -> dict:
        """Serializes topic sql model into json dict"""
        domain = DOMAIN_BY_KEY[topic.domain_key]
        return {
            "id": topic.id,
            "name": topic.name,
            "description": topic.description,
            "domain": domain.to_dict(),
            "domainSortOrder": topic.domain_sort_order,
        }
