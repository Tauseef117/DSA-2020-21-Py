from collections import Counter
for _ in range(int(input())):
    flag=0
    n,k=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(len(input()))
    l=Counter(l).values()
    for i in l:
        if i%k==0:
            flag=1
        else:
            flag=0
    print('Possible' if flag == 1 else 'Not possible')
