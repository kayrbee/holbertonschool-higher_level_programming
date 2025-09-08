#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element
    return new_list

# Alternative approaches:
# new_list = my_list.copy()
# //Equivalent functionality for Python 3+ but more explicit

# import copy
# new_list = copy.deepcopy(my_list)
# //Creates a deep copy which handles nested lists

# my_list = [1, 2, 3, 4, 5]
# idx = 3
# new_element = 9
# new_list = new_in_list(my_list, idx, new_element)

# print(new_list)
# print(my_list)
