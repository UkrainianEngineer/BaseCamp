#!/usr/bin/env python
"""
This module describes unittests for `numerical_functions` module.
This is needed for results verification only.
This is a helpful tool for mentors to verify the results of the students' home tasks.
"""
import unittest

from data_types.numericals_functions import (
    binary_to_decimal,
    decimal_to_binary,
    handle_exceptions,
    storage
)

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

class TestNumericalFunctions(unittest.TestCase):

    def verify_result_type(self, fn, value, expected):
        message = "`{}` type is expected, but `{}` found."
        result = fn(value)
        self.assertIsInstance(
            result,
            expected,
            message.format(expected.__name__, type(result).__name__)
        )

    def verify_results(self, fn, value, expected, message):
        if value is not None:
            result = fn(value)
        else:
            result = fn()
        self.assertEqual(
            result,
            expected,
            message.format(value, expected, result)
        )

    def test_binary_to_decimal_values(self):
        message = "Decimal representation for `{}` value is `{}`, but `{}` found."

        self.verify_results(binary_to_decimal, 10, 2, message)
        self.verify_results(binary_to_decimal, 11010, 26, message)
        self.verify_results(binary_to_decimal, 11010101010, 1706, message)

    def test_binary_to_decimal_result_type(self):
        self.verify_result_type(binary_to_decimal, 10, int)

    def test_decimal_to_binary_result_type(self):
        self.verify_result_type(decimal_to_binary, 2, int)

    def test_decimal_to_binary_values(self):
        message = "Binary representation for `{}` value is `{}`, but `{}` found."

        self.verify_results(decimal_to_binary, 2, 10, message)
        self.verify_results(decimal_to_binary, 3, 11, message)
        self.verify_results(decimal_to_binary, 1990, 11111000110, message)
        self.verify_results(decimal_to_binary, 2018, 11111100010, message)

    def test_storage_result_type(self):
        self.verify_result_type(storage, [], list)
        self.verify_result_type(storage, ["message"], list)

    def test_storage_values(self):
        message = "Expected storage for `{}` value is `{}`, but `{}` found."

        self.verify_results(storage, [], ["data"], message)
        self.verify_results(storage, None, ["data"], message)
        self.verify_results(storage, ["test"], ["test", "data"], message)
        self.verify_results(storage, ["message"], ["message", "data"], message)

    def test_handle_exceptions_type(self):
        self.verify_result_type(handle_exceptions, 16, str)
        self.verify_result_type(handle_exceptions, 100, str)
        self.verify_result_type(handle_exceptions, '4', str)
        self.verify_result_type(handle_exceptions, 'test', str)

    def test_handle_exceptions_values(self):
        message = "Expected message for `{}` value is `{}`, but `{}` found."

        self.verify_results(handle_exceptions, 1, "Wow! My number is lower.", message)
        self.verify_results(handle_exceptions, "1", "Wow! My number is lower.", message)
        self.verify_results(handle_exceptions, 41, "Wow! My number is lower.", message)
        self.verify_results(handle_exceptions, 42, "Wow! My number is lower.", message)
        self.verify_results(handle_exceptions, 43, "Yey! My number is higher!", message)
        self.verify_results(handle_exceptions, 1000, "Yey! My number is higher!", message)

if __name__ =='__main__':
    unittest.main()
