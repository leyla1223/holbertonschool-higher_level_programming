#!/usr/bin/python3
"""ffffffff"""


def inherits_from(obj, a_class):
    """Return ctly an instance of a_class)."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
