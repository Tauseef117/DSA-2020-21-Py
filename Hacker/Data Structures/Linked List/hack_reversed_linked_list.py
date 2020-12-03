n=int(input())
ar=list(map(int,input().split()))
l=[]
ev=[]
for i in ar:
    if i%2!=0:
        if len(ev)>0:
            ev=ev[::-1]
            for j in ev:
                l.append(j)
            ev=[]
        l.append(i)
    else:
        ev.append(i)
if len(ev) > 0:
    ev = ev[::-1]
    for j in ev:
        l.append(j)
print(*l)
