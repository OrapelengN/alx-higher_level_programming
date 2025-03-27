#!/usr/bin/python3
"""Unittest for Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_init(self):
        """Test initialization."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

        r2 = Rectangle(2, 10, 3, 4, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 12)

    def test_width_setter(self):
        """Test width setter."""
        r = Rectangle(1, 1)
        r.width = 5
        self.assertEqual(r.width, 5)

        with self.assertRaises(TypeError):
            r.width = "invalid"

        with self.assertRaises(ValueError):
            r.width = 0

        with self.assertRaises(ValueError):
            r.width = -1

    def test_height_setter(self):
        """Test height setter."""
        r = Rectangle(1, 1)
        r.height = 10
        self.assertEqual(r.height, 10)

        with self.assertRaises(TypeError):
            r.height = "invalid"

        with self.assertRaises(ValueError):
            r.height = 0

        with self.assertRaises(ValueError):
            r.height = -1

    def test_x_setter(self):
        """Test x setter."""
        r = Rectangle(1, 1)
        r.x = 2
        self.assertEqual(r.x, 2)

        with self.assertRaises(TypeError):
            r.x = "invalid"

        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_setter(self):
        """Test y setter."""
        r = Rectangle(1, 1)
        r.y = 3
        self.assertEqual(r.y, 3)

        with self.assertRaises(TypeError):
            r.y = "invalid"

        with self.assertRaises(ValueError):
            r.y = -1


if __name__ == '__main__':
    unittest.main()
