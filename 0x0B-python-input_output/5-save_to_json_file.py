#!/usr/bin/python3
"""Defines the save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (str): The JSON rep of the object
        filename (str): The filename
    """
    with open(filename, 'w', encoding='utf-8') as afile:
        j_file = json.dumps(my_obj)
        afile.write(j_file)
