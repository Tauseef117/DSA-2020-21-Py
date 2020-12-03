def seq_search(arr, ele):
    """
    General Sequential Search. Works on Unordered lists.
    """
    # Start at position 0
    pos = 0
    # Target becomes true if ele is in the list
    found = False

   # go until end of list
    while pos < len(arr) and not found:
        # If match
        if arr[pos] == ele:
            found = True
        # Else move one down
        else:
            pos = pos + 1
    return found
arr = [1, 9, 2, 8, 3, 4, 7, 5, 6]
print(seq_search(arr, 1))


def ordered_seq_search(arr, ele):
    """
    Sequential search for an Ordered list
    """
    # Start at position 0
    pos = 0

    # Target becomes true if ele is in the list
    found = False

    # Stop marker
    stopped = False

    # go until end of list
    while pos < len(arr) and not found and not stopped:

        # If match
        if arr[pos] == ele:
            found = True

        else:

            # Check if element is greater
            if arr[pos] > ele:
                stopped = True

            # Otherwise move on
            else:
                pos = pos + 1

    return found


arr.sort()
ordered_seq_search(arr, 3)
