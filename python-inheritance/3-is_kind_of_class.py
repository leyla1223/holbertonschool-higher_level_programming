#!/usr/bin/python3
"""hdhd"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass of a_class."""
    return isinstance(obj, a_class)
