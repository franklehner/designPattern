#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pylint: disable=too-few-public-methods
"""
singleton1.py
=============
"""


class Singleton():
    """
    Class Singleton
    """
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


SING = Singleton()
print("Object created", SING)

SING1 = Singleton()
print("Object created", SING1)
