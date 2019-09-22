import unittest
from main import calendar


class TestMergingOverlappingIntervals(unittest.TestCase):

    def test_output_1(self):
        thisarray = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        self.assertEqual(calendar(thisarray), [(0, 1), (3, 8), (9, 12)], 'An error occurred while processing your '
                                                                         'request')

    def test_output_2(self):
        thisarray = [(0, 3), (1, 2)]
        self.assertEqual(calendar(thisarray), [(0, 3)], 'An error occurred while processing your '
                                                        'request')

    def test_output_3(self):
        thisarray = [(0, 3), (0, 3)]
        self.assertEqual(calendar(thisarray), [(0, 3)], 'An error occurred while processing your '
                                                        'request')

    def test_output_4(self):
        thisarray = []
        self.assertEqual(calendar(thisarray), [], 'An error occurred while processing your '
                                                  'request')

