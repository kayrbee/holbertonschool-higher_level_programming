#!/usr/bin/python3
"""
Write a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    # # Get a string of object
    new_dict = {'name': obj.name, 'number': obj.number}
    return new_dict
