#!/usr/bin/python3
# NB: this is my original solution, which passed the checker
# def print_matrix_integer(matrix=[[]]):
#     rows, cols = 0, 0
#     size = len(matrix)
#     columns = len(matrix[0])
#     first_col = 1
#     if matrix == [[]]:
#         return print()
#     while (rows < size):
#         while (cols < columns):
#             if not first_col:
#                 print(" ", end='')
#             print("{:d}".format(matrix[rows][cols]), end='')
#             first_col = 0
#             cols += 1
#         print()
#         rows += 1
#         cols = 0
#         first_col = 1

# Alternative solution
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, val in enumerate(row):
            if i > 0:
                print(" ", end='')
            print("{:d}".format(val), end='')
        print()

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
