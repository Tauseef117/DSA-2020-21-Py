n=int(input())
if n==0:
    print('NO')
else:
    print('YES')
    b=bin(n)[2:][::-1]
    print(b.count('1'))
    for i in range(len(b)):
        if b[i]=='1':
            print(i,end=' ')
