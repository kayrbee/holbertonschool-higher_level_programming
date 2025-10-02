#!/usr/bin/python3
"""
Write a module that serialises and deserialises to/from json
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialise data and save to a file
    """
    with open(filename, "w", encoding="utf-8"):
        json.dump(data, filename)


def load_and_deserialize(filename):
    """
    Deserialise data from a file
    """
    data = json.load(filename)
    return data
