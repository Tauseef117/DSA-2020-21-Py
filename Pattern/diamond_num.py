def print_pattern (n):

    # val variable for value of each element
    val = 1

    # For printing the upper half of pattern
    # Outer for loop for number of rows
    for row in range(1, n + 1):

        # Inner for loop for printing space
        # in each line there will be n - row spaces
        for j in range(n - row):
            print (" ",end = " ")

        # printing numbers
        # for each row we have 2 * row -1 elements
        # in second row we have 2 * 2 -1 elements
        for k in range(1, 2 * row):

            if k < row:
                print (val, end = " ")
                val += 1
            elif k == row:
                print (val, end = " ")
            else:
                val -= 1
                print (val, end = " ")

        # move to next row
        print ()

    # For printing the lower half of pattern
    for row in range(n - 1, 0, -1):

        # Inner for loop for printing space
        # in each line there will be n - row spaces
        for j in range(n - row):
            print (" ", end = " ")

        # printing numbers
        # for each row we have 2 * row -1 elements
        for k in range(1, 2 * row):

            if k < row:
                print (val, end = " ")
                val += 1
            elif k == row:
                print (val, end = " ")
            else:
                val -= 1
                print (val, end = " ")

        # move to next row
        print()

# Driver code
n = 6
print_pattern(n)

# This code is contributed by Tauseef Ahmed _