for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        ele=list(map(int,input().split()))
        l.append(ele)
    c=0
    for i in range(n):
        for j in range(n):
            for p in range(i,n):
                for q in range(j,n):
                    if(l[i][j]>l[p][q]) and (i<=p and j<=q):
                        c+=1
    print(c)