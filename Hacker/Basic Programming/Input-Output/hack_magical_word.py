for i in range(int(input())):
    nstr=''
    n=int(input())
    s=input()
    if len(s)==n:
        for k in s:
            asci=ord(k)
            if asci in range(0,70):
                nstr+='C'
                continue
            elif asci in range(70,73):
                nstr += 'G'
                continue
            elif asci in range(73,77):
                nstr += 'I'
                continue
            elif asci in range(77,82):
                nstr += 'O'
                continue
            elif asci in range(82,87):
                nstr += 'S'
                continue
            elif asci in range(87,94):
                nstr+='Y'
                continue
            elif asci in range(94,100):
                nstr+='a'
                continue
            elif asci in range(100,103):
                nstr+='e'
                continue
            elif asci in range(103,106):
                nstr+='g'
                continue
            elif asci in range(106,109):
                nstr+='k'
                continue
            elif asci in range(109,112):
                nstr+='m'
                continue
            else:
                nstr+='q'
    print(nstr)