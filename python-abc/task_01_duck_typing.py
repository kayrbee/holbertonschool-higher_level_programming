#!/usr/bin/python3
"""
Module contains abstract class and
  related subclasses
"""


from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class - Shape
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Class inherits from Shape
    """
    pi = 3.141592653589793

    def __init__(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            self.__radius = 0
    
    def area(self):
        return (self.__class__.pi * self.__radius ** 2)
    
    def perimeter(self):
        return (2 * self.__class__.pi * self.__radius)



class Rectangle(Shape):
    """
    Class inherits from Shape
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    def area(self):
        return (self.__width * self.__height)
    
    def perimeter(self):
        return (2 * self.__width + 2 * self.__height)

def shape_info(self):
    area = self.area()
    perimeter = self.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
