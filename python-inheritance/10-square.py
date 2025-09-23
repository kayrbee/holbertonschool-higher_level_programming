#!/usr/bin/python3
"""
Module contains one subclass
Inherits from 7-base_geometry.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square subclass of Rectangle
    Has width == height
    """
    def __init__(self, size):
        """
        Initialise with width and height from size
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
