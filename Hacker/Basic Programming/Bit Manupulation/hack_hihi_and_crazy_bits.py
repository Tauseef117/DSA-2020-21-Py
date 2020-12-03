for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        print(n+1)
    else:
        for i in range(1,10**9):
            a=n^(n+i)
            if bin(a).count('1')==1:
                print(n+i)
                break
            else:
                continue