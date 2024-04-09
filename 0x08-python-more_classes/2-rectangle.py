#!/usr/bin/python3
"""This is a Rectangle class"""


class Rectangle:
    """The class Rectangle defined"""
    def __init__(self, width=0, height=0):
        """Initialization of the Rectangle

        Args:
            width (int): The width of a Rectangle
            height (int): The height of a Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The method to set the width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Method that gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The method to set the height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
