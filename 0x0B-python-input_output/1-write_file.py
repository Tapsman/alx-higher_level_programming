#!/usr/bin/python3
"""Defines file writing function."""


def write_file(filename="", text=""):
    """Function that writes a string to UTF8 text file.

    Args:
        filename (str): Is the name of the file to write to.
        text (str): The text to write the file to
    Returns:
        Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
