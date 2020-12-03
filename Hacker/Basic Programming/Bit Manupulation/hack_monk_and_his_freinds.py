for _ in range(int(input())):
    a,b=map(int,input().split())
    c=bin(a^b)
    print(c.count('1'))