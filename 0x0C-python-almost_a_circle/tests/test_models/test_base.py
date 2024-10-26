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


class TestBaseCustomID(unittest.TestCase):

    def test_custom_id(self):
        """Test that Base correctly stores a custom ID when provided."""
        base_instance = Base(89)

        self.assertEqual(base_instance.id, 89)  # Check if ID is as assigned


if __name__ == "__main__":
    unittest.main()
