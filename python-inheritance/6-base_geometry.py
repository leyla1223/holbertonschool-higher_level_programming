#!/usr/bin/python3
"""Define BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise Exception when area is not implemented."""
        raise Exception("area() is not implemented")
