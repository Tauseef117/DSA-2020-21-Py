for _ in range(int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    for k in range(int(input())):
        a=int(input())
        if a in ar:
            print('Yes')
        else:
            print('No')