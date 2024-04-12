#!/usr/bin/python3
"""Defines the print square function"""

def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): The size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for x in range(size):
            for y in range(size):
                print("#", end='')
            print('')
