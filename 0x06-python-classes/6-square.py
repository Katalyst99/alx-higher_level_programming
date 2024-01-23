#!/usr/bin/python3
""" This is a Square class """


class Square:
    """ The class Square defined """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialization of Square

        Args:
            size (int): The size of a square
            position (tuple) : The position of a square
        """
        self.size = size
        self.position = position

    def area(self):
        """ The method to return the area of the current square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Method that retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ The method to set the size """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """ The method that retrieves the position """
        return self.__position

    @position.setter
    def position(self, value):
        """" The method to set the position """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[1]) != int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """ The method that prints in stdout the square with # character """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print('')
            for x in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for y in range(self.__size):
                    print("#", end='')
                print('')
