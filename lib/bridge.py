#!/usr/bin/env python
#-*- coding: utf-8 -*-
#pylint: disable=all
""" Bridge Pattern """


import abc as _abc


class Bridge(object):
    """ Interface """
    __metaclass__ = _abc.ABCMeta

    @_abc.abstractmethod
    def operation_imp(self):
        """ Abstract method operation_imp """
        return


class Abstraction(object):
    """ Abstraction class """
    def __init__(self, implementation):
        """ Constructor """
        self.bridge = implementation

    def operation(self):
        """ operation in the abstract way """
        return "Abstraction <<< BRIDGE >>>>" + self.bridge.operation_imp()


class ImplementationA(Bridge):
    """ child class ImplementationA """
    def operation_imp(self):
        """ override """
        return "ImplementationA"


class ImplementationB(Bridge):
    """ child class ImplementationB """
    def operation_imp(self):
        """ override """
        return "ImplementationB"
