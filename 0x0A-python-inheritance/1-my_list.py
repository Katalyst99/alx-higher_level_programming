#!/usr/bin/python3
"""This a MyList class"""


class MyList(list):
    """The class that inherits from list class"""


    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
