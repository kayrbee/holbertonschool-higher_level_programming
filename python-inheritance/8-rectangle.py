#!/usr/bin/python3
"""
Module contains one subclass
Inherits from 7-base_geometry.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle subclass of BaseGeometry
    Has width and height
    """
    def __init__(self, width, height):
        """
        Initialise with width and height properties
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
