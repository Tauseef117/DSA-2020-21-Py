def merge_Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_Sort(left_half)
        merge_Sort(right_half)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                # The value from the left_half half has been used
                arr[k] = left_half[i]
                # Move the iterator forward
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_Sort(arr)
print(arr)