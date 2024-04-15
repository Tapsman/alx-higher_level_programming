#!/usr/bin/python3
"""A function that adds new attributes to objects if possible"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object.

    Args:
        obj (any): Is the object to add attribute to.
        att (str) Is the name of attribute to add to obj.
        value (any): Value of att.

    Raises:
        TypeError: if the attribute cannot be adde.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
