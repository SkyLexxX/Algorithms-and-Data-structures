import math
import sys


class Column:
    def __init__(self, max, current):
        self.min = 1
        self.max = max
        self.current = current


def check_equal(heights):
    res = []
    for i in heights:
        res.append(i.max)
    return len(set(res)) <= 1 and heights[0].max == 1


def height_definition_remake(distance, heights):
    result = []
    last_item = None
    if check_equal(heights):
        result.append((len(heights) - 1) * int(distance))
        total_sum = sum(result)
        return total_sum
    else:
        if len(heights) % 2 == 0:
            last_item = False
        else:
            last_item = heights.pop()
        if math.fabs(heights[0].min - heights[1].max) > math.fabs(heights[0].max - heights[1].min):
            heights[0].current = heights[0].min
        else:
            heights[0].current = heights[0].max
        for i in range(0, len(heights) - 1):
            if math.fabs(heights[i].current - heights[i + 1].max) > math.fabs(heights[i].current - heights[i + 1].min):
                heights[i + 1].current = heights[i + 1].max
            else:
                heights[i + 1].current = heights[i + 1].min
        if last_item:
            if math.fabs(heights[-1].current - last_item.max) > math.fabs(heights[-1].current - last_item.min):
                last_item.current = last_item.max
                heights.append(last_item)
            else:
                last_item.current = last_item.min
                heights.append(last_item)
        return heights


def calculate_electrical_wire(distance, heights):
    all_lenght = []
    if len(set(heights)) <= 1:
        return sys.exit()
    else:
        for i in range(0, len(heights) - 1):
            y = math.fabs(heights[i] - heights[i + 1])
            c = math.sqrt(pow(y, 2) + pow(int(distance), 2))
            all_lenght.append(c)
            y, c = 0, 0
        total_sum = sum(all_lenght)
        return total_sum


def main():
    result = []
    distance = input("Enter a distance between columns: ")
    heights = list(map(int, input("Enter a heights of columns: ").split()))

    objs = [Column(None, None) for i in range(len(heights))]
    for obj in range(len(objs)):
        objs[obj].max = heights[obj]

    print(height_definition_remake(distance, objs))
    for i in objs:
        print(i.current)
        result.append(i.current)
    print(calculate_electrical_wire(distance, result))


if __name__ == '__main__':
    main()
