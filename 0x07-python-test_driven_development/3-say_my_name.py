#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name.

    Raises:
        TypeError: If one of the first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be styring)
    print("My name is {} {}".format(first_name, last_name))
