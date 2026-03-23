"""Task Item Admin views"""

from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from flask_admin.model.form import InlineFormAdmin

from backend.models.task_item import TaskChecklistItem, TaskLink


class TaskChecklistItemInline(InlineFormAdmin):
    """TaskChecklistItem AdminView , displayed inline in the TaskItemAdminView"""

    form_columns = ["id", "sort_order", "text"]


class TaskLinkInline(InlineFormAdmin):
    """TaskLink AdminView , displayed inline in the TaskItemAdminView"""

    form_columns = ["id", "sort_order", "label", "url"]


class TaskItemAdmin(ModelView):
    """TaskItemAdminView"""

    column_list = [
        "id",
        "topic",
        "topic_sort_order",
        "min_energy",
        "est_mins",
        "is_active",
    ]

    column_labels = {
        "topic": "Topic",
        "topic_sort_order": "Topic Sort order",
        "min_energy": "Min Energy",
        "est_mins": "Est. Minutes",
        "is_active": "Is Active?",
    }

    column_filters = [
        "min_energy",
        "is_active",
    ]

    column_searchable_list = [
        "description",
    ]

    form_columns = [
        "topic",
        "topic_sort_order",
        "min_energy",
        "est_mins",
        "description",
        "checklist_items",
        "links",
        "is_active",
    ]

    inline_models = [
        TaskChecklistItemInline(TaskChecklistItem),
        TaskLinkInline(TaskLink),
    ]

    form_rules = [
        rules.FieldSet(
            [
                "topic",
                "topic_sort_order",
                "min_energy",
                "est_mins",
                "description",
                "is_active",
            ],
            "Task Item",
        ),
        rules.FieldSet(["checklist_items"], "Checklist"),
        rules.FieldSet(["links"], "Links"),
    ]
