#!/usr/bin/python3
"""
Module contains one function
"""


def is_kind_of_class(obj, a_class):
    """
    Function checks object is of kind
    Returns boolean
    """
    return (True if isinstance(obj, a_class) else False)
