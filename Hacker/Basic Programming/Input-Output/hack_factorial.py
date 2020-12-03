def fact(n):
    num = 1
    while (n > 1):
        num = n * num
        n = n - 1
    print(num)


n = int(input())
if n >= 1 and n <= 10:
    fact(n)

n = int(input())
p = 1
for i in range(1, n + 1):
    p = p * i
print(p)