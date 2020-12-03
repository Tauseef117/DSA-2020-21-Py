n=int(input())
c=list(map(int,input().split()))
id=list(map(int,input().split()))
if id==c:
    print(n)
    exit()
else:
    t=0
    while(len(c)>0):
        if c[0]==id[0]:
            c.pop(0)
            id.pop(0)
            t+=1
        else:
            c.append(c[0])
            c.pop(0)
            t+=1
    print(t)