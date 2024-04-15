#!/usr/bin/python3
"""This is a BaseGeometry class"""


class BaseGeometry:
    """The class BaseGeometry defined"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validation of value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """The class Rectangle that inherits from BaseGeometry defined"""

    def __init__(self, width, height):
        """Initialization of the Rectangle

        Args:
            width (int): The width of a Rectangle
            height (int): The height of a Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def __str__(self):
        """Returns the rectangle's string representation"""
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)


class Square(Rectangle):
    """The class Square that inherits from Rectangle defined"""

    def __init__(self, size):
        """Initialization of the Square

        Args:
            size (int): The size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ The method to return the area of the  square"""
        return self.__size ** 2
