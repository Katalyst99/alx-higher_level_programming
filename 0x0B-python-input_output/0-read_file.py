#!/usr/bin/python3
"""Defines the read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename (str): The filename
    """
    with open(filename, 'r', encoding='utf-8') as afile:
        for line in afile:
            print(line, end='')
