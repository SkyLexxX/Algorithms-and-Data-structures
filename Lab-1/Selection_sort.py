def sel_sort(hotel):
    swap = 0
    comparison = 0
    for i in range(len(hotel)):
        min_value = i
        for j in range(i + 1, len(hotel)):
            comparison += 1
            if hotel[min_value] > hotel[j]:
                min_value = j
        temp = hotel[i]
        hotel[i] = hotel[min_value]
        hotel[min_value] = temp
        swap += 1

    for i in range(len(hotel)):
        print("\t" + "%d" % hotel[i])
    print("\tswap = " + str(swap))
    print("\tcomparison = " + str(comparison))
    print()


def merge_sort(hotel):
    if len(hotel) > 1:
        middle_point = len(hotel) // 2

        left_side = hotel[:middle_point]
        right_side = hotel[middle_point + 1:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = 0
        j = 0
        k = 0
        # merge_comparison = 0
        # merge_swap = 0

        while i < len(left_side) and j < len(right_side):
            # merge_comparison += 1
            if left_side[i] < right_side[j]:
                # merge_swap += 1
                hotel[k] = left_side[i]
                i += 1
            else:
                # merge_swap += 1
                hotel[k] = right_side[i]
                j = +1
            k += 1
    # print(merge_comparison, merge_swap)


def print_list(hotel):
    for i in range(len(hotel)):
        print("\t" + "%d" % hotel[i])
    print()
