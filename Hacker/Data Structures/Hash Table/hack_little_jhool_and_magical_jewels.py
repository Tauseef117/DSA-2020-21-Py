for _ in range(int(input())):
    a=input()
    r,u,b,y=0,0,0,0
    r=a.count('r')
    u = a.count('u')
    b = a.count('b')
    y = a.count('y')
    print(min(r,u,b,y))