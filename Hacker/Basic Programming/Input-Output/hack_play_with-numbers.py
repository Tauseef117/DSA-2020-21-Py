n,q=map(int,input().split())
num=list(map(int,input().split()))
for i in range(q):
    l,r=map(int,input().split())
    total = 0
    count = 0
    for j in range(l,r+1):
        total=total+num[j]
        count+=1
    print(total//count)

n, q = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
for i in range(1, n):
    arr[i] = arr[i] + arr[i - 1]

for i in range(q):
    l, r = map(int, input().split(" "))
    n = r - l + 1
    if l == 1:
        val = arr[r - 1]
    else:
        val = arr[r - 1] - arr[l - 2]
    print(val // n)