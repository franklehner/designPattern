#!/usr/bin/env python
#-*- coding: utf-8 -*-
#pylint: disable=all
""" Builder Pattern """


import abc as _abc


class Director(object):
    """ Director class """

    @classmethod
    def construct(cls, builder):
        """ construct builder """
        builder.build_part_A()
        builder.build_part_B()
        builder.build_part_B()


class IBuilder(object):
    """ Interface """
    __metaclass__ = _abc.ABCMeta

    @_abc.abstractmethod
    def build_part_A(self):
        """ builder for part A """
        pass

    @_abc.abstractmethod
    def build_part_B(self):
        """ builder for part B """
        pass

    @_abc.abstractmethod
    def get_result(self):
        """ return result """
        return


class Builder1(IBuilder):
    """ Builder 1 """
    def __init__(self):
        """ Constructor """
        self._product = Product()

    def build_part_A(self):
        """ build part A """
        self._product.add("PartA ")

    def build_part_B(self):
        """ build part B """
        self._product.add("PartB ")

    def get_result(self):
        """ result """
        return self._product


class Builder2(IBuilder):
    """ Builder 1 """
    def __init__(self):
        """ Constructor """
        self._product = Product()

    def build_part_A(self):
        """ build part A """
        self._product.add("PartX ")

    def build_part_B(self):
        """ build part B """
        self._product.add("PartY ")

    def get_result(self):
        """ result """
        return self._product


class Product(object):
    """ Product class """
    def __init__(self):
        """ Constructor """
        self.parts = []

    def add(self, part):
        """ Add a part to parts """
        self.parts.append(part)

    def display(self):
        """ Show """
        print "\nProduct Parts ------------"
        for part in self.parts:
            print part,
        print
