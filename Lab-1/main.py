from time import perf_counter

from Hotel import Hotel
import Selection_sort


def main():
    mariott = Hotel("Mariott", 1000, 50000)
    hilton = Hotel("Hilton", 900, 15000)
    kempinski = Hotel("Kempinski", 1560, 20000)
    inter_continental = Hotel("InterContinental", 1100, 24000)

    # visitors = [mariott.amount_of_visitors, hilton.amount_of_visitors, kempinski.amount_of_visitors,
    #             inter_continental.amount_of_visitors]
    # rooms = [mariott.amount_of_rooms, hilton.amount_of_rooms, kempinski.amount_of_rooms,
    #          inter_continental.amount_of_rooms]

    visitors = [mariott.amount_of_visitors, hilton.amount_of_visitors, kempinski.amount_of_visitors]
    rooms = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

    print("visitors - ", str(visitors))
    print("rooms - ", str(rooms))

    print("mariott - ", str(mariott))
    print("hilton - ", str(hilton))
    print("kempinski - ", str(kempinski))
    print("inter_continental - ", str(inter_continental))

    print("Selection sort by visitors:")
    start_point_sel_visitors = perf_counter()
    Selection_sort.sel_sort(visitors)
    end_point_sel_visitors = perf_counter()
    print("\tTime Complexity: " + str(end_point_sel_visitors - start_point_sel_visitors))

    print("Selection sort by rooms:")
    start_point_sel_rooms = perf_counter()
    Selection_sort.sel_sort(rooms)
    end_point_sel_rooms = perf_counter()
    print("\tTime Complexity: " + str(end_point_sel_rooms - start_point_sel_rooms))

    print("Merge sort by visitors:")
    start_point_merge_visitors = perf_counter()
    Selection_sort.merge_sort(visitors)
    Selection_sort.print_list(visitors)
    end_point_merge_visitors = perf_counter()
    print("\tTime Complexity: " + str(end_point_merge_visitors - start_point_merge_visitors))

    print("Merge sort by rooms:")
    start_point_merge_rooms = perf_counter()
    Selection_sort.merge_sort(rooms)
    Selection_sort.print_list(rooms)
    end_point_merge_rooms = perf_counter()
    print("\tTime Complexity: " + str(end_point_merge_rooms - start_point_merge_rooms))


if __name__ == '__main__':
    main()
