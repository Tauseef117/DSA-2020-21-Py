n=int(input())
ar=list(map(int,input().split()))
a=0
for i in range(n):
    a+=ar[i]
    a*=10
if(a%11==0):
    print('YES')
else:
    print('NO')
