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


def merge(left_side, right_side):
    left_index, right_index = 0, 0
    result = []
    # iterate through both left and right sublist
    while left_index < len(left_side) and right_index < len(right_side):
        # if left value is lower than right then append it to the result
        if left_side[left_index] <= right_side[right_index]:
            result.append(left_side[left_index])
            left_index += 1
        else:
            # if right value is lower than left then append it to the result
            result.append(right_side[right_index])
            right_index += 1
    # concatenate the rest of the left and right sublists
    result += left_side[left_index:]
    result += right_side[right_index:]
    # return the result
    return result


def merge_sort(hotel):
    # if list contains only 1 element return it
    if len(hotel) <= 1:
        return hotel
    else:
        # split the lists into two sublists and recursively split sublists
        middle_point = int(len(hotel) / 2)
        left_sublist = merge_sort(hotel[:middle_point])
        right_sublist = merge_sort(hotel[middle_point:])
        # return the merged list using the merge_list function above
        return merge(left_sublist, right_sublist)
