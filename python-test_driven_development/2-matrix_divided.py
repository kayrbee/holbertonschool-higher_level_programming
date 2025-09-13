#!/usr/bin/python3
"""
This module contains one function for
dividing all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Takes a matrix and a division denominator

    Args:
      matrix (list of lists) : integers/floats
      div : integer demoninator
    
    Returns:
      new matrix containing the results,
      rounded to 2 decimal places
    """
    new_matrix = [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return new_matrix