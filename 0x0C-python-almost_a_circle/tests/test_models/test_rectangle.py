#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 50)

    def test_width_setter(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = 0

    def test_height_setter(self):
        with self.assertRaises(ValueError):
            self.rectangle.height = 0

    def test_x_setter(self):
        with self.assertRaises(ValueError):
            self.rectangle.x = -1

    def test_y_setter(self):
        with self.assertRaises(ValueError):
            self.rectangle.y = -1

if __name__ == '__main__':
    unittest.main()
