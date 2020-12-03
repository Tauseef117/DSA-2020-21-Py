for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    m=max(arr)
    sm=sum(arr)-m
    if m<sm:
        print('Yes')
    else:
        print('No')