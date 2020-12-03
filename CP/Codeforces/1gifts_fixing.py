for _ in range(int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    ya=list(map(int,input().split()))
    a=min(ar)
    b=min(ya)
    c=0
    for i in range(n):
        x=abs(a-ar[i])
        y=abs(b-ya[i])
        z=min(x,y)
        c=c+x+y-z
    print(c)