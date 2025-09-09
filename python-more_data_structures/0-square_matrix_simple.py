#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x * x, row)))
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

#  Notes
#  This code works for a single list
# def square_matrix_simple(matrix=[]):
    # new_matrix = [1, 2, 3]
    # result = list(map(lambda x: x ** 2, new_matrix))
    # return result
