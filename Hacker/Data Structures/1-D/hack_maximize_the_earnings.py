for _ in range(int(input())):
    n,r=map(int,input().split())
    ar=list(map(int,input().split()))
    c=1
    ele=ar[0]
    for i in range(1,len(ar)):
        if ar[i]>ele:
            c+=1
            ele=ar[i]
    print(c*r)