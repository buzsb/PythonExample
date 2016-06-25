import unittest
from LessThatInput import less_than_input

class LessThatInputTest(unittest.TestCase):
    
    def test_equality(self):   
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(less_than_input(a, 10), [1, 1, 2, 3, 5, 8])
        self.assertEqual(less_than_input(a, 10.6), [1, 1, 2, 3, 5, 8])
        
    def test_str_in_array(self):
        a = [1, 'dd', 3, 5]
        self.assertEqual(less_than_input(a, 10), [1,3,5])
    
    def test_empty_list(self):
        self.assertEqual(less_than_input([], 10), [])

    def test_second_argument_string(self):
        a = [1, 2, 3, 5]
        self.assertEqual(less_than_input(a, 's'), [])

if __name__ == '__main__':
    unittest.main()