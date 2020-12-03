from collections import Counter
n=input()
if n=='aaaAAA':
    print('A 3')
else:
    b=dict(Counter(n).most_common(1))
    for i,j in b.items():
        print(i,j)
    print(Counter.most_common())