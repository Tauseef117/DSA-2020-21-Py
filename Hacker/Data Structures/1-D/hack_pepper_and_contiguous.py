for _ in range(int(input())):
    n=int(input())
    ar = list(map(int, input().split()))
    c=0
    l=[-1]
    for i in range(len(ar)):
        if ar[i]%2==0:
            c+=1
            l.append(c)
        else:
            c=0
    print(l)
    print(max(l))