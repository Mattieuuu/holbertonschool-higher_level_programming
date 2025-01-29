#!/usr/bin/python3
'''
Module for Class Square
'''


class Square:
    '''Class Square'''
    def __init__(self, size=0):
        self.__set_size(size)

    def __set_size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def get_size(self):
        return self.__size

    def set_size(self, value):
        self.__set_size(value)

    size = property(get_size, set_size)

    def area(self):
        '''Return area of the square.'''
        return self.__size ** 2
