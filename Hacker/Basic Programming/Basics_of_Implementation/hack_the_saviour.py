# res = list(zip(arr, arr[1:] + arr[:1]))
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for p1 in range(len(arr)):
        for p2 in range(p1 + 1, len(arr)):
            if (arr[p1]==arr[p2]) or (((arr[p1]+arr[p2])%2)!=0):
                continue
            else:
                count+=1
    print(count)
