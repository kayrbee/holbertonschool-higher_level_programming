#!/usr/bin/python3
"""
Extend the Student class from
9-student.py
"""


class Student:
    """
    Instantiate the Student class with
    first name, last name and age

    Include a public method to_json(self, attrs=None)
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    """
    def __init__(self, first_name='', last_name='', age=''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)
        else:
            obj_attrs = vars(self)
            filtered_attrs = {}
            for attr in attrs:
                if attr in obj_attrs:
                    filtered_attrs['{}'.format(attr)] = obj_attrs[attr]
                else:
                    continue
            return filtered_attrs
