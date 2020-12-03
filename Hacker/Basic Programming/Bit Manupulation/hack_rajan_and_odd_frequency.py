from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
l=Counter(arr)
for i,j in l.items():
    if j%2!=0:
        print(i)
        exit()
