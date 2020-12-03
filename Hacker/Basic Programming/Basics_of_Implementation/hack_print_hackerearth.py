step=0
n=int(input())
string=input().lower()
if len(string) == n:
    h = string.count('h')
    a = string.count('a')
    c = string.count('c')
    k = string.count('k')
    e = string.count('e')
    r = string.count('r')
    t = string.count('t')
    while(True):
        if h>=2 and a>=2 and e>=2 and r>=2 and c>=1 and k>=1 and t>=1:
            step+=1
            h -= 2
            a -= 2
            e -= 2
            r -= 2
            c -= 1
            k -= 1
            t -= 1
        else:
            break
print(step)

