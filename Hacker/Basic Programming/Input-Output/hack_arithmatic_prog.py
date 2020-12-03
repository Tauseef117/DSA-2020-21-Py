import math
t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    if b-a == c-b:
        print('0')
    else:
        ba = b-a
        cb = c-b
        diff = abs(ba - cb)   #abs prints only value not sign
        d = diff//2
        if diff % 2 == 0:
            print(d)
        else:
            print(d+1)


        ba = b - a
        cb = c - b
        diff = abs(ba - cb)
        print(math.ceil(diff / 2))