from func_for_task23 import swap, average

import unittest

""" я наверно не понял задание или ненашел требований к этим функциям"""


class TestFunc_for_task23(unittest.TestCase):

    def test_swap(self):
        self.assertEqual(swap("abcd"), 'cdab')
        self.assertEqual(swap('abcde'), 'cdeab')
        self.assertEqual(swap(''), '')

    def test_swap_2(self):
        self.assertEqual(type(swap('abcd')), str)

    def test_average(self):
        self.assertEqual(average(2, 4, 6), 4)
        self.assertEqual(average(33), 33)
        self.assertEqual(average(0, 0, 0, 0), 0)
        self.assertEqual(average(), 0)  # будет ошибка деление на 0

    def test_average_2(self):
        self.assertEqual(type(average(2, 4, 6)), float)


if __name__ == '__main__':
    unittest.main()
