n=int(input())
arr=list(map(int,input().split()))
l=len(arr)
L=[]
for i in range(l):
    length=len(arr)
    if length>=6:
        i=0
        ss=arr[i]+(arr[i+1]+arr[i+2])+(arr[i+3]+arr[i+4]+arr[i+5])
        L.append(ss)
        del arr[0]
        continue
    elif length>=3:
        i=0
        ss = arr[i] + (arr[i+1] + arr[i+2])
        L.append(ss)
        del arr[0]
        continue
    elif length>=1:
        i=0
        ss = arr[i]
        L.append(ss)
        del arr[0]
        continue
    else:
        break
print(max(L))