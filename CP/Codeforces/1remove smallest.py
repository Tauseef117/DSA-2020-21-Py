for _ in range(int(input())):
    n=int(input())
    ar=sorted(list(set(map(int,input().split()))))
    c=0
    d=0
    if len(ar)==1:
        print('YES')
        c=1
        continue
    else:
        for i in range(len(ar)-1):
            if abs(ar[i]-ar[i+1])==1 or abs(ar[i]-ar[i+1]==0):
                d+=1
            if len(ar)-d == 1:
                print('YES')
                c=1
                break
        if c==0:
            print('NO')