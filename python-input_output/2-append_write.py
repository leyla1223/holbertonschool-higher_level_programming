#!/usr/bin/python3
"""Function to append a string to a UTF-8 text file"""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
