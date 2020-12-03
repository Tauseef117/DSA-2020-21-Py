def dis(a,b,ar):
    c,k=0,0
    for i in range(1,len(ar)+1):
        if a in ar[i-1]:
            k = i
        else:
            continue
    for i in range(len(ar)):
        if b in ar[i-1]:
            c = i
        else:
            continue
    if c < k:
        print(len(range(c, k)))
    else:
        c,k= k, c
        print(len(range(c, k)))

n,k=map(int,input().split())
ar1=[]
for i in range(1,k+1):
    ar2=list(map(int,input().split()))
    if ar2[0]!=0:
        ar2=ar2[1:]
    ar1.append(ar2)
q = int(input())
for i in range(1, q + 1):
    a, b = map(int, input().split())
    for i in ar1:
        if a in i and b in i:
            print('0')
            break
    else:
        dis(a,b,ar1)



