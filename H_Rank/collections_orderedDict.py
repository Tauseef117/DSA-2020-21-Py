from collections import OrderedDict
arr = OrderedDict()
for _ in range(int(input())):
    line=list(input())
    a=' '.join(line[0:len(line)-1])
    b=int(line[-1])
    if a in arr.keys():
        arr[a]=arr[a]+b
    else:
        arr[a]=b
for i, j in arr.items():
    print(i,j)
for i,j in arr.items():
    s=''
    s+=str(i)+str(j)
    print(s[::2]+s[-1])