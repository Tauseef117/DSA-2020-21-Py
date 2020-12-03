print('Enter odd number greater than 4')
n = int(input())
l = n//2
m = n//2
r = 1
for i in range(n):
    if i < (n//2):
        for k in range(l):
            print(end=' ')
        for j in range(i + 1):
            print('*', end=' ')
        print('\t')
        l -= 1
    elif i == n//2:
        for j in range(n//2+1):
            print('*', end=' ')
        print('\t')
    elif i > (n//2):
        for k in range(r):
            print(end=' ')
        r += 1
        for j in range(m):
            print('*', end=' ')
        print('\t')
        m -= 1
