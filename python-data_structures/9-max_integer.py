#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = my_list[:]
    if new_list == []:
        return "None"
    else:
        new_list.sort()
        return new_list[-1]

# Alternative approaches:

# Tests
# my_list = [1, 90, 2, 13, 34, 5, -13, 3]
# # my_list = []
# max_value = max_integer(my_list)
# print("Max: {}".format(max_value))
