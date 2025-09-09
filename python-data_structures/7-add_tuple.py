#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    max_range = 2
    for i in range(max_range):
        item1 = tuple_a[i] if i < len(tuple_a) else 0
        item2 = tuple_b[i] if i < len(tuple_b) else 0
        if i == 0:
            result_a = (item1 + item2)
        else:
            result_b = (item1 + item2)
    result = (result_a, result_b)
    return result

# Alternative approaches:

# Tests
# tuple_a = (1, 89)
# tuple_b = (88, 11)
# new_tuple = add_tuple(tuple_a, tuple_b)
# print(new_tuple)

# print(add_tuple(tuple_a, (1, )))
# print(add_tuple(tuple_a, ()))
