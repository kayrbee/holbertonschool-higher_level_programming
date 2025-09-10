#!/usr/bin/python3
def roman_to_int(roman_string):
    integer_equivalent = 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    length = len(roman_string)
    for i in range(length):
        current_int = roman_dict.get(roman_string[i])
        if roman_string[i] == 'I' and i < (length - 1):
            if roman_string[i + 1] == 'X' or roman_string[i + 1] == 'V':
                next_int = roman_dict.get(roman_string[i + 1])
                integer_equivalent = next_int - current_int
                break
            else:
                integer_equivalent += current_int

        else:
            integer_equivalent += roman_dict.get(roman_string[i])

    return integer_equivalent

# # Tests
# roman_number = "X"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "VII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "IV"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "VI"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "IX"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "LXXXVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "DCCVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))
