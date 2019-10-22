import unittest

from beers import translate_string_to_list, my_combo, solution, beer_identifier


class TestMergingOverlappingIntervals(unittest.TestCase):

    def test_output_1(self):
        employee, beer = 7, 4
        list_of_likes = ['YNNY', 'YNYN', 'YNYN', 'NYYN', 'NYYN', 'NYNN', 'NNYN']

        input_list = translate_string_to_list(beer, list_of_likes)
        merged_combination_list = my_combo(input_list)
        result_search = solution(merged_combination_list, set(merged_combination_list[-1]))
        result = beer_identifier(result_search, input_list, set(merged_combination_list[-1])), result_search

        self.assertEqual(result, ([1, 2, 3], [3, 2, 1, 4, 6, 5, 2, 3, 7, 5, 4]), 'An error occurred while processing '
                                                                                 'your request')

    def test_output_2(self):
        employee, beer = 6, 3
        list_of_likes = ['YNN', 'YNY', 'YNY', 'NYY', 'NYY', 'NYN']

        input_list = translate_string_to_list(beer, list_of_likes)
        merged_combination_list = my_combo(input_list)
        result_search = solution(merged_combination_list, set(merged_combination_list[-1]))
        result = beer_identifier(result_search, input_list, set(merged_combination_list[-1])), result_search

        self.assertEqual(result, ([1, 2], [3, 2, 1, 4, 6, 5]), 'An error occurred while processing your request')

    def test_output_3(self):
        employee, beer = 2, 2
        list_of_likes = ['YN', 'NY']

        input_list = translate_string_to_list(beer, list_of_likes)
        merged_combination_list = my_combo(input_list)
        result_search = solution(merged_combination_list, set(merged_combination_list[-1]))
        result = beer_identifier(result_search, input_list, set(merged_combination_list[-1])), result_search

        self.assertEqual(result, ([1, 2], [1, 2]), 'An error occurred while processing your request')

    def test_output_4(self):
        employee, beer = 2, 2
        list_of_likes = ['YN', 'NY']

        input_list = translate_string_to_list(beer, list_of_likes)
        merged_combination_list = my_combo(input_list)
        result_search = solution(merged_combination_list, set(merged_combination_list[-1]))
        result = beer_identifier(result_search, input_list, set(merged_combination_list[-1])), result_search

        self.assertEqual(result, ([1, 2], [1, 2]), 'An error occurred while processing your request')

    def test_output_5(self):
        employee, beer = 12, 9
        list_of_likes = ['YNNNNNNNN', 'YNYNNNNNN', 'YNYNNNNNN', 'NYYNNNNNN', 'NYYNNNNNN', 'NYNNNNNNN', 'NNNYNNNNN',
                         'NNNNYNNNN', 'NNNNNYNNN', 'NNNNNNYNN', 'NNNNNNNYN', 'NNNNNNNNY']

        input_list = translate_string_to_list(beer, list_of_likes)
        merged_combination_list = my_combo(input_list)
        result_search = solution(merged_combination_list, set(merged_combination_list[-1]))
        result = beer_identifier(result_search, input_list, set(merged_combination_list[-1])), result_search

        self.assertEqual(result, ([1, 2, 4, 5, 6, 7, 8, 9], [3, 2, 1, 4, 6, 5, 7, 8, 9, 10, 11, 12]), 'An error '
                                                                                                      'occurred while '
                                                                                                      'processing '
                                                                                                      'your request')
