#!/usr/bin/python3
""" This is a Square class """


class Square:
    """ The class Square defined """
    def __init__(self, size=0):
        """ Initialization of Square

        Args:
            size (int): The size of a square
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ The method to return the area of the current square
        """
        return self.__size ** 2
