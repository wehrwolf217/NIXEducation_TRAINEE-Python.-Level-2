from func_for_task23 import swap, average

import unittest

""" я наверно не понял задание или ненашел требований к этим функциям"""
class TestFunc_for_task23(unittest.TestCase):
    def setUp(self):
        pass

    def test_swap(self):
        self.assertEqual(swap("abcd"), 'cdab')

    def test_swap_2(self):
        self.assertEqual(type(swap('abcd')), str)

    def test_average(self):
        self.assertEqual(average(2, 4, 6), 4)

    def test_average_2(self):
        self.assertEqual(type(average(2, 4, 6)), float)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
