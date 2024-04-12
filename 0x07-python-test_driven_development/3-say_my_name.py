#!/usr/bin/python3
"""Defines the say my name function"""

def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str): last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {:s} {:s}'.format(first_name, last_name))
