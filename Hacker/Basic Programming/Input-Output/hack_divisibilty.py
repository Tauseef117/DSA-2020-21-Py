t=int(input())
n=list(map(int,input().split()))
str_is=''
for i in n:
    last=str(i%10)
    str_is+=last
if int(str_is) % 10 ==0:
    print('Yes')
else:
    print('No')

#Sol 2
N = int(input())
data = [int(x) for x in input().split()]

last=(data[N-1])%10
if last==0:
    print('Yes')
else:
    print('No')