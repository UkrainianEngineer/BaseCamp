"""
This module describes a basic example how `self` works in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Message:
    class_var = 2

    def __init__(self):
        self.instance_var = 4

if __name__ == '__main__':
    # Instance variable example.
    message = Message()
    new_message = Message()
    print(message.instance_var)
    print(new_message.instance_var)
    message.instance_var = 6
    print(message.instance_var)
    print(new_message.instance_var)

    # Class variable example.
    message = Message()
    new_message = Message()
    print(message.class_var)
    print(new_message.class_var)
    Message.class_var = 6
    print(message.class_var)
    print(new_message.class_var)