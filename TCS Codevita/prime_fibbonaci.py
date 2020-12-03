def primes_method4(n,m):
    ar=[]
    if n<=2:
        ar=[2]
    if n%2==0:
        n=n+1
    for num in range(n,m+1,2):
        if all(num%i!=0 for i in range(2, int(num**.5 ) + 1)):
            ar.append(num)
    return ar

a,b=map(int,input().split())
ar=primes_method4(a,b)
l=[]
for i in range(len(ar)):
    for j in range(0,len(ar)):
        if i==j:
            continue
        else:
            l.append(int(str(ar[i])+str(ar[j])))
l=set(l)
li=[]
for i in l:
    if i%2==0:
        continue
    else:
        if all(i % j != 0 for j in range(2, int(i ** .5) + 1)):
            li.append(i)
x=min(li)
y=max(li)
final=[x,y]
for i in range(len(li)-2):
    final.append(final[-1]+final[-2])
print(final[-1])
