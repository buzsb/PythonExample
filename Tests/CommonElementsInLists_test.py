import unittest
from CommonElementsInLists import common_elements_finding

class CommonElsementsTest(unittest.TestCase):
    def test_equality(self):
        a, b = [1, 2, 3], [2, 4, 5]
        self.assertEqual(common_elements_finding(a, b), [2])
        a, b = [1, 2, 3, 4], [2, 4, 5]
        self.assertEqual(common_elements_finding(a, b), [2, 4])

if __name__ == '__main__':
    unittest.main()