#!/usr/bin/python3
"""Student class module"""


class Student:
    """Student class with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student instance
        If attrs is a list of strings, only include those attributes.
        Otherwise, include all attributes."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
