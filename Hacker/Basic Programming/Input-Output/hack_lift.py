def step(a,b):
    if(a>b):
        a,b=b,a
        d = range(a, b)
        d = len(d)
        return d
    else:
        d=range(a,b)
        d=len(d)
        return d


t=int(input())
A=0
B=7
for i in range(t):
    n=int(input())
    a=step(A,n)
    b=step(B,n)
    if a<b or a==b:
        print('A')
        A=n
    else:
        print('B')
        B=n

A=0
B=7
for i in range(int(input())):
    N = int(input())
    if ((N - A) <= (B - N)):
        print("A")
        A = N
    else:
        print('B')
        B = N