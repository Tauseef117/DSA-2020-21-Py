from itertools import permutations
for _ in range(int(input())):
    a = set(tuple(input()))
    b=input()
    print(a)
    b=list(set(permutations(b)))
    print(b)
    if a in b :
        print('YES')
    else:
        print('NO')