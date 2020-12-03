n=int(input())
arr=list(map(int,input().split()))
ele=arr.index(max(arr))
arr=arr[:ele+1]
l=[]
while(len(arr)>0):
    a=0
    for i in range(0,len(arr)):
        a=a^arr[i]
    l.append(a)
    ele = arr.index(max(arr))
    arr=arr[1:ele+1]
print(max(l))


