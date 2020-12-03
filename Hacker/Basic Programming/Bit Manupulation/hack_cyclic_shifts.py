for _ in range(int(input())):
    n,m,c=map(str,input().split())
    m=int(m)
    n=bin(int(n))[2:]
    l=len(n)
    if l<16:
        n= '0' * (16 - l) + n
    if c == 'L':
        for i in range(m):
            n= n[1:] + n[0]
        print(int(n, 2))
    else:
        for i in range(m):
            n = n[-1] + n[:-1]
        print(int(n, 2))