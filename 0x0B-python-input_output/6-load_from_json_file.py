#!/usr/bin/python3
"""Defines the load_from_json_file function"""

import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”

    Args:
        filename (str): The filename
    """
    with open(filename, 'r', encoding='utf-8') as afile:
        j_file = json.loads(afile.read())
    return j_file
