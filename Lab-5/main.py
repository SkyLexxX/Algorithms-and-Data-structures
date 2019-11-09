import math


def check_equal(heights):
    return len(set(heights)) <= 1


def calculate_electrical_wire(distance, heights):
    result = []
    all_lenght = []
    if check_equal(heights):
        result.append((len(heights)-1) * int(distance))
        total_sum = sum(result)
        return total_sum
    else:
        for i in range(0, len(heights)-1):
            y = math.fabs(heights[i] - heights[i+1])
            c = math.sqrt(pow(y, 2) + pow(int(distance), 2))
            all_lenght.append(c)
            y, c = 0, 0
        total_sum = sum(all_lenght)
        return total_sum


# distance = 2
# heights = [3, 3, 3]
# print(calculate_electrical_wire(distance, heights))

def main():
    distance = input("Enter a distance between columns: ")
    # print(distance)
    heights = list(map(int, input("Enter a heights of columns: ").split()))
    # print("List of heights: ", heights)
    print(calculate_electrical_wire(distance, heights))


if __name__ == '__main__':
    main()
