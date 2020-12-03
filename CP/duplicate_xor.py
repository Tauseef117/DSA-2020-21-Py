l=[100,101,102,103,101]
a=[100,101,102,103]
x=l[0]
for i in range(1,len(l)):
    x=x^l[i]
for i in range(len(a)):
    x=x^a[i]
print(x)