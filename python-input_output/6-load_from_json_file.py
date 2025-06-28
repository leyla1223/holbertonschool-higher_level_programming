#!/usr/bin/python3
"""Function to load an object from a JSON file"""

import json


def load_from_json_file(filename):
    """Creates an object from JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
