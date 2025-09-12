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

# Tests
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
