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
    row_size_check = 0

    for row in matrix:
        if len(row) != len(matrix[0]):
            row_size_check = 1

    if row_size_check == 1:
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for row in matrix:
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of"
                    " integers/floats")

    result = [[round(matrix[i][j] / div, 2) for j in range(len(matrix[0]))]
              for i in range(len(matrix))]
    return result
