#Tauseef Ahmed-4SF17CS173


a=[]
n= int(input("Enter the number of elements in list:"))
for i in range(0,n):
    ele=int(input("Enter element"))
    a.append(ele)
unique = []


for i in a:
    if i not in unique:
        unique.append(i)
print("Non duplicate list:")
print(unique)