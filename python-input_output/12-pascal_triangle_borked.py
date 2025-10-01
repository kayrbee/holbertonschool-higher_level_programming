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
        if row == 0:
            row_list.append(1)
            triangle.append(row_list)
        elif row == 1:
            row_list = [1, 1]
            triangle.append(row_list)           
        # Control row size
        else:
            for index in range(i):
                print(range(i))
                start_val = 1
                next_value = 1
                if index == 0:
                    row_list.append(start_val)
                elif index == 1:
                    next_value += start_val
                    row_list.append(next_value)
                else:
                    row_list.append(start_val)

            triangle.append(row_list)
    
    return triangle