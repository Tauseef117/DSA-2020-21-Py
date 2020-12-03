from collections import Counter
for _ in range(int(input())):
    s=Counter(input()).values()
    flag=0
    for i in s:
        if i>=2:
            flag=1
    print('Yes' if flag == 1 else 'No')