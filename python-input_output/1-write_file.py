#!/usr/bin/python3
"""Function to write a string to a UTF-8 text file"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text ber of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
