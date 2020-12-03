n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    ele=a[i]+b[i]
    c.append(ele)
print(*c)

from sys import stdin
N = int(input())
A = list(map(int, stdin.readline().split(' ')))
B = list(map(int, stdin.readline().split(' ')))
print (' '.join(map(str, [A[i] + B[i]  for i in range(N)])))