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


counter = 0


def compare(left, right):
    global counter
    counter = counter + 1
    return left <= right


def merge(left_side, right_side):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left_side) and right_index < len(right_side):
        if compare(left_side[left_index], right_side[right_index]):
            result.append(left_side[left_index])
            left_index += 1
        else:
            result.append(right_side[right_index])
            right_index += 1
    result += left_side[left_index:]
    result += right_side[right_index:]
    return result


def merge_sort(hotel):
    if len(hotel) <= 1:
        return hotel
    else:
        middle_point = int(len(hotel) / 2)
        left_side = merge_sort(hotel[:middle_point])
        right_side = merge_sort(hotel[middle_point:])
        return merge(left_side, right_side)
