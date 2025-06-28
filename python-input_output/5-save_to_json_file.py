#!/usr/bin/python3
"""Function to write an object to a file as JSON"""

import json


def save_to_json_file(my_obj, filename):
    """Writes JSON representation of my_obj to filename"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
