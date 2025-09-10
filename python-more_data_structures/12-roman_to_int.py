#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    total, prev_int = 0, 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

    for ch in roman_string:
        current_int = roman_dict.get(ch, 0)
        if current_int > prev_int:
            total += current_int - (2 * prev_int)
        else:
                total += current_int
        prev_int = current_int
    return total

# # Tests
# # 10
# roman_number = "X"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 7
# roman_number = "VII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = None
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = 2
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = ""
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 4
# roman_number = "IV"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 6
# roman_number = "VI"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 9
# roman_number = "IX"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 87
# roman_number = "LXXXVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 707
# roman_number = "DCCVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 124
# roman_number = "CXXIV"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 99
# roman_number = "XCIX"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 89
# roman_number = "LXXXIX"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# # 1900
# roman_number = "MCM"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))
