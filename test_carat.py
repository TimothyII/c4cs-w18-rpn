import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("5 1 ^")
        self.assertEqual(5, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 ^")
        self.assertEqual(125, result)
    def test_multiply(self):
        result = rpn.calculate("100 0 ^")
        self.assertEqual(1, result)
    def test_divide(self):
        result = rpn.calculate("100 2 ^")
        self.assertEqual(10000, result)

