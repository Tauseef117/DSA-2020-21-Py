t=int(input())
for i in range(t):
    n=int(input())
    if n%12==1:
        seat=n+11
        type='WS'
    if n%12==2:
        seat=n+9
        type = 'MS'
    if n%12==3:
        seat=n+7
        type = 'AS'
    if n%12==4:
        seat=n+5
        type = 'AS'
    if n%12==5:
        seat=n+3
        type = 'MS'
    if n%12==6:
        seat=n+1
        type = 'WS'
    if n%12==7:
        seat=n-1
        type = 'WS'
    if n%12==8:
        seat=n-3
        type = 'MS'
    if n%12==9:
        seat=n-5
        type = 'AS'
    if n%12==10:
        seat=n-7
        type = 'AS'
    if n%12==11:
        seat=n-9
        type = 'MS'
    if n%12==0:
        seat=n-11
        type = 'WS'
    print(seat,type)







