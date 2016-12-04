""" Try to use the Bridge Pattern """


import sys, os
sys.path.append(os.path.abspath("../"))
from designPattern.lib.bridge import Abstraction as _Abstraction
from designPattern.lib.bridge import ImplementationA as _ImplementationA
from designPattern.lib.bridge import ImplementationB as _ImplementationB


def main():
    """ Main Program """
    print "Bridge Pattern"
    print _Abstraction(_ImplementationA()).operation()
    print _Abstraction(_ImplementationB()).operation()


if __name__ == "__main__":
    main()
