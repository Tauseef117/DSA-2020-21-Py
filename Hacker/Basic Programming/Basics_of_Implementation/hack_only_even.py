for i in range(int(input())):
    n=int(input())
    count=0
    arr=list(map(int,input().split()))
    for k in range(len(arr)):
        for l in range(k,len(arr)):
            if arr[l]%2==0:
                count=count+len(arr)-l
                break
    print(count)


