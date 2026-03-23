"""Models for DayComposition"""

from dataclasses import dataclass, field

from .domain_type import DomainType
from .errors import ValidationError
from .utils import TimeWindow


@dataclass
class DomainTypeComposition:
    """Represents one domain type's contribution to a template."""

    domain_type: DomainType
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
class DayComposition:
    """Defines a particular composition of domain types for the day"""

    name: str
    composition: list[DomainTypeComposition] = field(default_factory=list)
    id: str = field(init=False)

    def __post_init__(self) -> None:
        self.id = self.name.replace(" ", "")
        for d in self.composition:
            if isinstance(d.domain_type, str):
                d.domain_type = DomainType[d.domain_type]
        self.validate()

    def validate(self) -> None:
        """Validate that all percentages sum to 100."""

        total_percentage = sum({item.percentage for item in self.composition})
        if total_percentage != 100:
            raise ValidationError(
                f"Percentages must sum to 100 (got {total_percentage})."
            )
