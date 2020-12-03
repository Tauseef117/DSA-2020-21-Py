for _ in range(int(input())):
    n=int(input())
    c=input()
    count=0
    for i in range(1,n+1):
        c=c[1:]+c[0]
        b=int(c)
        if b%2==0:
            count+=1
    print(count)


#Solution as even binary number will have 0 in last place
for _ in range(int(input())):
    n=int(input())
    c=input()
    print(c.count('0'))