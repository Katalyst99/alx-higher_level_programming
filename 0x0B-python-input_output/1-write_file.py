#!/usr/bin/python3
"""Defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and, 
    returns the number of characters written

    Args:
        filename (str): The file name
    """
    char_number = 0
    with open(filename, 'w', encoding='utf-8') as afile:
        for line in afile:
            char_number += 1
        return char_number
