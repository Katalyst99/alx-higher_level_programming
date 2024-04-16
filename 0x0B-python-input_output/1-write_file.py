#!/usr/bin/python3
"""Defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and, 
    returns the number of characters written

    Args:
        filename (str): The file name
    """
    with open(filename, 'w', encoding='utf-8') as afile:
        return afile.write(text)
