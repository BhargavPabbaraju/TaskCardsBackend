"""
Custom errors
"""


class ValidationError(Exception):
    """Raised when a domain model fails validation."""

    def __init__(self, message: str, field: str | None = None):
        super().__init__(message)
        self.field = field
