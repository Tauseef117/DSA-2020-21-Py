n=int(input())
str=input().strip() #removes spaces before &  leading
length=len(str)
if length==n:
    str=str.replace('.','B')
    if 'HH' in str:
        print('NO')
        exit()
    else:
        print('YES')
print(str)