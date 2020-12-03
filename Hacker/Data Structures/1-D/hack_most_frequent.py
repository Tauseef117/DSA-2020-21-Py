from collections import Counter
a=int(input())
n=list(map(int,input().split()))
n=Counter(n)
for i,j in n.most_common(1):
    print(i)

n=int(input())
arr=list(map(int, input().split()))
ar_sortd=list(set(arr))
ar_sortd.sort()
li=[]
for i in ar_sortd:
    li.append(arr.count(i))
print(ar_sortd[li.index(max(li))])