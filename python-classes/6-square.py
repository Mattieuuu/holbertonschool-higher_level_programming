#!/usr/bin/python3
"""Module that defines a Square class.
This module contains a class that defines a square by its size
and position, with methods to calculate area and print the square.
"""


class Square:
    """Class that defines a square.
    This class represents a square with private attributes for
    size and position, and methods to manage these properties.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.
        Args:
            size (int): Size of the square side.
            position (tuple): Position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The size to set.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        Args:
            value (tuple): The position as a tuple of 2 positive integers.
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print()
            return

        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
