#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
from typing import List
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered: List[int] = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered: List[int] = [1, 2, 4, 3, 4, 5]
        self.assertEqual(max_integer(unordered), 5)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning: List[int] = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 5)

    def test_empty_list(self):
        """Test an empty list."""
        empty: List[int] = []
        self.assertIsNone(max_integer(empty))

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element: List[int] = [2]
        self.assertEqual(max_integer(one_element), 2)

    def test_floats(self):
        """Test a list of floats."""
        floats: List[float] = [1.53, 6.33, -9.123, 15.2, 6.0, 17.5]
        self.assertEqual(max_integer(floats), 17.5)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats: List[float] = [1.53, 15.5, -9, 15, 6, 16]
        self.assertEqual(max_integer(ints_and_floats), 16)

    def test_string(self):
        """Test a string."""
        string: str = "Morning"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings: List[str] = ["Asemonu", "is", "my", "last", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertIsNone(max_integer(""))


if __name__ == '__main__':
    unittest.main()
