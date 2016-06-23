import unittest
from NoDuplicateList import list_remuve_duplicates

class NoDuplicateListTest(unittest.TestCase):
    def test_equality(self):
        a = [1, 1, 3, 6, 4, 7, 3, 9, 4]
        b = [1, 3, 6, 4, 7, 9]
        self.assertEqual(list_remuve_duplicates(a), b)
    def test_not_iterable_argument(self):
        with self.assertRaises(TypeError):
            list_remuve_duplicates(12)
            list_remuve_duplicates(100)

if __name__ == '__main__':
    unittest.main()