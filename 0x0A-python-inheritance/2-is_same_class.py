#!/usr/bin/python3
"""Defines the is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance, or False"""
    return type(obj) is a_class
