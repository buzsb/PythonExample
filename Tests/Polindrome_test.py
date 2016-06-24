import unittest
from Polindrome import revers_string

class PolindromeTest(unittest.TestCase):
    def test_corect_work(self):
        self.assertEqual(revers_string('abc'), 'cba')

if __name__ == '__main__':
    unittest.main()