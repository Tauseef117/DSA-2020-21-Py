for _ in range(int(input())):
    sum=''
    a,b=map(str,input().split())
    sum=str(int(a[::-1])+int(b[::-1]))
    print(int(sum[::-1]))
