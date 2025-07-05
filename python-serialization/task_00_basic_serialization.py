#!/usr/bin/env python3
"""Json import"""


import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The file where data will be saved (overwrites if exists).
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file to a dictionary.

    Args:
        filename (str): The JSON file to load.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
