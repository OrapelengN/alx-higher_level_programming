#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer function."""

    def test_ordered_list(self):
        """Test when the list is sorted in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test when the list is not sorted."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max integer is at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        """Test when the list has only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test when the list is empty."""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test when the list contains all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test when the list contains both positive and negative numbers."""
        self.assertEqual(max_integer([-10, 5, 0, 20, -2]), 20)

    def test_duplicates(self):
        """Test when the list contains duplicate values."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        """Test when the list contains floating-point numbers."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_int_floats(self):
        """Test when the list contains both integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.9, 2]), 4.9)

    def test_large_numbers(self):
        """Test when the list contains very large numbers."""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_string(self):
        """Test when the input is a string (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer("hello")

    def test_list_of_strings(self):
        """Test when the list contains strings (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer(["hello", "world"])

    def test_none_argument(self):
        """Test when passing None (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
