"""Models for Template"""

from dataclasses import dataclass, field

from .colors import Color
from .errors import ValidationError
from .utils import TimeWindow


@dataclass
class ColorComposition:
    """Represents one color's contribution to a template."""

    color: Color
    percentage: int
    card_count: int | None = None
    duration: int | None = None
    time_window: TimeWindow | None = None

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        """Validates that percentage is non negative and below 100"""
        if self.percentage < 0 or self.percentage > 100:
            raise ValidationError(
                f"Percentage must be between [0,100] but is {self.percentage}"
            )


@dataclass
class Template:
    """Defines a particular composition of colors for the day"""

    name: str
    composition: list[ColorComposition] = field(default_factory=list)
    id: str = field(init=False)

    def __post_init__(self) -> None:
        self.id = self.name.replace(" ", "")
        for c in self.composition:
            if isinstance(c.color, str):
                c.color = Color[c.color]
        self.validate()

    def validate(self) -> None:
        """Validate that all colors are present and percentages sum to 100."""
        colors_in_template = {item.color for item in self.composition}
        all_colors = set(Color)

        if colors_in_template != all_colors:
            raise ValidationError(
                "Template must contain exactly one composition for each color."
                + "\n"
                + f"Missing colors: ${all_colors - colors_in_template}"
            )

        total_percentage = sum({item.percentage for item in self.composition})
        if total_percentage != 100:
            raise ValidationError(
                f"Percentages must sum to 100 (got {total_percentage})."
            )
