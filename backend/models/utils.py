"""Common utility models"""

from dataclasses import dataclass


@dataclass
class TimeWindow:
    """Represents a time window with start and end times in HH:MM"""

    start: str
    end: str
