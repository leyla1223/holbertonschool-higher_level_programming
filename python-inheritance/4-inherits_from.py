#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherits from a_class (but not if obj is exactly an instance of a_class)."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
