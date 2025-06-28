#!/usr/bin/python3
"""ffffffff"""


def inherits_from(obj, a_class):
    """Return True if obj is an i_class (but not if obj is exactly an instance of a_class)."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
