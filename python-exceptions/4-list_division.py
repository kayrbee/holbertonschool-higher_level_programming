#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = [0] * list_length

    for i in range(len(result_list)):
        try:
            result_list[i] = my_list_1[i] / my_list_2[i]
            # continue
        except ZeroDivisionError:
            result_list[i] = 0
            print("division by 0")
            continue
        except TypeError:
            print("wrong type")
            continue
        except IndexError:
            print("out of range")
            break
        # finally:

    return result_list

# Tests
# my_l_1 = [10, 8, 4]
# my_l_2 = [2, 4, 4]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)

# print("--")

# my_l_1 = [10, 8, 4, 4]
# my_l_2 = [2, 0, "H", 2, 7]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)
