n,k=map(int,input().split())
ar=list(map(int,input().split()))
ar.sort()
i=0
j=n-1
flag=0
while(i<j):
    if ar[i]+ar[j]==k:
        flag=1
        break
    elif ar[i]+ar[j]>k:
        j-=1
    elif ar[i]+ar[j]<k:
        i+=1
print('YES' if flag==1 else 'NO')