"""
This module describes a basic example how `self` works in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Message:
    def greeting(self, name):
        return "Hello {}!".format(name)

if __name__ == '__main__':
    message = Message()
    greeting = message.greeting("Pavlo")
    print(greeting)
    self_greeting = Message.greeting(message, "Paul")
    print(self_greeting)