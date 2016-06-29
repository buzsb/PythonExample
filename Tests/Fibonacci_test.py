import unittest
from Fibonacci import fib, rfib


class FibonacciTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(17), 1597)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fib(-2)

    def test_string_argument(self):
        with self.assertRaises(ValueError):
            fib('string')


class RecursiveFibonacciTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(rfib(6), 8)
        self.assertEqual(rfib(17), 1597)

    def test_negative(self):
        self.assertEqual(rfib(-1), -1)
        self.assertEqual(rfib(-5), -5)

    def test_string_argument(self):
        self.assertEqual(type(rfib('aa')), str)
        self.assertEqual(rfib('more'), "This is not a namber")


if __name__ == '__main__':
    unittest.main()
