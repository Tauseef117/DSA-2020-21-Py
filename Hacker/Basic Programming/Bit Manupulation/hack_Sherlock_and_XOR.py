for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    c=0
    for i in arr:
        if i%2==0:
            c+=1
        else:
            continue
    print(c*(len(arr)-c))

def ans():
    for _ in range(int(input())):
        n = int(input())
        odd = 0
        for x in input().split():
            odd += x[-1] in "13579"
        yield (n - odd) * odd
print(*ans(), sep="\n")