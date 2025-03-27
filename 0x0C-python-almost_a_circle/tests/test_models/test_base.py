#!/usr/bin/python3
"""Unittest for Base class."""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_auto_id_assignment(self):
        """Test automatic ID assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_manual_id_assignment(self):
        """Test manual ID assignment."""
        b4 = Base(10)
        b5 = Base(-5)
        b6 = Base(0)

        self.assertEqual(b4.id, 10)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b6.id, 0)

    def test_mixed_id_assignment(self):
        """Test mixed ID assignment."""
        b1 = Base()
        b2 = Base(100)
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 2)

    def test_private_attribute_access(self):
        """Test that the private attribute __nb_objects is not directly accessible."""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

if __name__ == '__main__':
    unittest.main()
