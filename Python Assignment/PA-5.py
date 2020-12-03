# Tauseef Ahmed-4SF17CS173


list1 =[[1,5,6],[6,6,7],[4,2,3]]
larg=0
for i in list1:
    temp=sum(i)
    if temp>larg:
        larg=temp
        larg_valuelist=i
print(larg_valuelist)
