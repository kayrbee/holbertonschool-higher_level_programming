#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = []
    for i in my_list:
        new_matrix.append(replace if i == search else i)
    return new_matrix

# # Alternative:
# def search_replace(my_list, search, replace):
#     return [replace if i == search else i for i in my_list]

# # Tests
# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)

# print(new_list)
# print(my_list)
