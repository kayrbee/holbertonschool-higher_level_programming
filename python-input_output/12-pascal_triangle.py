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

    # Control row creation
    for row in range(n):
        row_list = []
        i = row + 1
        # Control row size
        for index in range(i):
            row_list.append(1)
        triangle.append(row_list)
            # print(row_list)
            # print(triangle)
    
    return triangle