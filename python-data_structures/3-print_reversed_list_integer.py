#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    while i > 0:
        print("{:d}".format(my_list[i - 1]))
        i -= 1

# Alternative approaches:
    # Use list slicing
    # for num in my_list[::-1]:
    #     print("{:d}".format(num))
    # 
    # Use reversed() in-built method
    # for num in reversed(my_list):
    # print("{:d}".format(num))