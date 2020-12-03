n,q=map(int,input().split())
arr=list(map(int,input().split()))
for _ in range(q):
    l, r = map(int, input().split())
    c = 0
    for i in range(l, r+1):
        a = str(bin(arr[i][2:]))
        if '11' in a:
            c += 1
    print(c)
