for i in range(int(input())):
    h1,m1,h2,m2=map(int,input().split())
    m1=m1+h1*60
    m2=m2+h2*60
    tmin=m2-m1
    hour=0
    if tmin>=60:
        hour=tmin%60
        minu=tmin-hour*60  #minu=tmin%60
        print(hour,minu)
    else:
        print(hour,tmin)

