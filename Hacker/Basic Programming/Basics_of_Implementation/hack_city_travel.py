s,x,n=map(int,input().split())
day=0
first=[]
sec=[]
for i in range(1,n+1):
    a,b=map(int,input().split())
    first.append(a)
    sec.append(b)
for i in sec:
    s-=i
    day+=1
r=True
while(r==True):
    if s>0:
        s-=x
        day+=1
        r=True
    else:
        r=False
print(day)