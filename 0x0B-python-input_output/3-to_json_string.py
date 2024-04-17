#!/usr/bin/python3
"""A string to a JSON function."""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of a string object."""
    return json.dumps(my_obj)
