for _ in range(int(input())):
    n,m=map(int,input().split())
    ar=list(map(int,input().split()))
    a=set(ar[:n])
    for i in range(n,n+m):
        if a[i] in a:
            print('YES')
        else:
            print('NO')
            a.add(a[i])