import math
n=input()
c=0
for i in n:
    if i == '*':
        c += 1
if c==0:
    print(int(math.sqrt(int(n))))
    exit()
flag=0
val=0
for i in range(1,101):
    sq=str(i*i)
    if len(sq)==len(n):
        flag=1
        for j in range(len(n)):
            if n[j]!='*':
                if n[j]!=sq[j]:
                    flag=0
                    break
        if flag==1:
            val=1
            print(int(i))
            break
    else:
        continue
if val==0:
    print(0)





import math
list=[]
for i in range(1,101):
    list.append(str(i*i))
n=input()
if len(n)==5:
    print('100')
    exit()
arr=[]
c=0
r=0
for i in n:
    if i =='*':
        c+=1
if c==0:
    print(int(math.sqrt(int(n))))
    exit()
if n=='*':
    print('1')
    exit()
if len(n)==3:
    for i in list:
        if len(i)==3:
            if n[0]==i[0] and n[-1]==i[-1]:
                arr.append(int(i))
        else:
            continue
if len(n)==4:
    for i in list:
        if len(i)==4:
            if n[0]==i[0] and n[-1]==i[-1]:
                if c==2:
                    arr.append(int(i))
                elif c==1:
                    r=n.find('*')
                    if r==2:
                        if n[1]==i[1]:
                            arr.append(int(i))
                    elif r==1:
                        if n[2] == i[2]:
                            arr.append(int(i))
if len(arr)==0:
    print('0')
else:
    ele = min(arr)
    print(int(math.sqrt(ele)))
