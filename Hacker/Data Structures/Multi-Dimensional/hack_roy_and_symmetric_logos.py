for _ in range(int(input())):
    n=int(input())
    l=[]
    x = 0
    y = 0
    for i in range(n):
        ele=list(map(int,input()))
        l.append(ele)
    for i in range(n):
        j=n-i-1
        for k in range(n):
            if l[i][k]!=l[j][k]:
                x=1
    for i in range(n):
        j = n - i - 1
        for k in range(n):
            if l[k][i]!=l[k][j]:
                y=1
    if x == 1 or y == 1:
        print('NO')
    else:
        print('YES')

for _ in range(int(input())):
    n=int(input())
    l=[]
    x,y=0,0
    for i in range(n):
        ele=list(map(int,input()))
        l.append(ele)
    for i in range(n):
        j=n-i-1
        for k in range(n):
            if l[i][k]!=l[j][k]:
                x=1
        for k in range(n):
            if l[k][i]!=l[k][j]:
                y=1
    print('NO' if x==1 or y==1 else 'YES' )