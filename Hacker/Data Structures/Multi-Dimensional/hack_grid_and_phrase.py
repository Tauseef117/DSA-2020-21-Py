n, m = map(int, input().split())
st = list()
for _ in range(n):
    st.append(input())
count = 0
for i in range(n):
    for j in range(m):
        if st[i][j] == 's':
            if i <= n - 4 and j <= m - 4:
                if st[i + 1][j + 1] == 'a' and st[i + 2][j + 2] == 'b' and st[i + 3][j + 3] == 'a':
                    count += 1

            if j <= m - 4:
                if st[i][j + 1] == 'a' and st[i][j + 2] == 'b' and st[i][j + 3] == 'a':
                    count += 1

            if i <= n - 4:
                if st[i + 1][j] == 'a' and st[i + 2][j] == 'b' and st[i + 3][j] == 'a':
                    count += 1

            if i >= 3 and j <= m - 4:
                if st[i - 1][j + 1] == 'a' and st[i - 2][j + 2] == 'b' and st[i - 3][j + 3] == 'a':
                    count += 1
print(count)

n,m=map(int,input().split())
l=[]
for i in range(n):
    ele = list(input())
    l.append(ele)
a=''
b=''
count= ''
d=''
e=''
f=''
cn=0
for i in range(n):
    a+=l[i][0]
    b+=l[i][m-1]
for i in range(m):
    count+=l[0][i]
    d+=l[n-1][i]
if n==m:
    for i in range(n):
        for j in range(n):
            if i==j:
                e+=l[i][j]
            if i+j==n-1:
                f+=l[i][j]
if 'saba' in a:
    cn+=1
if 'saba' in b:
    cn+=1
if 'saba' in count:
    cn+=1
if 'saba' in d:
    cn+=1
if 'saba' in e:
    cn+=1
if 'saba' in f:
    cn+=1
if 'saba' in a[::-1]:
    cn+=1
if 'saba' in b[::-1]:
    cn+=1
if 'saba' in count[::-1]:
    cn+=1
if 'saba' in d[::-1]:
    cn+=1
if 'saba' in e[::-1]:
    cn+=1
if 'saba' in f[::-1]:
    cn+=1
print(count)