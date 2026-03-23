"""
Template Loader
"""

from pathlib import Path

import yaml

from backend.constants.paths import DAY_COMPOSITION_DIR
from backend.models import DayComposition, DomainTypeComposition


class DayCompositionLoader:
    """
    Loads day compositions from yaml files
    Each file has a name and domain type composition for the day
    """

    @classmethod
    def load_all(cls):
        """
        Loads all yaml files from directory
        """
        day_compositions: dict[str, DayComposition] = {}
        for file in DAY_COMPOSITION_DIR.glob("*.yaml"):
            day_composition = cls.load_one(file)
            day_compositions[day_composition.id] = day_composition
        return day_compositions

    @classmethod
    def load_one(cls, path: Path) -> DayComposition:
        """
        Converts an individual yaml files contents into DayComposition
        """
        data = yaml.safe_load(path.read_text())

        compositions = [DomainTypeComposition(**c) for c in data.get("composition", [])]

        day_composition = DayComposition(name=data["name"], composition=compositions)
        return day_composition


print(DayCompositionLoader.load_all())
