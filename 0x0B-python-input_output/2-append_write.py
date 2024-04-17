#!/usr/bin/python3
"""Defines file writing function."""


def append_write(filename="", text=""):
    """Function that appends a string to UTF8 text file.

    Args:
        filename (str): Is the name of the file to append.
        text (str): The string to append the file to
    Returns:
        Number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
