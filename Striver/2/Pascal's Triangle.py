def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    #for i in range(2,numRows):
    for i in range(numRows):
       # print(i)
        for j in range(1,i):
         #   print(i,j)
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal

a=generate(5)
for i in a:
    print(*i)


