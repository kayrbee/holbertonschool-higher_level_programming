#!/usr/bin/python3
"""
Module contains one function
"""


def inherits_from(obj, a_class):
    """
    Function checks object inheritance
    Filters out cases of same type
    Returns boolean
    """
    if type(obj) is not a_class:
        return (True if issubclass(type(obj), a_class) else False)
