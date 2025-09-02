#!/usr/bin/python3

for i in range(0, 10):
    for j in range(1, 10):
        if j > i and not i == 8:
            print("{}{}".format(i, j), end=', ')
print("{}{}".format(i - 1, j))
