#!/usr/bin/python3
"""The Student class"""


class Student:
    """The Student class defined"""

    def __init__(self, first_name, last_name, age):
        """Initialization of Student

        Args:
            first_name (str): The first name 
            last_name (str): The last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description of Student"""
        return self.__dict__
