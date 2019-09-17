import time

import read_from_file
import sort


def main():
    list_of_hotels = read_from_file.read_from_file("data.txt")
    visitors = []
    rooms = []

    for i in list_of_hotels:
        rooms.append(i.amount_of_rooms)
        visitors.append(i.amount_of_visitors)
    print(visitors)
    print(rooms)

    print("Selection sort by visitors:")
    start_sel = time.time()
    print(sort.sel_sort(visitors))
    print("%f s" % (time.time() - start_sel))

    print("Merge sort by rooms:")
    start_sel1 = time.time()
    print(sort.merge_sort(rooms))
    print(time.time() - start_sel1)
    print(sort.counter)


if __name__ == '__main__':
    main()
