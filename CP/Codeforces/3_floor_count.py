for _ in range(int(input())):
    n ,x= map(int,input().split())
    if n<3:
        print('1')
        continue
    else:
        print(((n-3)//x)+2)