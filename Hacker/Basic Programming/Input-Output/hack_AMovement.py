n=int(input())
step=0
if n>5:
    step=n//5
    n=n-step*5
if n%5!=0:
    step+=1
print(step)

#Sol2
n=int(input())
if(n%5==0):
    print(n//5)
else:
    print(n//5+1)