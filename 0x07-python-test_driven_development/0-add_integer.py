#!/usr/bin/python3
"""Defines the add integer function"""

def add_integer(a, b=98):
    """Returns an integer: the addition of a and b"""


    """
    Args:
        a (int): first number
        b (int): second number
    """
    if type(a) is not int and type(a) is not float or a is not a:
        raise TypeError('a must be an integer')
    elif type(b) is not int and type(b) is not float or b is not b:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
