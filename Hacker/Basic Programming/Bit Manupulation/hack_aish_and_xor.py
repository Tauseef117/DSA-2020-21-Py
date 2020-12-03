n=int(input())
arr=list(map(int,input().split()))
q=int(input())
li=list()
zero=list()
cnt=0
a=0
b=0
for i in arr:
    a= a ^ i
    li.append(a)
    b=bin(i)[2:]
    cnt= cnt + b.count('0')
    zero.append(cnt)
for _ in range(q):
    l, r = map(int, input().split())
    l=l-1
    r=r-1
    if l==0:
        unset=zero[r]
        xor=li[r]
    else:
        unset= zero[r] - zero[l - 1]
        xor= li[r] ^ li[l - 1]
    print(xor,unset)

#My solution

n=int(input())
arr=list(map(int,input().split()))
q=int(input())
for _ in range(q):
    a=None
    l,r=map(int,input().split())
    c=0
    for i in range(l-1,r):
        if i==l-1:
            a=arr[i]
            c=bin(arr[i])[2:].count('0')
        else:
            a=a^arr[i]
            c=c+bin(arr[i])[2:].count('0')
    print(a,c)

