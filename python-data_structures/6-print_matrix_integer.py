#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows, cols = 0, 0
    size = len(matrix)
    columns = len(matrix[0])
    if matrix == [[]]:
        return print()
    while (rows < size):
        while (cols < columns):
            print("{:d} ".format(matrix[rows][cols]), end='')
            cols += 1
        print()
        rows += 1
        cols = 0

# Tests
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix = [
#     [1, 2],
#     [4, 5],
#     [7, 8]
# ]

# print_matrix_integer(matrix)
# print("--")
# print_matrix_integer()
