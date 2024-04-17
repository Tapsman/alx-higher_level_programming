#!/usr/bin/python3
"""Function to write JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Funct to write and object to text file using JSON repreentation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
