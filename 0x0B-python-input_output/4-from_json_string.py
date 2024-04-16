#!/usr/bin/python3
"""Defines the from_json_string function"""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string

    Args:
        my_str (str): The JSON rep of the object
    """
    return json.loads(my_str)
