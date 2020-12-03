def back(s,er):
    b=0
    if er[-1]==s:
        b=b+len(er)-1
    elif er[0]==s:
        b=b+len(er)-1
    return b

def move(s,er):
    m=0
    if er[-1] != s:
        m = m + 1
    return m

sentence=list(input().split())
error=list(input())
p,b,m=0,0,0
for word in sentence:
    if list(word)==error :
        p+=1
    else:
        for i in range(len(word)):
            if i==len(word)-1:
                if word[i-1] in error:
                    b = b + back(word[i], error)
                    m = m + move(word[i], error)
                else:
                    p = p + 1
                    b = b + back(word[i], error)
                    m = m + move(word[i], error)
            elif word[i] in error:
                p=p+1
                b=b+back(word[i],error)
                m=m+move(word[i],error)
            else:
                continue
print(p+b+m)
