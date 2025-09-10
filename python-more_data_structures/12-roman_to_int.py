#!/usr/bin/python3
def roman_to_int(roman_string):
    # Create a dict of roman numerals and their integer equivalent
    # Compare each character in roman_string to dict key
    #   Won't work for pattern matching 9!
    # Add dict value
    integer_equivalent = 0
    roman_dict = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    length = len(roman_string)
    for i in range(length):
        # integer_equivalent += roman_dict.get(roman_string[i])
        current_int = roman_dict.get(roman_string[i])
        # if roman_string[i] == 'I' and roman_string[i + 1] == 'X':
        if roman_string[i] == 'I':
            integer_equivalent = roman_dict.get(roman_string[i + 1]) - current_int
            break
        else:
            integer_equivalent += roman_dict.get(roman_string[i])

    return integer_equivalent

# Tests
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "LXXXVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "DCCVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))