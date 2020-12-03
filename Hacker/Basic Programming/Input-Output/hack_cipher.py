alpha =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower =[i.lower() for i in alpha]
num=['0','1','2','3','4','5','6','7','8','9']
string =input()
k=int(input())
strin=''
for i in string:
    if i in alpha:
        s=alpha[(alpha.index(i)+k)%26]
        strin+=s
    elif i in lower:
        s = lower[(lower.index(i) + k) % 26]
        strin += s
    elif i in num:
        s = num[(num.index(i) + k) % 10]
        strin += s
    else:
        strin +=i
print(strin)
