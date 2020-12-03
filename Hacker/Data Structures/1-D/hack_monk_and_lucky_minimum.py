for _ in range(int(input())):
    n=int(input())
    arr = list(map(int, input().split()))
    if arr.count(min(arr))%2==0:
        print('Unlucky')
    else:
        print('Lucky')

for _ in range(int(input())):
    n=int(input())
    arr = list(map(int, input().split()))
    mi=min(arr)
    a=arr.count(mi)
    if a%2==0:
        print('Unlucky')
    else:
        print('Lucky')