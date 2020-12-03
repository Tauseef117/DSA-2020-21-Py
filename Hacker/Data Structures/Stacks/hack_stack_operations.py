n,k=map(int,input().split())
arr=list(map(int,input().split()))
if k==n:
    print('-1')
elif n==1 and k%2!=0:
    print('-1')
elif k>n:
    print(max(arr))
else:
    print(max(max(arr[:k-1]),arr[k]))