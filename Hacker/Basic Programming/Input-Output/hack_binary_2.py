test_cases =int(input())
for i in range(test_cases):
    x, y, a, b =input().split()
    if int(x) * int(y) == int(a) + int(b):
        print("Yes")
    else:
        print("No")
