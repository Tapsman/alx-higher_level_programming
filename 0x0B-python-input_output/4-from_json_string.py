#!/usr/bin/python3
"""JSON to object function."""
import json


def from_json_string(my_str):
    """function to return the Python object representation to a JSON string."""
    return json.loads(my_str)
