#!/usr/bin/python3
"""
This module contains 1 function which prints a square
"""


def print_square(size):
    """
    print_square is a function which prints # characters

    Args:
      size: number of rows and columns to print

      Returns: nothing
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')

    for i in range(size):
        string = size * '#'
        print(string)
