#!/usr/bin/python3
"""
Module for class "Square"
  3-square.py
Write a class Square that defines a square by:

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError
 exception with the message size must be an integer
if size is less than 0, raise a ValueError exception
with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module
Why?

Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we
 control the type and value.
Getter and setter methods are not 100% Python, but more OOP.
With them, you will be able to validate the assignment
 of a private attribute and also
 define how getting the attribute value will be available from outside
  - by copy? by assignment? etc.
 Also, adding type/value validation in the setter will centralize the logic,
   since you will do it in only one place.
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
