#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""
singleton2.py
=============

Lazy instantiation
"""


class Singleton:
    """
    Singleton class
    """
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__method called...")
        else:
            print("Instance already created:", self.get_instance())

    @classmethod
    def get_instance(cls):
        """
        Create Object
        """
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


if __name__ == "__main__":
    SING = Singleton()
    print("Object created", Singleton.get_instance())
    SING1 = Singleton()
