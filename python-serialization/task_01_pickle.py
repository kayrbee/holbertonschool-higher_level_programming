#!/usr/bin/python3
"""
Use Pickle to convert to/from binary
"""


import pickle


class CustomObject:
    def __init__(self, name='', age='', is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        # data = vars(self)
        # for key in data:
        #     print("{}: {}".format(key, data[key]))
        # Alternative implemetation
        keys = self.__dict__.keys()
        for key in keys:
            print("{}: {}".format(key, self.__dict__[key]))

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as file:
            return pickle.load(file)
