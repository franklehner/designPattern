#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pylint: disable=all
""" Singleton Pattern """


class Singleton(object):
    """ Singleton class """
    _instance = None
    def __new__(cls, *args, **kwargs):
        """ Create new instance of the class """
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
