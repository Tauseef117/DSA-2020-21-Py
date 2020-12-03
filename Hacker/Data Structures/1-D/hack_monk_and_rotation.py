import collections

for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    a = collections.deque(arr)
    a.rotate(q)
    print(*a)

for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    x = q % n
    print(*(arr[n - x:] + (arr[:n - x])))

ar=[1,2,3,4,5]
n,q=5,2
x=2%5
ar[5-2:]+ar[:5-2]
ar[4,5]+ar[1,2,3]