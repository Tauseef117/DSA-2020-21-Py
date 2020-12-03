for _ in range(int(input())):
    zer=[0]*32
    for i in range(int(input())):
        n=int(input())
        for j in range(0,32):
            if n & (1<<j): #determines which all bits are set if 0 then not set are counted
                zer[j]+=1 #counting set bit position
    val=0
    for m in range(1,32):
        if zer[m]>zer[val]:
            val=m
    print(val)