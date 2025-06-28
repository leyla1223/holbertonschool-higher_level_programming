#!/usr/bin/python3
"""Function that returns the dictionary description for JSON serialization"""


def class_to_json(obj):
    """Return the dictionary of an object's attributes for JSON serialization"""
    return obj.__dict__
