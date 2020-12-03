def flip(a):
    if a==0:
        return 1
    else:
        return 0
n,q=map(int,input().split())
ar=list(map(int,input().split()))
for i in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        b=a[1]
        ar[b-1]=flip(ar[b-1])
    else:
        c = a[1]
        d = a[2]
        if ar[d-1]==1:
            print('ODD')
        else:
            print('EVEN')


