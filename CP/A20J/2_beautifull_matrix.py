arr=list()
for i in range(5):
    ar = list(map(int, input().split()))
    arr.append(ar)
for i in range(5):
    for j in range(5):
        if arr[i][j]==1:
            #(3-r)+(3-c)
            print(abs(3-(i + 1)) + abs(3 - (j + 1)))
            exit()
        else:
            continue
