#!/usr/bin/python3
"""Function to return Python object from JSON string"""

import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string"""
    return json.loads(my_str)
