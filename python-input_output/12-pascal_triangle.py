#!/usr/bin/python3
"""
Create Pascal's Triangle
as a list of lists
"""

def pascal_triangle(n):
    triangle = []
    # if n <= 0 or n is not isinstance(n, int):
    if n <= 0:
        return triangle
    last_row = []

    # Control row creation
    for row_index in range(n):
        row_list = []
        row = row_index + 1
        # Control row size
        for index in range(row):
            if index == 0 or index == row_index:
                row_list.append(1)
            else:
                row_list.append(last_row[index] + last_row[index - 1])
        triangle.append(row_list)
        last_row = row_list

    return triangle
