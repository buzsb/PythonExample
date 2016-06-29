import unittest
from EvenNumbers import even_numbers


class EvenNumbersTest(unittest.TestCase):

    def test_equality(self):
        a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(even_numbers(a), [4, 16, 36, 64, 100])

    def test_empty_list(self):
        a = []
        self.assertEqual(even_numbers(a), [])

    def test_no_even_numders_in_list(self):
        a = [3, 5, 7]
        self.assertEqual(even_numbers(a), [])

if __name__ == '__main__':
    unittest.main()
