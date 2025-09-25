#!/usr/bin/python3
"""
Module contains a class which
  extends iter()
"""


class CountedIterator:
    """
    CountedIterator is a custom iterator that wraps
    any iterable and counts how many items have been
    consumed during iteration.

    Other ways to enhance this class:
    - Add a reset method to reset counter and iterator
    - Add a fn to recreate the iterable
    - Support slicing and index access
    """
    def __init__(self, data):
        self.length = len(data)
        self.iterator = iter(data)
        self.__counter = 0
    
    def __iter__(self):
        return self

    def get_count(self):
        return self.__counter

    def __next__(self):
        if self.__counter == self.length:
            raise StopIteration
        self.__counter += 1
        return next(self.iterator)
