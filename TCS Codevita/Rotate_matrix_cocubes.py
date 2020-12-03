arr=[[1,2,3,4,11,13],[5,6,7,8,32,33],[15,16,17,18,72,93]]
n=len(arr)
m=len(arr[0])
ip=int(input())
if ip==1:
    l=[]
    for i in arr[1]:
        l.append(i)
    a=l[:2]
    l=l[2:]
    for i in a:
        l.append(i)
    for i in range(len(arr[0])):
        arr[1][i]=l[i]
    print(arr)
else:
    l = []
    for i in range(n):
        l.append(arr[i][1])
    a=l[:1]
    l=l[1:]
    for i in a:
        l.append(i)
    for i in range(n):
        arr[i][1]=l[i]
    print(arr)