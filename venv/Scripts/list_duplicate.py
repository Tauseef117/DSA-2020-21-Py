list= [3,4,5,6,7,3]
unique=[]
for number in list:
    if number not in unique:
        unique.append(number)
print(unique)


print(set(list))


for i in list:
    index= list.index(i)
    num = list[index]
    for j in list:
        if j==num:
            print(j)
    #        list.remove(j)
# print(list)