#!/usr/bin/python3
""" This is a Rectangle class """


class Rectangle:
    """ The class Rectangle defined """
    def __init__(self, width=0, height=0):
        """ Initialization of the Rectangle

        Args:
            width (int): The width of a rectangle
            height (int) : The height of a rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Gets the width of the rectangle object"""
            return self.__width

        @width.setter
        def width(self, value):
            """ The method to set the width """
            if type(value) != int:
                raise TypeError('width must be an integer')
            elif value < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value

        @property
        def height(self):
            """Method that retrieves the height"""
            return self.__height

        @height.setter
        def height(self, value):
            """ The method to set the height """
            if type(value) != int:
                raise TypeError('height must be an integer')
            elif value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
