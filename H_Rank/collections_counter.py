from collections import Counter
n=int(input())
ar=list(map(int,input().split()))
ar=Counter(ar)
s=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a in ar.keys():
        if ar[a]>=1:
            ar[a]=ar[a]-1
            s=s+b
print(s)