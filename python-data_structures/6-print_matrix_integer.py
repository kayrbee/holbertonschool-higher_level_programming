#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    if matrix == [[]]:
        return print()
    while (i < len(matrix)):
        print(matrix[i])
        i += 1

# Alternative approaches:

# # Tests
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print_matrix_integer(matrix)
# print("--")
# print_matrix_integer()
