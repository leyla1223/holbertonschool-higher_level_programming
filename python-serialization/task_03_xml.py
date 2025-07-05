#!/usr/bin/env python3
"""no json yes xml"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The output XML filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Ensure all values are stored as strings

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a dictionary.

    Args:
        filename (str): The XML file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except (FileNotFoundError, ET.ParseError):
        return None
