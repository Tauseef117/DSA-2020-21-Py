from bisect import *
arr=[]
for k in range(1,1000000):
    ini =k
    a = str(bin(k))
    b=2 ** (len(a)-2)
    k = k*b
    arr.append(k)

for _ in range(int(input())):
    n=int(input())
    count=0
    count=bisect_right(arr,n)
    print(n-count)

#My solution
def one(x):
    c=0
    for i in x:
        if i=='1':
            c+=1
    return c
for _ in range(int(input())):
    n=int(input())
    count=0
    for i in range(1,n+1):
        a=n//i
        a=one(bin(a))
        b=one(bin(i))
        if a<=b:
            count+=1
        else:
            continue
    print(count)


