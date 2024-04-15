#!/usr/bin/python3
"""Defines the inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a_class, or False"""
    return isinstance(obj, a_class) and type(obj) is not a_class
