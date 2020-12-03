for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    l=[]
    for i in range(n):
        if len(l)==0:
            l.append(arr[i])
        else:
            while(k>0 and len(l)>0 and l[-1]<arr[i]):
                l.pop()
                k-=1
            l.append(arr[i])
    print(*l)
