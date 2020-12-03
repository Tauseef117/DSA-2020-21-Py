def one(n):
    count=0
    while(n):
        n=n & (n-1)
        count+=1
    return count

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ar=[]
    for i in range(n):
        ar.append([one(arr[i]),i,arr[i]])
    ar.sort()
    for i in range(n):
        ar[i]=ar[i][2]
    print(*ar)  #print list without bracket or comma


def one(n):
    count=0
    while(n):
        n=n & (n-1)
        count+=1
    return count

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ar=[]
    for i in arr:
        a=one(i)
        ar.append(a)
    dic=dict(zip(arr,ar))
    key_list = list(dic.keys())
    val_list = list(dic.values())
    al = sorted(dic.values())
    ar = []
    for i in al:
        ar.append(key_list[val_list.index(i)])
    print(ar)