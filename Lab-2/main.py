import unittest


class TestMergingOverlappingIntervals(unittest.TestCase):

    def test_output_1(self):
        thisarray = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        self.assertEqual(calendar(thisarray), [(0, 1), (3, 8), (9, 12)], 'An error occurred while processing your '
                                                                         'request')

    def test_output_2(self):
        thisarray = [(0, 3), (1, 2)]
        self.assertEqual(calendar(thisarray), [(0, 3)], 'An error occurred while processing your '
                                                        'request')


def calendar(intervals):
    sorted_intervals = sorted(intervals, key=lambda tup: tup[0])
    merged_intervals = []

    for pair in sorted_intervals:
        if not merged_intervals:
            merged_intervals.append(pair)
        else:
            last_interval = merged_intervals.pop()
            if last_interval[1] >= pair[0]:
                new_tup = (last_interval[0], max(last_interval[1], pair[1]))
                merged_intervals.append(new_tup)
            else:
                merged_intervals.append(last_interval)
                merged_intervals.append(pair)
    return merged_intervals


def main():
    thisarray = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    print("Original list of ranges: {}".format(thisarray))
    merged_list = calendar(thisarray)
    print("List of ranges after merge_ranges: {}".format(merged_list))


if __name__ == '__main__':
    main()
    unittest.main()
