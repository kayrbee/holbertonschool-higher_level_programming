#!/usr/bin/python3
"""
Extend the Student class from
10-student.py
"""


class Student:
    """
    Instantiate the Student class with
    first name, last name and age

    Include a public method to_json(self, attrs=None)
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved

    Include a public method def reload_from_json(self, json)
        that replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
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

    def reload_from_json(self, json):
        if not json or not isinstance(json, dict):
            return
        keys = {"first_name", "last_name", "age"}
        for key in keys:
            if key in json:
                setattr(self, key, json[key])
