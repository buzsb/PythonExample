import unittest
from BackwardString import backwards_string

class BackwardTest(unittest.TestCase):
    def test_corect_work(self):
        self.assertEqual(backwards_string('aa ff gg'), 'gg ff aa')
        self.assertEqual(backwards_string('a b c d'), 'd c b a')

    def test_argument_not_string(self):
        with self.assertRaises(TypeError):
            backwards_string(123)
            backwards_string([1,2])


if __name__ == '__main__':
    unittest.main()