n=input()
val = 1
sum = 0
if len(n) == 10:
    for i in n:
        i = int(i)
        sum = sum + val * i
        val = val + 1
    if sum % 11 == 0:
        print('Legal ISBN')
    else:
        print('Illegal ISBN')
else:
        print('Illegal ISBN')