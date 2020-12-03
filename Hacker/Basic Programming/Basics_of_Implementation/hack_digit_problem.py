a, b = map(int, input().split())
a = str(a)
count = 0
for i in range(len(a)):
    if a[i] != '9' and count < b:
        a = a.replace(a[i], '9', 1)
        count += 1
print(a)

