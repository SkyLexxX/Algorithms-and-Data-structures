from itertools import permutations


def translate_string_to_list(beer, list_of_likes):
    translated_list = []
    for index in range(0, int(beer)):
        translated_list.append(list())

    for i in range(0, len(list_of_likes)):
        for j in range(0, int(beer)):
            if list_of_likes[i][j] == "Y":
                translated_list[j].insert(j, i + 1)
    return translated_list


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
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


def main():
    employee, beer = input("Enter a two value: ").split()
    list_of_likes = list(map(str, input("Enter a string of beer likes: ").split()))
    print(list_of_likes)

    input_list = translate_string_to_list(beer, list_of_likes)
    merged_combination_list = my_combo(input_list)
    print("\nSolution\n")
    result_search = solution(merged_combination_list, set(merged_combination_list[-1]))
    print(beer_identifier(result_search, input_list, set(merged_combination_list[-1])), result_search)


if __name__ == '__main__':
    main()
