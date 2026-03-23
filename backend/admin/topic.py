"""
Topic Admin view setup
"""

from flask_admin.contrib.sqla import ModelView
from wtforms import SelectField

from backend.models import DOMAIN_BY_KEY, DOMAINS

DOMAIN_CHOICES = [(domain.key, domain.name) for domain in DOMAINS]


class TopicAdmin(ModelView):
    """Topic Admin View"""

    column_list = [
        "id",
        "domain_key",
        "domain_sort_order",
        "name",
        "description",
        "is_active",
    ]
    column_labels = {
        "domain_key": "Domain",
        "domain_sort_order": "Domain sort order",
    }
    column_filters = ["domain_key", "is_active"]
    column_searchable_list = ["name", "description"]

    form_columns = [
        "domain_key",
        "domain_sort_order",
        "name",
        "description",
        "is_active",
    ]

    form_overrides = {
        "domain_key": SelectField,
    }

    form_args = {
        "domain_key": {
            "choices": DOMAIN_CHOICES,
            "coerce": str,
        }
    }

    def _domain_name(self, _, model):
        return DOMAIN_BY_KEY.get(model.domain_key, model.domain_key).name

    column_formatters = {
        "domain_key": _domain_name,
    }
