arr = [[1, 2, 3], [4, 5, 6], [2, 3, 4, 5]]
# arr = [[1, 2, 3], [4, 5, 6], [2, 3, 4, 5], [7], [8], [9], [10], [11], [12]]
# arr = [[1, 2, 3], [4, 5, 6], [2, 3, 4, 5, 7], [1]]
# arr = [[1], [2]]


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def merge(array):
    merged_list = []
    for i in array:
        for j in i:
            merged_list.append(list(sum(j, [])))
    return merged_list


def my_combo(array):
    result = []
    for i in range(1, len(array) + 1):
        result.append(list(combinations(array, i)))
    result = merge(result)
    return result


def beer_identifier(result, start, users):
    amount_of_beer = []
    check = []
    for idx, i in enumerate(start):
        temp = i
        if all(x in result for x in temp):
            if len(set(check)) == len(users):
                return amount_of_beer
            elif all(z in check for z in i):
                continue
            else:
                check += i
                amount_of_beer.append(idx + 1)
    return amount_of_beer


def solution(combination, number_of_employees):
    for i in combination:
        if len(set(i)) == len(number_of_employees):
            return i


print(my_combo(arr))
last = my_combo(arr)
print("\nSolution\n")
res = solution(last, set(last[-1]))
print(beer_identifier(res, arr, set(last[-1])), res)
