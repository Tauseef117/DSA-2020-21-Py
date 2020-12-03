st=list(input())
s=[]
for i in range(len(st)):
    if len(s)==0:
        s.append(st[i])
    else:
        if (st[i] == '(') and len(st)>0:
            s.append(st[i])
        elif st[i] == ')':
            if len(s) > 0 and s[-1] == '(':
                s.pop()
            else:
                s.append(st[i])
print(len(s))