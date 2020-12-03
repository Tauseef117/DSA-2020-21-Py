t=int(input())
for i in range(t):
    str1=list(input())
    str2=list(input())
    if len(str1)<=10000 and len(str2)<=10000:
        liston=[]
        for j in str1:
            if j in str2:
                liston.append(j)
                str2.remove(j)
        print(len(str1)+len(str2)-len(liston))