a=[4,5,7,8,9]
sum=0
for ind,val in enumerate(a):
    sum+=val * (ind+1) * (len(a)-ind)
print(sum)

a=[4,5,7,8,9]
sum=0
for i in range(len(a)):
    sum+=a[i]*(i+1)*(len(a)-i)
print(sum)

a=[1,2,3,4,5]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(a[i:j])

a=[1,2,3,4,5]
print(a[5:5])
print(a[1:4])
[]
[2, 3, 4]