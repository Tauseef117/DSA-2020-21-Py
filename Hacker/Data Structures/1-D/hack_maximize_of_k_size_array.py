n,k=map(int,input().split())
ar=list(map(int,input().split()))
l=[]
b=0
for i in range(len(ar)-k+1):
    a=ar[b:b+k]
    b+=1
    ele=max(a)
    l.append(ele)
print(*l)
