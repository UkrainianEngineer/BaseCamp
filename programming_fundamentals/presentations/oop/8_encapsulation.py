"""
This module describes a basic encapsulation in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Human:

    def __init__(self):
        # Encapsulated attribute.
        self.__deposit_sum = 15000

    def increase_deposit(self, value):
        self.__deposit_sum += value

    def show_deposit(self):
        return self.__deposit_sum

if __name__ == '__main__':
    # Instance variable example.
    human = Human()
    #print(human.__deposit_sum)
    human.increase_deposit(1500)
    print(human.show_deposit())
