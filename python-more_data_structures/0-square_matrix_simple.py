#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [sublist[:] for sublist in matrix]
    for row in range(len(new_matrix)):
        for element in range(len(new_matrix[row])):
            new_matrix[row][element] *= new_matrix[row][element]
    return new_matrix

# # Tests
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# new_matrix = square_matrix_simple(matrix)
# print(new_matrix)
# print(matrix)
