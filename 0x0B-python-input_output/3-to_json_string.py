#!/usr/bin/python3
"""Defines the to_json_string function"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object

    Args:
        my_obj (str): The JSON rep of the object
    """
    return json.dumps(my_obj)
