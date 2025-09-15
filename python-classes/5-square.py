#!/usr/bin/python3
"""
Module for class "Square"
  4-square.py
Write a class Square that defines a square by:

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception
  with the message size must be an integer
if size is less than 0, raise a ValueError exception with
  the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns
  the current square area
Public instance method: def my_print(self):
  that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
"""


class Square:
    """
    Square class

    Attributes:
      size : private

    Returns:
      nothing
    """
    __size = 0

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)

    # Getter
    @property
    def size(self):
        return self.__size

    # Setter
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
