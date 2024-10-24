# tests/test_models/test_base.py
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_initialization(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_base_custom_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)


if __name__ == '__main__':
    unittest.main()
