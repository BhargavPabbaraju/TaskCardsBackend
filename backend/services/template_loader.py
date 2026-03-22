"""
Template Loader
"""

from pathlib import Path

import yaml

from backend.constants.paths import TEMPLATES_DIR
from backend.models import DomainTypeComposition, Template


class TemplateLoader:
    """
    Loads templates from yaml files
    Each template has a name and domain type composition
    """

    @classmethod
    def load_all_templates(cls):
        """
        Loads all yaml files from TEMPLATES_DIR directory
        """
        templates: dict[str, Template] = {}
        for file in TEMPLATES_DIR.glob("*.yaml"):
            template = cls.load_template(file)
            templates[template.id] = template
        return templates

    @classmethod
    def load_template(cls, path: Path) -> Template:
        """
        Converts an individual yaml files contents into Template
        """
        data = yaml.safe_load(path.read_text())

        compositions = [DomainTypeComposition(**c) for c in data.get("composition", [])]

        template = Template(name=data["name"], composition=compositions)
        return template
