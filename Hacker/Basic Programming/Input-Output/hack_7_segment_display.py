sticks = {"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
N = int(input())
for _ in range(N):
    num = list(input())
    total = 0
    for i in num:
        total += sticks[i]
    if total %2==0:
        print("1"*(total//2))
    else:
        print("7"+"1"*(total//2-1))

#My sol
for i in range(int(input())):
    str=input()
    sticks = 0
    for j in str:
        j=int(j)
        if j==0 or j==6 or j==9:
            sticks=sticks+6
            continue
        elif j==1:
            sticks=sticks+2
            continue
        elif j==2 or j ==3 or j==5:
            sticks=sticks+5
            continue
        elif j==4 :
            sticks=sticks+4
            continue
        elif j==7:
            sticks=sticks+3
            continue
        else:
            sticks=sticks+7
    if sticks % 2 == 1:
        a = ('7' * 1)
        sticks -= 3
        if (sticks % 2 == 0):
            num = sticks // 2
            b = '1' * num
            print(a + b)
    elif sticks%2==0:
        num=sticks//2
        print('1'*num)