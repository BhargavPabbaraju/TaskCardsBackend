"""Admin setup"""

from backend.extensions import admin, db
from backend.models import TaskItem, Topic

from .task_item import TaskItemAdmin
from .topic import TopicAdmin


def init_admin():
    """Initialize Flask admin with admin views"""
    admin.add_view(TopicAdmin(Topic, db.session))
    admin.add_view(TaskItemAdmin(TaskItem, db.session))
