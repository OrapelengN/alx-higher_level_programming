#!/usr/bin/python3
"""Unittest for Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_init_with_id(self):
        """Test initialization with a given id."""
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

        b2 = Base(0)
        self.assertEqual(b2.id, 0)

        b3 = Base(-5)
        self.assertEqual(b3.id, -5)

    def test_init_without_id(self):
        """Test initialization without a given id."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_multiple_instances(self):
        """Test multiple instances with and without ids."""
        b1 = Base()
        b2 = Base(100)
        b3 = Base()
        b4 = Base(0)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 0)
        self.assertEqual(b5.id, 3)

    def test_private_attribute_access(self):
        """Test that the private attribute __nb_objects is not directly accessible."""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

if __name__ == '__main__':
    unittest.main()
