def prod(x):
    print(x[0] * x[1] * x[2])

n=int(input())
ar=list(map(int,input().split()))
for i in range(len(ar)):
    if i==0 or i==1:
        print('-1')
    elif i==2:
        print(ar[0]*ar[1]*ar[2])
    else:
        prod(sorted(ar[:i+1],reverse=True)[:3])
s