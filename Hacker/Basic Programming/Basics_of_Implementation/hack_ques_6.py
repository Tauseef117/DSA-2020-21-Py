for _ in range(int(input())):
    n = int(input())
    m = 0
    for i in range(n):
        for j in range(i, n - 1):
            print('', end=' ')
        for k in range(i + m + 1):
            print('*', end='')
        m += 1
        print('\t')