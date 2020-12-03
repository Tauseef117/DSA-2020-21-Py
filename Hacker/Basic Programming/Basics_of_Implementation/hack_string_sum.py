import string
alpha=dict(zip(string.ascii_lowercase, range(1,27)))
n=input()
sum=0
for i in n:
    sum+=alpha.get(i,None)
print(sum)