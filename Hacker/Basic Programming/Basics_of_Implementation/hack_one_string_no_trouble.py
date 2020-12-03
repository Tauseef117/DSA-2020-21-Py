string=input()
big=0
c=0
for i in range(len(string)-1):
    if string[i]!=string[i+1]:
        c+=1
        if c > big:
            big=c
    else:
        c=0
print(big + 1)