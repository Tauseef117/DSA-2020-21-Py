p,s,t,h,x=map(int,input().split())
cost=0
for i in range(x):
    if s<=t:
        cost+=h
        s-=1
    else:
        cost+=p
        s-=1
print(cost)