""" Script for Singleton Pattern """


import sys as _sys
import os as _os
_sys.path.append(_os.path.abspath("../"))

from designPattern.lib.singleton import Singleton as _Singleton


def main():
    """ Main function """
    singleton1 = _Singleton()
    singleton2 = _Singleton()
    if id(singleton1) == id(singleton2):
        print "same"
    else:
        print "different"


if __name__ == "__main__":
    main()
