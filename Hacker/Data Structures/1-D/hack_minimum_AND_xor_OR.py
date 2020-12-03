for _ in range(int(input())):
    n=int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    a=[]
    for i in range(len(ar)-1):
        val = (ar[i] and ar[i+1]) ^ (ar[i] or ar[i+1])
        a.append(val)
    print(min(a))