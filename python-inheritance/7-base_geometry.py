#!/usr/bin/python3
"""
Module contains one class
Builds on 5-base_geometry.py
"""


class BaseGeometry:
    """
    Implements 2 public instance methods
        def area(self):
            raises an Exception with the message
            "area() is not implemented"
        def integer_validator(self, name, value):
            you can assume name is always a string
            if value is not an integer: raise a TypeError exception
              with the message "<name> must be an integer"
            if value is less or equal to 0: raise a ValueError
              exception with the message "<name> must be greater than 0"
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            s = name + " must be an integer"
            raise TypeError(s)
        if value <= 0:
            s = name + " must be greater than 0"
            raise ValueError(s)
