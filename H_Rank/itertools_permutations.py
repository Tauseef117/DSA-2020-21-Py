from itertools import permutations
a,b=input().split()
a=sorted(a.upper())
b=int(b)
perms = [''.join(i) for i in permutations(a,b)]
for i in perms:
    print(i)

from itertools import permutations
a=[1,2,4,5]
print(*list(permutations(a,2)))