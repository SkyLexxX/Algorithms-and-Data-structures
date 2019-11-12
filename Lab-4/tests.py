import unittest

from main import create_graph


class DetectCycleDFS(unittest.TestCase):

    def test_output_1(self):
        g = create_graph('test_output_1.txt')
        result = g.identify_cycle()
        self.assertEqual(result, ([0, 5, 10]), 'An error occurred while processing your request')

    def test_output_2(self):
        g = create_graph('test_output_2.txt')
        result = g.identify_cycle()
        self.assertEqual(result, ([46, 70, 73, 163, 125, 98, 20, 127, 131, 154, 46, 62, 167]), 'An error occurred while'
                                                                                               'processing your request')

    def test_output_3(self):
        g = create_graph('test_output_3.txt')
        result = g.identify_cycle()
        self.assertEqual(result, ([40, 4, 29, 27, 9, 73, 70, 123, 66, 55, 136, 87, 112, 109, 95, 46, 40]), 'An error '
                                                                                                           'occurred '
                                                                                                           'while '
                                                                                                           'processing '
                                                                                                           'your '
                                                                                                           'request')

