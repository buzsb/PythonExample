import unittest
from BackwardString import backwards_string


class BackwardTest(unittest.TestCase):

    def test_corect_work(self):
        self.assertEqual(backwards_string('aa ff gg'), 'gg ff aa')
        self.assertEqual(backwards_string('a b c d'), 'd c b a')

    def test_empty_string_argument(self):
        self.assertEqual(backwards_string(''), '')

    def test_argument_int(self):
        with self.assertRaises(TypeError):
            backwards_string(123)

    def test_argument_list(self):
        with self.assertRaises(TypeError):
            backwards_string([1, 2])

    def test_argument_dictionary(self):
        with self.assertRaises(TypeError):
            backwards_string({'a': 2})


if __name__ == '__main__':
    unittest.main()
