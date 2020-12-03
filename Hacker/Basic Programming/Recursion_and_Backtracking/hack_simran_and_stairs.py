n=int(input())
if n<3:
    print(n)
else:
    a,b,c=1,1,2
    for i in range(n-2):
        res=a+b+c
        a,b,c=b,c,res
    print(res)

def tcount(n):
    if (n == 0):
        return 1
    elif (n < 0):
        return 0
    return tcount(n - 1) + tcount(n - 2) + tcount(n - 3)


n = int(input())
steps = [0] * 31
steps[1] = 1
steps[2] = 2
steps[3] = 4
for i in range(4, n + 1):
    steps[i] = steps[i - 1] + steps[i - 2] + steps[i - 3]
print(steps[n])