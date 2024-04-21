#!/usr/bin/python3
"""Defines the Base class"""





class Base:
    """Represents the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the Base

        Args:
            __nb_objects (int): The number of objects
            id           (int): The id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
