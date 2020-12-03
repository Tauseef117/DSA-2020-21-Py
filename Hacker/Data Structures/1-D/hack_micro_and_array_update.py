for _ in range(int(input())):
    n, k =map(int,input().split())
    arr=min(map(int,input().split()))
    if arr>=k:
        print('0')
    else:
        print(len(range(arr,k)))

for _ in range(int(input())):
    n, k =map(int,input().split())
    arr=list(map(int,input().split()))
    arr=sorted(arr)
    ele=arr[0]
    if ele>=k:
        print('0')
    else:
        print(len(range(ele,k)))