from time import perf_counter

import read_from_file
import sort


def main():
    list_of_hotels = read_from_file.read_from_file("data.txt")

    mariott = list_of_hotels[0]
    hilton = list_of_hotels[1]
    kempinski = list_of_hotels[2]
    inter_continental = list_of_hotels[3]

    visitors = [mariott.amount_of_visitors, hilton.amount_of_visitors, kempinski.amount_of_visitors,
                inter_continental.amount_of_visitors]
    rooms = [mariott.amount_of_rooms, hilton.amount_of_rooms, kempinski.amount_of_rooms,
             inter_continental.amount_of_rooms]

    print("Selection sort by visitors:")
    start_point_sel_visitors = perf_counter()
    print(sort.sel_sort(visitors))
    end_point_sel_visitors = perf_counter()
    print("\tTime Complexity: " + str(end_point_sel_visitors - start_point_sel_visitors))

    print("Merge sort by rooms:")
    start_point_merge_rooms = perf_counter()
    print(sort.merge(rooms))
    end_point_merge_rooms = perf_counter()
    print("\tTime Complexity: " + str(end_point_merge_rooms - start_point_merge_rooms))


if __name__ == '__main__':
    main()
