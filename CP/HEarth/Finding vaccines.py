v=int(input())
n=int(input())
vir=input()
mx=0
for i in range(v):
    m=int(input())
    vac=input()
    cur=0
    if 'G' in vac:
        cur+=vir.count('C')*vac.count('G')
    if 'C' in vac:
        cur+=vir.count('G')*vac.count('C')
    if cur>mx:
        mx=cur
        c=i+1
print(c)