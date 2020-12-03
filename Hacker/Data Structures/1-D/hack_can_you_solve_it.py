for _ in range(int(input())):
    n=int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    a=[]
    for i in range(len(ar)-1):
        for j in range(i,len(ar)):
            print(ar[i],ar[j])
            val=abs(ar[i] - ar[j]) ^ abs(i-j)
            if val==0:
                continue
            else:
                a.append(val)
    print(max(a))