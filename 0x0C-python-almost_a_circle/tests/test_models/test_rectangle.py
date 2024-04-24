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

    def test_typerror_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle('10', 2)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(None, 2)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(12.5, 2)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle({1, 4, 7}, 2)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle([1, 4, 7], 2)


    def test_typerror_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rh = Rectangle(10, "two")
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rh = Rectangle(10, {1, 4, 7})
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rh = Rectangle(10, 12.5)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rh = Rectangle(2, None)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rh = Rectangle(2, [1, 4, 7])


    def test_typeerror_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rx = Rectangle(10, 2, "six")
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rx = Rectangle(7, 4, 5.3, 2)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rx = Rectangle(4, 7, None)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rx = Rectangle(10, 2, {1, 2, 3}, 5)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rx = Rectangle(3, 6, [1, 2, 4], 3)


    def test_typeerror_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            ry = Rectangle(10, 2, 6, "four")
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            ry = Rectangle(5, 7, 4, 2.3)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            ry = Rectangle(10, 5, 2, {1, 3, 6})
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            ry = Rectangle(2, 3, 6, [2, 5, 3])


    def test_valueerror_width(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            rw = Rectangle(0, 5)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            rw = Rectangle(-5, 10)


    def test_valueerror_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            rh = Rectangle(5, -10)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            rh = Rectangle(2, 0)


    def test_valueerror_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            rx = Rectangle(10, 2, -5, 4)


    def test_valueerror_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            ry = Rectangle(10, 2, 5, -4)


if __name__ == "__main__":
    unittest.main()
        
