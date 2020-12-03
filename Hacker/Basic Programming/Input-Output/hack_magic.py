n=int(input())
num=list(map(int,input().split()))
num.sort()
sum=sum(num)
list=[]
for i in num:
    if(sum - i) % 7 == 0:
        list.append(i)
if len(list)==0:
    print('-1')
else:
    print(num.index(min(list)))