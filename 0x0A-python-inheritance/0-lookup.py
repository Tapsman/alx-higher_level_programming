#!/usr/bin/python3
"""lookup"""


def lookup(obj):
    """Looks up yhe object attributes and methods.

    Args:
        obj(object): The object that will be listed

    Returns:
        list: The object attributes
    """
    return dir(obj)
