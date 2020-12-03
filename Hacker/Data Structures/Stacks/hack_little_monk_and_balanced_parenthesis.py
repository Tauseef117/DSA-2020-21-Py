n = map(int, input())
ar =list(map(int, input().split()))
maxlen = 0
currlen = 0
stack = []
l = []
for ele in ar:
    if ele > 0:
        stack.append(ele)
    else:
        if len(stack) > 0 and stack[-1] == -ele:
            currlen += 2
            stack.pop()
            if currlen >= maxlen:
                maxlen = currlen
            if len(stack) == 0:
                l.append(currlen)
                currlen = 0
        else:
            currlen = 0
            stack = []
            l.append(-1)
currlen = 0
for ele in l:
    if ele == -1:
        currlen = 0
    else:
        currlen += ele
        if currlen >= maxlen:
            maxlen = currlen
print(maxlen)


n=int(input())
ar=list(map(int,input().split()))
c=[0]
for i in range(len(ar)-1):
    for j in range(i+1,len(ar)+1):
        ele=ar[i:j]
        if len(ele)%2 == 0:
            a=len(ele)
            for k in range(a//2):
                b=-(ele[-1])
                if ele[0] == b:
                    ele=ele[1:-1]
                else:
                    break
        if len(ele)==0:
            c.append(a)
        else:
            continue
print(max(c))