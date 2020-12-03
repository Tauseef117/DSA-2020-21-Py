n,x,y=map(int,input().split())
arr=list(map(int,input().split()))
list=[int(i) for i in range(x,y+1)]
Flag=0
for i in arr:
    if i in range(x,y+1):
        Flag=0
    else:
        Flag=1
if Flag==0:
    print('YES')
else:
    print('NO')
