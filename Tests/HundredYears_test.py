import unittest
from HundredYears import say_when, calculate_years

class HundredYearsTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(calculate_years(99), 2017)

    def test_over_hundred(self):
        self.assertFalse(calculate_years(100))
        self.assertFalse(calculate_years(200))
        self.assertFalse(calculate_years(300))
        
    def test_less_zero(self):
        self.assertFalse(calculate_years(-1))
        self.assertFalse(calculate_years(-10))
        self.assertFalse(calculate_years(-100))

if __name__ == '__main__':
    unittest.main()