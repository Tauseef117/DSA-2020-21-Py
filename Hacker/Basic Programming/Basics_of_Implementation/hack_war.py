for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    bc=max(arr)
    ac=max(arr2)
    print(bc)
    if bc>ac:
        print('Bob')
    elif ac>bc:
        print('Alice')
    else:
        print('Tie')