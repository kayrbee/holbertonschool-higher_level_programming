#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_copy = my_list[:]
    list_result = []
    for item in list_copy:
        if (item % 2 == 0):
            result = 1
        else:
            result = 0
        list_result.append(result)
    return list_result

# Alternative approaches:

# # Tests
# my_list = [0, 1, 2, 3, 4, 5, 6]
# list_result = divisible_by_2(my_list)

# i = 0
# while i < len(list_result):
#     print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
#     i += 1
