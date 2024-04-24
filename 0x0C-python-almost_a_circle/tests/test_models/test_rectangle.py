#!/usr/bin/python3
"""Unittests for the rectangle class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittesting of The Rectangle class"""

    def test_rec1(self):
        r1 = Rectangle(10, 2,)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_rec2(self):
        r2 = Rectangle(5, 4, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 2)

    def test_rec3(self):
        r3 = Rectangle(2, 10, 5, 3)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 10)
        self.assertEqual(r3.x, 5)
        self.assertEqual(r3.y, 3)

    def test_rec4(self):
        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)
        self.assertEqual(r4.id, 12)


if __name__ == "__main__":
    unittest.main()
        
