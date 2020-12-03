for _ in range(int(input())):
    a=input()
    b=input()
    flag=0
    for i in range(len(b)-1):
        if b[i] in a:
            print('YES')
            flag=1
            break
    if flag==0:
        print('NO')