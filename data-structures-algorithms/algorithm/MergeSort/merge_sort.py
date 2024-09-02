def merge(left, right, arr):
    # Initialize pointers for left, right, and the merged array
    i = j = k = 0

    # Traverse both subarrays and insert the smaller element into the merged array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements of left, if any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements of right, if any
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sorting the first half
        merge_sort(left_half)

        # Sorting the second half
        merge_sort(right_half)

        # Merging the sorted halves
        merge(left_half, right_half, arr)


if __name__ == '__main__':
    arr = [21, 38, 43, 3, 9, 82, 10, 13]
    merge_sort(arr)
    print("Sorted array is:", arr)
