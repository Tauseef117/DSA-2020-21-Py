s=list(input())
ar=[]
for i in range(len(s)):
    if(len(ar)==0):
        ar.append(s[i])
    elif ar[-1]==s[i]:
        ar.pop()
    else:
        ar.append(s[i])
if len(ar)==0:
    print('Empty String')
else:
    print(''.join(ar))

# explain why index out of range

s=list(input())
ar=[s[0]]
for i in range(1,len(s)):
    if ar[-1]==s[i]:
        ar.pop()
    else:
        ar.append(s[i])
if len(ar)==0:
    print('Empty String')
else:
    print(''.join(ar))