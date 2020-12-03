t=int(input())
for k in range(t):
    length=list(map(int,input().split()))
    column_nam=list(map(str, input().split()))
    S=[]
    col='|'
    line_dashed = '+'
    val=[]
    for i in range(length[1]):
        S.append(list(map(str, input().split())))
    for i in range(length[0]):
        s=len(column_nam[i])
        for j in range(length[1]):
            if len(S[j][i])>s:
                s=len(S[j][i])
        line_dashed+= '-' * (s + 2) + '+'
        col+=' ' + column_nam[i] + ' ' * (s - len(column_nam[i])) + ' |'
        val.append(s)
    print(line_dashed)
    print(col)
    print(line_dashed)
    for i in range(length[1]):
        row= '|'
        for j in range(length[0]):
            if S[i][j].isdigit():
                row+= ' ' + ' ' * (val[j] - len(S[i][j])) + S[i][j] + ' |'
            else:
                row+= ' ' + S[i][j] + ' ' * (val[j] - len(S[i][j])) + ' |'
        print(row)
    print(line_dashed)