#!/usr/bin/python3
def uppercase(str):
    for char in str:
        i = ord(char)
        if i > 96 and i < 123:
            print("{}".format(chr(i - 32)), end='')
        else:
            print(char, end='')
    print()
