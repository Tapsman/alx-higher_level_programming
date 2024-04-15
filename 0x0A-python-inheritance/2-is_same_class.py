#!/usr/bin/python3
"""This is the module for is_same_class meth."""


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of a class."""
    return type(obj) == a_class
