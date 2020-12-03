for _ in range(int(input())):
    n=input()
    if n==n[::-1]:
        print('-1')
    else:
        print(*(sorted(n)),sep='')