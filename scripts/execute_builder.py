""" Script for Builder Pattern """


import sys as _sys
import os as _os
_sys.path.append(_os.path.abspath("../"))

from designPattern.lib.builder import Director as _Director
from designPattern.lib.builder import Builder1 as _Builder1
from designPattern.lib.builder import Builder2 as _Builder2


def main():
    """ Main function """
    director = _Director()
    builder1 = _Builder1()
    builder2 = _Builder2()

    director.construct(builder1)
    product1 = builder1.get_result()
    product1.display()

    director.construct(builder2)
    product2 = builder2.get_result()
    product2.display()


if __name__ == "__main__":
    main()
