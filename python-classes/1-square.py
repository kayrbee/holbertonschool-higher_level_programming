#!/usr/bin/python3
"""
Module for class "Square"
  (based on 0-square.py)
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)

Why?

Why size is private attribute?

The size of a square is crucial for a square, many things depend on it
(area computation, etc.), so you, as class builder, must control the type and
value of this attribute. One way to have the control is to keep it privately.
You will see in next tasks how to get, update and validate the size value.
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

    def __init__(self, size):
        self.__size = size
