a,b=map(int,input().split())
x=min(a,b)
#HCF
for i in range(x,0,-1):
    if a%i==0 and b%i==0:
        print('HCF is',i)
        break
#LCM
for i in range(x,a*b):
    if i%a==0 and i%b==0:
        print('LCM is',i)
        break