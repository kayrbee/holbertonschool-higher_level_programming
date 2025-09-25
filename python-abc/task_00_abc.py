#!/usr/bin/python3
"""
Module contains abstract class and
  related subclasses
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class - Animal
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Class inherits from Animal
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Class inherits from Animal
    """

    def sound(self):
        return "Meow"
