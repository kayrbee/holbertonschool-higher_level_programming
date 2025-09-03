#!/usr/bin/python3
def fizzbuzz():
    first = True
    for i in range(1, 101):
        if not first:
            print(" ", end='')
        first = False
        if ((i % 3 == 0) and (i % 5 == 0)):
            i = "FizzBuzz"
        elif (i % 3 == 0):
            i = "Fizz"
        elif (i % 5 == 0):
            i = "Buzz"
        print("{}".format(i), end='')
    print()
