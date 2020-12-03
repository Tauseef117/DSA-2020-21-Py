t=int(input())
if t<=100 and t>=1:
    for i in range(1,t+1):
        str, str1 = input().split()
        str = str.lower()
        str1 = str1.lower()
        str = str.strip()
        str1 = str1.strip()
        str = sorted(str)
        str1 = sorted(str1)
        if str == str1:
            print('YES')
        else:
            print('NO')
else:
    print('NO')

