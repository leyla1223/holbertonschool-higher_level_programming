#!/usr/bin/python3
"""Define BaseGeometry class with area and integer_validator methods."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise Exception when area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
