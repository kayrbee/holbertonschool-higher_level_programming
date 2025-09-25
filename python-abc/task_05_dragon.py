#!/usr/bin/python3
"""
Module contains a class which
  uses mixins
"""


class SwimMixin:
    pass

class FlyMixin:
    pass

class Dragon(SwimMixin, FlyMixin):
    pass