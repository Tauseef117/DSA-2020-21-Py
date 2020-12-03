import string
alpha=dict(zip(string.ascii_lowercase, range(1,27)))
for _ in range(int(input())):
    arr = []
    nstr=input()
    for i in nstr:
        arr.append(alpha.get(i))
    narr = arr[::-1]
    final = []
    for i in range(len(arr)):
        final.append(arr[i] + narr[i])
    key_list = list(alpha.keys())
    val_list = list(alpha.values())
    val = ''
    for i in final:
        if i<=26:
            b = key_list[val_list.index(i)]
            val += str(b)
        else:
            i=i-26
            b = key_list[val_list.index(i)]
            val += str(b)
    print(val)
