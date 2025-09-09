#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    sum = 0
    for i in new_list:
        sum += i
    return sum

# Alternative:
    # new_list = list(dict.fromkeys(my_list))

# # Tests
# my_list = [1, 2, 3, 1, 4, 2, 5]
# result = uniq_add(my_list)
# print("Result: {:d}".format(result))
