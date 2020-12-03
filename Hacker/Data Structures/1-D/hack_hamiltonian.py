n=int(input())
ar=list(map(int,input().split()))
l=[]
for i in range(len(ar)-1):
    c = 0
    ele=ar[i]
    for j in range(i+1,len(ar)):
        if ar[j]>ele:
            c+=1
        else:
            continue
    if c>0:
        continue
    else:
        l.append(ele)
l.append(ar[-1])
print(*l)

n=int(input())
ar=list(map(int,input().split()))
l=[]
l.append(ar[-1])
ar=ar[::-1]
ele=ar[0]
for i in range(1,len(ar)):
    if(ar[i]>=ele):
        l.append(ar[i])
        ele=ar[i]
print(*l[::-1])
