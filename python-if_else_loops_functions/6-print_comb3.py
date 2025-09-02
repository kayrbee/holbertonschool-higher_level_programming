#!/usr/bin/python3
first = True
for i in range(0, 10):
    for j in range(1, 10):
        if j > i:
            if not first:
                print(", ", end='')
            print("{}{}".format(i, j), end='')
            first = False
print()
