#!/usr/bin/python3
"""Defines the append_file function"""


def append_file(filename="", text=""):
    """Returns the number of characters added

    Args:
        filename (str): The file name
        text (str): The string to append
    """
    with open(filename, 'a', encoding='utf-8') as afile:
        return afile.write(text)
