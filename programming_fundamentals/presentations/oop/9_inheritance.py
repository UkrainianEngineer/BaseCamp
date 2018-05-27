"""
This module describes a basic inheritance in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Human:

    def get_location(self):
        return "Your location is Ukraine."


class Student(Human):
    @staticmethod
    def get_scholarship():
        return "Your scholarship is 1000."

    @staticmethod
    def get_subjects():
        return "Your favourite subjects are mathematics and informatics."

if __name__ == '__main__':
    # Instance variable example.
    student = Student()
    print(student.get_scholarship())
    print(student.get_subjects())
    print(student.get_location())
