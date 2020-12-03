n,k=map(int,input().split())
arr=list(map(int,input().split()))
ini_sum=sum(arr[:k])
last_sum=ini_sum
for i in range(1,k):
    last_sum+= arr[-i] - arr[k - i]
    if last_sum>=ini_sum:
        ini_sum=last_sum
print(ini_sum)