#!/usr/bin/python3
"""
Write a class Student that defines a student by
Public instance attributes:
- first_name
- last_name
- age
"""


class Student:
    """
    Instantiate the Student class with
    first name, last name and age

    Include a public method to_json(self)
    as per ex 8
    """
    def __init__(self, first_name='', last_name='', age=''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
