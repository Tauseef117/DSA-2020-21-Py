n=int(input())
num=n
for i in range(n):
    num=n
    for j in range(n-i):
        print(num,end=' ')
        num-=1
    print('\t')
print('\n')

for i in range(n):
    num=n
    for j in range(i+1):
        print(num,end=' ')
        num-=1
    print('\t')
print('\n')

num=n
for i in range(n):
    for j in range(n-i):
        print(num,end=' ')
    num-=1
    print('\t')
print('\n')

for i in range(0, n): #5
    for j in range(0, n-1-i): #4 empty spaces
        print(' ',end="") #=print(end=" ")
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")
print('\n')

k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")
print('\n')

for i in range(int(input())):
    n = int(input())
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end=' ')
        for k in range(2 * n - 2 * i):
            print('#', end=' ')
        for l in range(i):
            print('*', end=' ')
        print('\t')


