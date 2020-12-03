from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
ar=Counter(arr)
list=[]
for i,j in ar.items():
    if ar[i]==1:
        list.append(i)
list.sort()
print(*list)
