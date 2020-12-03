n,x=map(int,input().split())
ar=list(map(int,input().split()))
c=0
ma=max(ar)
if x>=ma:
    print(len(ar))
    exit()
else:
    for i in range(len(ar)):
        if c == 2:
            print(i - 2)
            exit()
        elif ar[i] > x:
            c += 1
    if c == 1:
        print(len(ar) - 1)







