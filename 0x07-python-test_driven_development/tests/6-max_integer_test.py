#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_value(self):
        """ Test list with random order"""
        self.assertEqual(max_integer([79, 95, 9, 51, 0, -45]), 95)

        """ Test negative integers list """
        self.assertEqual(max_integer([-1, -6, -84.5, -20]), -1)

        """ Test max integer at the beginning of the list"""
        self.assertEqual(max_integer([80, 56, 35, 15, 0, -56]), 80)

        """ Test max integer at the end of the list"""
        self.assertEqual(max_integer([56, 30, 5.5, 0, -66, 99]), 99)

        """ Test an empty list """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

        """ Test a string """
        self.assertEqual(max_integer("This test file just broke my brain"), "y")

        """ Test a list with a string(s) in it """
        self.assertEqual(max_integer(["zero", "one", "three"]), "zero")

        """ Test a list of lists """
        self.assertEqual(max_integer([[0, 1], [2, 3]]), [2, 3])


if __name__ == '__main__':
    unittest.main()