str=input()
n=len(str)
if n >=1 and n <=100:
    ele=''
    for i in str:
        if i.isupper() == True:
            a=i.lower()
            ele+=a
        else:
             b=i.upper()
             ele+=b
print(ele)