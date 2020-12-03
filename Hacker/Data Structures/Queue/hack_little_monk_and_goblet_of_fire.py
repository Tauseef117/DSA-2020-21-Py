l=[]
q=[[],[],[],[]]
for _ in range(int(input())):
    line=input().split()
    line=list(line)
    if len(line)>1:
        a=int(line[1])
        b=int(line[2])
        if a not in l:
            l.append(a)
        q[a-1].append(b)
      #  print(q)
    else:
        b1=q[l[0]-1].pop(0)
        print(l[0],b1)
        if len(q[l[0]-1])==0:
            l.pop(0)

#5
#E 1 1
#[[1], [], [], []]
#E 2 1
#[[1], [1], [], []]
#E 1 2
#[[1, 2], [1], [], []]
#D
#1 1
#D
#1 2