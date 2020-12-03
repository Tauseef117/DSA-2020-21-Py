n=int(input())
num=list(map(int,input().split()))
length=len(num)
a=length//2
arr1=num[:a]
arr2=num[a:]
st=''
for i in arr1:
    i=str(i)
    st+=i[0]

# for i in range(len(arr1)):
#    j=str(arr1[i])
#    st+=j[0]


for i in arr2:
    i=str(i)
    st+=i[-1]
if int(st)%11==0:
    print('OUI')
else:
    print("NON")