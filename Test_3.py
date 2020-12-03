def getSum(n):
    sum = 0
    while (n > 0):
        sum += int(n % 10)
        n = int(n / 10)
    return sum

for _ in range(int(input())):
    n,s=map(int,input().split())
    su=getSum(n)
    t=n
    while(1):
        if su<=s:
            break
        n+=1
        su = getSum(n)
    print(n-t)
