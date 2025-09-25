#!/usr/bin/python3
"""
Module contains a class which
  extends list class
"""


class VerboseList(list):
    """
    VerboseList prints notifications
    whenever an item is added or removed
    from a list
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        if item in self:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)
        else:
            print("Item not found")

    def pop(self, index=-1):
        self.index_validator(index)
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(item)

    def index_validator(self, index):
        if not isinstance(index, int):
            raise TypeError("Must be an integer")
        if len(self) == 0:
            raise ValueError("List is empty")
        if index > len(self) - 1 or index < -len(self):
            raise ValueError("Index is out of range")
