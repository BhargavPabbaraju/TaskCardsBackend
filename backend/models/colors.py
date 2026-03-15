"""Models related to colors that group tasks"""

from dataclasses import dataclass
from enum import Enum


class Color(Enum):
    """Colors as enums(This is what will be used throughout backend code)"""

    RED = "Red"  # Work Related tasks / Anything with urgent looming deadlines
    BLUE = "Blue"  # Relax - Nap , Anime , Movie , etc
    PURPLE = "Purple"  # Personal learning - System design , Japanese, etc
    YELLOW = "Yellow"  # Life admin - cleaning , cooking , exercise, etc
    GREEN = "Green"  # Creative tasks - hobby programming , game dev, guitar , etc


@dataclass
class ColorModel:
    """Model of Color, used to display colors in frontend"""

    color: Color
    description: str
    fun: bool
    engaging: bool  # Whether it Requires focus

    def to_dict(self):
        """Converts to Serializable JSON version"""
        return {
            "color": self.color.value,
            "description": self.description,
            "fun": self.fun,
            "engaging": self.engaging,
        }


COLORS = [
    ColorModel(
        color=Color.RED,
        description="Work Related tasks / Anything with urgent looming deadlines",
        fun=False,
        engaging=True,
    ),
    ColorModel(
        color=Color.BLUE,
        description="Relax - Nap , Anime , Movie , etc",
        fun=True,
        engaging=False,
    ),
    ColorModel(
        color=Color.YELLOW,
        description="Life admin - cleaning , cooking , exercise, etc",
        fun=False,
        engaging=False,
    ),
    ColorModel(
        color=Color.PURPLE,
        description="Personal learning - System design , Japanese, etc",
        fun=False,
        engaging=True,
    ),
    ColorModel(
        color=Color.GREEN,
        description="Creative tasks - hobby programming , game dev, guitar , etc",
        fun=True,
        engaging=True,
    ),
]
