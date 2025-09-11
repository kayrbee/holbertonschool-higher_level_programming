#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for index, item in enumerate(my_list):
        if index < x:
            try:
                print("item: {} ".format(item), end='')
                counter += 1
            except IndexError:
                print("x larger than length my_list")
    print()
    return counter

# # Tests
# my_list = [1, 2, 3, 4, 5]

# nb_print = safe_print_list(my_list, 2)
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))
