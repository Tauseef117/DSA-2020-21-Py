def isPossible(l, m, x, y):
    if (l * m == x + y):
        return True;

    return False;


# Driver code
if __name__ == "__main__":

    l = 3;
    m = 2;
    x = 4;
    y = 2;

    if (isPossible(l, m, x, y)):
        print("True");
    else:
        print("No");