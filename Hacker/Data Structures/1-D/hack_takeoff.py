for _ in range(int(input())):
    n,p,q,r=map(int,input().split())
    a=[]
    b=[]
    c=[]
    for i in range(1,n+1):
        if p*i<=n:
            a.append(p*i)
        if q*i<=n:
            b.append(q*i)
        if r*i<=n:
            c.append(r*i)
    a=set(a)
    b=set(b)
    c=set(c)
    all=a.union(b).union(c)
    same_day=a.intersection(b).union((b).intersection(c)).union((a).intersection(c))
    print(len(all)-len(same_day))