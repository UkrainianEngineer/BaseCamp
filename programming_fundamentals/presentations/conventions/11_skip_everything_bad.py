"""
This module describes bad example of skipping all the mistakes silently.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


def do_something():pass

try:
    do_something()
except:
    pass
