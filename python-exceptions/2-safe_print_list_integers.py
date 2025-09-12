#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    length_li = 0
    for item in my_list:
        length_li += 1
    for index, item in enumerate(my_list):
        if index < x:
            try:
                print("{:d}".format(item), end='')
                counter += 1
            except TypeError:
                continue
            except ValueError:
                continue
        if x > length_li:
            raise IndexError
        

            
    print()
    return counter

