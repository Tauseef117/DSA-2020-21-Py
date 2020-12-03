n=int(input())
arr=list(map(int,input().split()))
a,b,c=0,0,0
if len(arr)==n:
    for i in range(n):
        if i<n:
            if i%3==1:
                b += arr[i]
            elif i%3==2:
                c += arr[i]
            else:
                a += arr[i]
    print(a,b,c)

n = int(input())
lst = list(map(int, input().split()))
sum1 = sum(lst[0::3])
sum2 = sum(lst[1::3])
sum3 = sum(lst[2::3])
print(str(sum1)+" "+str(sum2)+" "+str(sum3))