import unittest
import constant
import sort


class TestMergingOverlappingIntervals(unittest.TestCase):

    def test_sorting(self):
        self.assertEqual(sort.sel_sort(constant.first_set), (
            [2, 11, 12, 18, 19, 21, 25, 26, 30, 37, 42, 44, 45, 46, 58, 65, 68, 72, 73, 76, 83, 85, 89, 91, 93], 25,
            300), 'An error occurred while processing your request with first set by selection sort')
        self.assertEqual(sort.sel_sort(constant.second_set), (
            [2, 3, 5, 6, 13, 15, 18, 20, 21, 24, 27, 31, 32, 34, 38, 40, 41, 42, 43, 47, 48, 49, 50, 51, 52, 55, 58, 60,
             63, 64, 66, 67, 71, 72, 73, 75, 77, 79, 81, 83, 85, 86, 88, 90, 92, 94, 95, 96, 97, 99], 50, 1225),
                         'An error occurred while processing your request with second set by selection sort')
        self.assertEqual(sort.sel_sort(constant.third_set), (
            [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18, 19, 21, 23, 24, 25, 27, 29, 30, 31, 32, 33, 36, 37, 38,
             39, 40, 41, 42, 43, 45, 46, 48, 51, 53, 54, 55, 56, 58, 59, 62, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77,
             78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98], 75, 2775),
                         'An error occurred while processing your request with third set by selection sort')
        self.assertEqual(sort.merge(constant.first_set), (
            [2, 11, 12, 18, 19, 21, 25, 26, 30, 37, 42, 44, 45, 46, 58, 65, 68, 72, 73, 76, 83, 85, 89, 91, 93], 12,
            12),
                         'An error occurred while processing your request with third set by merge sort')
        self.assertEqual(sort.merge(constant.second_set), (
            [2, 3, 5, 6, 13, 15, 18, 20, 21, 24, 27, 31, 32, 34, 38, 40, 41, 42, 43, 47, 48, 49, 50, 51, 52, 55, 58, 60,
             63, 64, 66, 67, 71, 72, 73, 75, 77, 79, 81, 83, 85, 86, 88, 90, 92, 94, 95, 96, 97, 99], 25, 25),
                         'An error occurred while processing your request with second set by merge sort')
        self.assertEqual(sort.merge(constant.third_set), (
            [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18, 19, 21, 23, 24, 25, 27, 29, 30, 31, 32, 33, 36, 37, 38,
             39, 40, 41, 42, 43, 45, 46, 48, 51, 53, 54, 55, 56, 58, 59, 62, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77,
             78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98], 37, 37),
                         'An error occurred while processing your request with third set by merge sort')
