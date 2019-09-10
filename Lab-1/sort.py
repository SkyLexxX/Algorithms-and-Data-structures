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
    return hotel, swap, comparison


def merge(hotel):
    if len(hotel) <= 1:
        return hotel

    middle_point = len(hotel) // 2

    left_side = hotel[:middle_point]
    right_side = hotel[middle_point:]

    merge(left_side)
    merge(right_side)

    return merge_sort(left_side, right_side)


def merge_sort(left_side, right_side):
    merge_comparison, merge_swap = 0, 0
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left_side) and right_index < len(right_side):
        merge_comparison += 1
        if left_side[left_index] < right_side[right_index]:
            merge_swap += 1
            result.append(left_side[left_index])
            left_index += 1
        else:
            result.append(right_side[right_index])
            right_index += 1

    result += left_side[left_index:]
    result += right_side[right_index:]
    return result, merge_swap, merge_comparison
