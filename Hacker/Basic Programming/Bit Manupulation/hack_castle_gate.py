for _ in range(int(input())):
    n=int(input())
    count=0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i^j<=n:
                count+=1
            else:
                continue
    print(count)