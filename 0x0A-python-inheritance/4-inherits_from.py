#!/usr/bin/python3
"""The module for inherits_from."""


def inherits_from(obj, a_class):
    """Detrmines if an object is a subclass of a class."""
    return isinstance(obj, a_class) and type(obj) != a_class
