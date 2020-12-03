for _ in range(int(input())):
    st=list(input())
    s=[]
    flag=True
    for i in range(len(st)):
        if len(s)==0:
            s.append(st[i])
        else:
            if st[i]=='{':
                s.append(st[i])
            elif st[i]=='[':
                s.append(st[i])
            elif st[i]=='(':
                s.append(st[i])
            elif st[i]==')':
                if len(s)>0 and s[-1]=='(':
                    s.pop()
                else:
                    flag=False
            elif st[i]==']':
                if len(s)>0 and s[-1]=='[':
                    s.pop()
                else:
                    flag=False
            elif st[i]=='}':
                if len(s)>0 and s[-1]=='{':
                    s.pop()
                else:
                    flag=False
    if flag==True and len(s)==0:
        print('YES')
    else:
        print('NO')

