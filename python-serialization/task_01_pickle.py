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
        if not filename:
            return None
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
                return True
        except (pickle.PicklingError, TypeError, AttributeError) as e:
            print(f"[Serialisation Error] Failed to serialise object: {e}")
        except (IOError, OSError) as e:
            print(f"[Serialisation Error] file error with '{filename}'")

    @classmethod
    def deserialize(cls, filename):
        if not filename:
            return None
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if not isinstance(obj, cls):
                    raise TypeError("Deserialised object is \
                                    not of type {cls.__name__}")
                return obj
        except (pickle.UnpicklingError, EOFError, TypeError, AttributeError) as e:
            print(f"[Deserialisation Error] Malformed \
                  file '{filename}': {e}")
            return None
        except FileNotFoundError:
            print(f"[Deserialisation Error] File not found: \
                  '{filename}'")
            return None
