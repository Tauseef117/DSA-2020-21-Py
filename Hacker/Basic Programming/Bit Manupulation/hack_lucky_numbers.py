for _ in range(int(input())):
    n=int(input())
    sum=0
    for i in range(1,n+1):
        a=bin(i)
        if a.count('1')==2:
            sum=sum+i
    print(sum%1000000007)