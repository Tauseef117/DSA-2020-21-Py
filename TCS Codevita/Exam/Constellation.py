n = int(input())
one = list(input().split())
two = list(input().split())
three = list(input().split())
i = 0
while (i < n - 2):

    if one[i] == '#':
        print('#', end="")
        i +=1
        continue

    elif one[i] == '*' and one[i + 1] == '.' and one[i + 2] == '*':
        if two[i] == '*' and two[i + 1] == '.' and two[i + 2] == '*':
            if three[i] == '*' and three[i + 1] == '*' and three[i + 2] == '*':
                print('U', end="")
                i +=3
                continue

    elif one[i] == '*' and one[i + 1] == '*' and one[i + 2] == '*':
        if two[i] == '*' and two[i + 1] == '.' and two[i + 2] == '*':
            if three[i] == '*' and three[i + 1] == '*' and three[i + 2] == '*':
                print('O', end="")
                i += 3
                continue

        elif two[i] == '.' and two[i + 1] == '*' and two[i + 2] == '.':
            if three[i] == '*' and three[i + 1] == '*' and three[i + 2] == '*':
                print('I', end="")
                i += 3
                continue

        elif two[i] == '*' and two[i + 1] == '*' and two[i + 2] == '*':
            if three[i] == '*' and three[i + 1] == '*' and three[i + 2] == '*':
                print('E', end="")
                i += 3
                continue

    elif one[i] == '.' and one[i + 1] == '*' and one[i + 2] == '.':
        if two[i] == '*' and two[i + 1] == '*' and two[i + 2] == '*':
            if three[i] == '*' and three[i + 1] == '.' and three[i + 2] == '*':
                print('A', end='')
                i += 3
                continue
    else:
        i += 1
