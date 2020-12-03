while(1):
    try:
        n=bin(int(input()))
        print(n.count('1'))
    except:
        break

for _ in range(int(input())):
    n=int(input())
    count=0
    while(n):
        n=n & (n-1)
        count+=1
    print(count)