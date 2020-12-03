for _ in range(int(input())):
    n=int(input())
    ar = list(map(int, input().split()))
    if len(ar)==1:
        print('1')
        continue
    else:
        ele=ar[0]
        c=1
        for i in range(1,len(ar)):
            if i==1:
                if ar[i]>ele:
                    continue
                else:
                    c+=1
                    ele=ar[i]
            else:
                if ar[i]<ele:
                    c+=1
                    ele=ar[i]
                else:
                    continue
        print(c)
