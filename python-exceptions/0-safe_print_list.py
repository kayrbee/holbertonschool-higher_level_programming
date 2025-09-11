#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for index, item in enumerate(my_list):
        if index < x:
            try:
                print("{}".format(item), end='')
                counter += 1
            except IndexError:
                print("x larger than length my_list")
    print()
    return counter
