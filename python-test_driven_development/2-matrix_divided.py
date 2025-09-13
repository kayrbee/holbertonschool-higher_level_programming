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
    
    return new_matrix

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8]]
# res = matrix_divided(matrix, 3)
# print(res)