list=list(map(int,input()))
c=0
for i in list:
    if i==6:
        continue
    else:
        c+=1
if list[-1]==6:
    c=-11
print(c)