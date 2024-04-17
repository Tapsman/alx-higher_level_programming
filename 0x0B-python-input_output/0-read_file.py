#!/usr/bin/python3
"""It Defines a text file-reading function."""


def read_file(filename=""):
    """Function to print the contents of a UTF8 file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
