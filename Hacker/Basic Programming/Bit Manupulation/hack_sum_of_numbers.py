from itertools import combinations

def is_possible_sum(numbers, n):
    for r in range(len(numbers)):
        for combo in combinations(numbers, r + 1):
        #2nd parameter is step initial 1(r+1,0+1)
            if sum(combo) == n:
                return True
    return False
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    s=int(input())
    a=is_possible_sum(arr,s)
    if a==True:
        print('YES')
    else:
        print('NO')