#!/usr/bin/python3
"""
Write a function that returns an object of
a JSON string
"""


import json


def from_json_string(my_str):
    """
    Function to deserialise from json
    You don’t need to manage exceptions
     if the JSON string doesn’t represent an object.
    """
    return json.loads(my_str)
