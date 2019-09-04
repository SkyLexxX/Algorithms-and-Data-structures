# def selection_sort(hotel):
#     start_time = time.time()
#     swap = 0
#     comparison = 0
# 
#     # Traverse through all array elements
#     for i in range(len(hotel)):
#         # print(hotel)
#         # print("i = " + str(i))
#
#         # Find the minimum element in remaining
#         # unsorted array
#         min_idx = i
#         for j in range(i + 1, len(hotel)):
#             # print("j = " + str(j))
#             comparison += 1
#             if hotel[min_idx] > hotel[j]:
#                 min_idx = j
#
#         swap += 1
#         # Swap the found minimum element with
#         # the first element
#         # hotel[i], hotel[min_idx] = hotel[min_idx], hotel[i]
#
#         temp = hotel[i]
#         hotel[i] = hotel[min_idx]
#         hotel[min_idx] = temp
#
#     for i in range(len(hotel)):
#         print("\t" + "%d" % hotel[i])
#     print("--- %s seconds ---" % (time.time() - start_time))
#     print("swap = " + str(swap))
#     print("comparison = " + str(comparison))
#     print()


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

    for i in range(len(hotel)):
        print("\t" + "%d" % hotel[i])
    print("\tswap = " + str(swap))
    print("\tcomparison = " + str(comparison))
    print()


# Python program for implementation of MergeSort
def mergeSort(hotel):
    if len(hotel) > 1:
        mid = len(hotel) // 2  # Finding the mid of the array
        L = hotel[:mid]  # Dividing the array elements
        R = hotel[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        # while i > len(L) and j > len(R): - changing order of sorting
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                hotel[k] = L[i]
                i += 1
            else:
                hotel[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            hotel[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            hotel[k] = R[j]
            j += 1
            k += 1


def print_list(hotel):
    for i in range(len(hotel)):
        print("\t" + "%d" % hotel[i])
    print()
