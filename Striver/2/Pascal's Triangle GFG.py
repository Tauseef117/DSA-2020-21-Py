def generate2(numRows):
    pascal2 = [[0]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(i+1):
            if j==0 or i==j:
                pascal2[i][j]=1
                print(pascal2[i][j],end=' ')
            else:
                pascal2[i][j]=pascal2[i-1][j-1] + pascal2[i-1][j]
                print(pascal2[i][j], end=' ')
        print(end='\n')

generate2(5)