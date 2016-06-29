import unittest
from Polindrome import reversing_string


class PolindromeTest(unittest.TestCase):

    def test_corect_work(self):
        self.assertEqual(reversing_string('abc'), 'cba')

    def test_empty_string_argument(self):
        self.assertEqual(reversing_string(''), '')

    def test_number_argument(self):
        self.assertEqual(reversing_string('12'), '21')


if __name__ == '__main__':
    unittest.main()
