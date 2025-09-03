#!/usr/bin/python3
def uppercase(str):
    for char in str:
        i = ord(char)
        if i > 96 and i < 123:
            char = chr(i - 32)
        print("{}".format(char), end='')
    print()
