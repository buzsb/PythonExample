import unittest
from CommonElementsInLists import common_elements_finding


class CommonElsementsTest(unittest.TestCase):

    def test_equality(self):
        a, b = [1, 2, 3, 4], [2, 4, 5]
        self.assertEqual(common_elements_finding(a, b), [2, 4])

    def test_first_list_empty(self):
        a, b = [], [1, 2, 3]
        self.assertEqual(common_elements_finding(a, b), [])

    def test_second_list_empty(self):
        a, b = [1, 2, 3], []
        self.assertEqual(common_elements_finding(a, b), [])

    def test_same_lists(self):
        a, b = [1, 2, 3], [1, 2, 3]
        self.assertEqual(common_elements_finding(a, b), [1, 2, 3])

    def test_string_in_lists(self):
        a, b = [1, 'abc', 3], [1, 'abc']
        self.assertEqual(common_elements_finding(a, b), [1, 'abc'])

if __name__ == '__main__':
    unittest.main()
