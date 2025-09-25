#!/usr/bin/python3
"""
Module contains a class which
  extends iter()
"""


class CountedIterator:
    """
    CountedIterator extends iter()
    function to track the number of items
    iterated over.

    Overrides __next__() with a counter
    """
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.iterator = iter(data)
        self.__counter = 0

    def get_count(self):
        return self.__counter

    def __next__(self):
        if self.__counter == self.length:
            raise StopIteration
        self.__counter += 1
        return self.data[self.__counter - 1]
