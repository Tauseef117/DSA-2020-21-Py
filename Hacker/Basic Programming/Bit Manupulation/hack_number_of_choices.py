for _ in range(int(input())):
    n, k =map(int,input().split())
    arr=list(map(int,input().split()))
    l=[]
    for i in arr:
        a=bin(i)
        b=a.count('1')
        l.append(b)
    ar=sorted(l,reverse=True)[:k]
    print(sum(ar))