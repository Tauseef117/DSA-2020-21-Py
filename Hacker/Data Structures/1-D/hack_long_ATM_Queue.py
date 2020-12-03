n=int(input())
c=list(map(int,input().split()))
co=1
for i in range(len(c)-1):
    if c[i] >c[i+1]:
        co+=1
print(co)