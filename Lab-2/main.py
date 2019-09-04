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
    si = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for tup in si:
        if not merged:
            merged.append(tup)
        else:
            b = merged.pop()
            if b[1] >= tup[0]:
                new_tup = (b[0], max(b[1], tup[1]))
                merged.append(new_tup)
            else:
                merged.append(b)
                merged.append(tup)
    return merged


def main():
    thisarray = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    print("Original list of ranges: {}".format(thisarray))
    merged_list = calendar(thisarray)
    print("List of ranges after merge_ranges: {}".format(merged_list))


if __name__ == '__main__':
    main()
    unittest.main()
