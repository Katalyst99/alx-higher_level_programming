#!/usr/bin/python3
"""Defines the class Rectangle that inherits from Base"""

from models.base import Base



class Rectangle(Base):
    """Represents the Rectangle class"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the Rectangle

        Args:
            width (int): The width of object
            height (int): The height of object
            x (int): The x co-ordinate of object
            y (int): The y co-ordinate of object
            id (int): The id of object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Method that retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The method to set the width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
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
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value


    @property
    def x(self):
        """Method that gets the x co-ordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """The method to set the x co-ordinate"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Method that gets the y co-ordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """The method to set the y co-ordinate"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

     def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width
