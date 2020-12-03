t = int(input())
for i in range(t):
    ar1=[]
    ar2=[]
    g ,p = map(int,input().split())
    np = int(input())
    for j in range(np):
        p1,p2 =map(int,input().split())
        ar1.append(p1)
        ar2.append(p2)

    sum1=sum(ar1)
    val1 = sum1 * g

    sum2 = sum(ar2)
    val2 = sum2 * p
    total = val1 + val2

    sum3 = sum(ar1)
    val3 = sum3 * p

    sum4 = sum(ar2)
    val4 = sum4 * g
    total1 = val3 + val4

    print(min(total, total1))


// 2nd solution

t = int(input())
for i in range(t):
    ar1 = []
    ar2 = []
    g, p = map(int, input().split())
    np = int(input())
    for j in range(np):
        p1, p2 = map(int, input().split())
        ar1.append(p1)
        ar2.append(p2)

    count = 0
    for i in ar1:
        if i == 1:
            count = count + 1
    sum1 = count * g

    count2 = 0
    for i in ar2:
        if i == 1:
            count2 += 1
    sum2 = count2 * p
    total = sum1 + sum2

    count3 = 0
    for i in ar1:
        if i == 1:
            count3 += 1
    sum3 = count3 * p

    count4 = 0
    for i in ar2:
        if i == 1:
            count4 += 1
    sum4 = count4 * g
    total1 = sum3 + sum4
    print(min(total, total1))