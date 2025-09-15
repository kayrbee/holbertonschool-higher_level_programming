#!/usr/bin/python3
"""
Module for class "Square"
  (based on 1-square.py)
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with optional size:
  def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception
  with the message size must be an integer
if size is less than 0, raise a ValueError exception
  with the message size must be >= 0
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
        try:
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
