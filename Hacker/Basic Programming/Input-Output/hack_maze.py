str=input().strip()
str.upper()
a,b=0,0
if len(str)<=200 and len(str)>=1:
    for i in str:
        if(i=='R'):
            a=a+1
        elif(i=='L'):
            a=a-1
        elif (i == 'U'):
            b = b + 1
        elif (i == 'D'):
            b = b - 1
print(a,b)