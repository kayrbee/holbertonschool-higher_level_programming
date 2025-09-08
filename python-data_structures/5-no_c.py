#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    return new_string.replace('c', '').replace('C', '')

# Alternative approaches:
# #  Use join
# def no_c(my_string):
#     return ''.join(ch for ch in my_string if ch not in 'cC')

# #  My original version
# def no_c(my_string):
    # for char in my_string:
    #     if (char == 'C') or (char == 'c'):
    #         continue
    #     else:
    #         new_string += char
    # return new_string

# #  Use filter
# def no_c(my_string):
#     return ''.join(filter(lambda ch: ch not in 'cC', my_string))


# Tests
# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
