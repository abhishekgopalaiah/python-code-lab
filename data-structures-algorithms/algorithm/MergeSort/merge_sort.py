def merge(left, right):
    # Initialize an empty list to hold the merged output
    sorted_array = []
    i = j = 0

    # Traverse both arrays and insert the smaller element into the sorted_array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Collect remaining elements from left, if any
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # Collect remaining elements from right, if any
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array


def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sorting the first half
        left_sorted = merge_sort(left_half)

        # Sorting the second half
        right_sorted = merge_sort(right_half)

        # Merging the sorted halves
        return merge(left_sorted, right_sorted)
    else:
        # Base case: the array is already sorted if it has one or no element
        return arr


if __name__ == '__main__':
    arr = [21, 38, 43, 3, 9, 82, 10, 13]
    sorted_array = merge_sort(arr)
    print("Sorted array is:", sorted_array)
