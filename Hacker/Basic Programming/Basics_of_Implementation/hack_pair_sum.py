a,b = map(int,input().split())
arr=list(map(int,input().split()))
for i in arr:
    for j in arr:
        if i!=j and i+j==b:
            print('YES')
            exit()
else:
    print('NO')