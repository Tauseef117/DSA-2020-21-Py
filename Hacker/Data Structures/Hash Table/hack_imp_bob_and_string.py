from collections import Counter
for _ in range(int(input())):
    a=Counter(input())
    b=Counter(input())
    c=a-b
    d=b-a
    sum=0
    for i in c.values():
        sum+=i
    for i in d.values():
        sum+=i
    print(sum)