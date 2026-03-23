"""Task item api routes"""

from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload, selectinload

from backend.models import TaskItem
from backend.serializers import TaskItemSerializer

task_items_bp = Blueprint("task_items_api", __name__, url_prefix="/api/task-items")


@task_items_bp.get("")
def list_task_items():
    """Returns list of all task items"""
    query = TaskItem.query.options(
        joinedload(TaskItem.topic),
        selectinload(TaskItem.checklist_items),
        selectinload(TaskItem.links),
    )

    topic_id = request.args.get("topic_id", type=int)
    if topic_id is not None:
        query = query.filter(TaskItem.topic_id == topic_id)

    is_active = request.args.get("is_active", type=str)
    if is_active == "true":
        query = query.filter(TaskItem.is_active.is_(True))
    elif is_active == "false":
        query = query.filter(TaskItem.is_active.is_(False))

    task_items = query.order_by(
        TaskItem.topic_id, TaskItem.topic_sort_order, TaskItem.id
    ).all()

    return jsonify([TaskItemSerializer.serialize(item) for item in task_items])
