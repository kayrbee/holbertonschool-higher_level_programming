#!/usr/bin/python3
"""
Module for class "Square"
  5-square.py
Write a class Square that defines a square by:

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError 
exception with the message size must be an integer
if size is less than 0, raise a ValueError exception
 with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise
 raise a TypeError exception with the message position
 must be a tuple of 2 positive integers
Instantiation with optional size and optional position:
 def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self):
 that returns the current square area
Public instance method: def my_print(self):
 that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be set using space 
- Don’t fill lines by spaces when position[1] > 0
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
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

# attribute 'size'
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

# attribute 'position'
    # Getter
    @property
    def position(self):
        return self.__position

    # Setter
    @position.setter
    def position(self, value):
        # if not isinstance(value, tuple):
        #     raise TypeError("position must be a tuple of 2 positive integers")
        # if len(value) != 2:
        #     raise TypeError("position must be a tuple of 2 positive integers")
        # if type(value[0]) is not int or type(value[1]) is not int:
        #     raise TypeError("position must be a tuple of 2 positive integers")
        # self.__position = value
        if (not isinstance(value, tuple) or len(value) != 2
             or not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value
