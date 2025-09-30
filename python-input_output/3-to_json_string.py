#!/usr/bin/python3
"""
Write a function that returns the
JSON representation of an object (string)
"""


import json

def to_json_string(my_obj):
    """
    Function to serialise to json
    You don’t need to manage exceptions
      if the object can’t be serialized.
    """
    json.dumps(my_obj)
