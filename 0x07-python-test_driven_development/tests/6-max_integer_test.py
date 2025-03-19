#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        negative = [-1, -5, -3, -8]
        self.assertEqual(max_integer(negative), -1)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers."""
        mixed = [-1, 5, -3, 8]
        self.assertEqual(max_integer(mixed), 8)

    def test_float_numbers(self):
        """Test a list with float numbers."""
        floats = [1.5, 3.2, 2.8, 5.1]
        self.assertEqual(max_integer(floats), 5.1)

    def test_duplicate_numbers(self):
        """Test a list with duplicate numbers."""
        duplicates = [1, 2, 2, 4, 4, 3]
        self.assertEqual(max_integer(duplicates), 4)

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["a", "b", "c"]
        with self.assertRaises(TypeError):
            max_integer(strings)

    def test_none(self):
        """Test with None as input."""
        with self.assertRaises(TypeError):
            max_integer(None)
