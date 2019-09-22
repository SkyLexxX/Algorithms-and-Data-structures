def calendar(intervals):
    sorted_intervals = sorted(intervals)
    index = 0
    while index < len(sorted_intervals) - 1:
        if sorted_intervals[index][0] <= sorted_intervals[index + 1][0] <= sorted_intervals[index][1]:
            sorted_intervals[index] = (sorted_intervals[index][0],
                                       max(sorted_intervals[index][1], sorted_intervals[index + 1][1]))
            sorted_intervals.pop(index + 1)
            index -= 1
        index += 1
    return sorted_intervals


def main():
    intervals = [(1, 3), (1, 1), (2, 6), (8, 10), (15, 18), (0, 4), (1, 1)]
    print(calendar(intervals))


if __name__ == '__main__':
    main()
