"""
Domain Type enum
"""

from enum import Enum


class DomainType(Enum):
    """
    Represents a broader category for task cards
    """

    WORK = "Work"
    LEARNING = "Learning"
    HOME = "Home"
    HEALTH = "Health"
    CREATIVE = "Creative"
    ENTERTAINMENT = "Entertainment"
    REVIEW = "Review"
