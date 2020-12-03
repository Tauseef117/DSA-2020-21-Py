for _ in range(int(input())):
    n=input()
    l=len(n)
    n=set(n)
    le=len(n)
    ar=[]
    for i in n:
        ar.append(int(i))
    if len(n)==len(range(min(ar),max(ar)))+1 and l==le:
        print('YES')
    else:
        print('NO')