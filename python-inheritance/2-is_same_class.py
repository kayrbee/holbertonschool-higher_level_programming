#!/usr/bin/python3
"""
Module contains one class
"""


class MyList(list):
    """
    Extends the list class
    Adds a print_sorted method:
        Sorts then prints the given list object
    """
    def print_sorted(self):
        print(sorted(self))
