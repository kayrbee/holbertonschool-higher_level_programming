#!/usr/bin/python3
def safe_print_integer(value):
    # print an integer with "{:d}.format()"
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False

# # Tests
# value = 89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))

# value = -89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))

# value = "School"
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
