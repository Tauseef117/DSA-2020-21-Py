n=int(input())
arr=list(map(int,input().split()))
min=min(arr)
max=max(arr)
list=[int(i) for i in range(min,max+1)]
if set(list)==set(arr):
    print('YES')
else:
    print('NO')