#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print("Pre-conversion")
print(type(m))
print(m)
print("---", "Post-conversion", sep='\n')

mj = class_to_json(m)
print(type(mj))
print(mj)