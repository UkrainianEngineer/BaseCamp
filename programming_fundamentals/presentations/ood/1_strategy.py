"""
This module describes a basic example of strategy pattern in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# The Strategy pattern suggests to take a class that does something important
# in a lot of different ways and extract all these algorithms
# into separate classes called strategies.


class StrategyExample:
    def __init__(self, func=None):
        if func:
            self.execute = func
    def execute(self):
        print("Original execution")

def executeReplacementFirst():
    print("First Strategy")

def executeReplacementSecond():
    print("Second Strategy")


# This is a simple usage of our singleton.
strategy = StrategyExample()
strategy1 = StrategyExample(executeReplacementFirst)
strategy2 = StrategyExample(executeReplacementSecond)

strategy.execute()
strategy1.execute()
strategy2.execute()
