"""TaskItemSerializer"""

from backend.models import DOMAIN_BY_KEY, TaskItem, Topic

from .topic import TopicSerializer


class TaskItemSerializer:
    """TaskItemSerializer"""

    @classmethod
    def serialize(cls, task_item: TaskItem) -> dict:
        """Convert TaskItem model to API response dict."""
        topic: Topic = task_item.topic
        domain = DOMAIN_BY_KEY[topic.domain_key]

        return {
            "id": task_item.id,
            "topic": TopicSerializer.serialize(topic),
            "domain": domain.to_dict(),
            "description": task_item.description,
            "topicSortOrder": task_item.topic_sort_order,
            "minEnergy": task_item.min_energy.name if task_item.min_energy else None,
            "estMins": task_item.est_mins,
            "isActive": task_item.is_active,
            "checklistItems": [
                {
                    "id": item.id,
                    "text": item.text,
                    "sortOrder": item.sort_order,
                }
                for item in task_item.checklist_items
            ],
            "links": [
                {
                    "id": link.id,
                    "label": link.label,
                    "url": link.url,
                    "sortOrder": link.sort_order,
                }
                for link in task_item.links
            ],
        }
