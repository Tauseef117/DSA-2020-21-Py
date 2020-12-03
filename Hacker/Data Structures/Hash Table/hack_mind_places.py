n,m=map(int,input().split())
l=[]
for _ in range(n):
    ele=list(map(int,input().split()))
    l.append(ele)
for _ in range(int(input())):
    flag=0
    a=int(input())
    for i in range(n):
        for j in range(m):
            if l[i][j]==a:
                print(i,j)
                flag=1
                continue
    if flag==0:
        print('-1 -1')