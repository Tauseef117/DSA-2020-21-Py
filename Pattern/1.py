n=int(input())
for i in range(1,n+1):
    print('* '*i)
print('\n')

for i in range(1,n+1):
    for j in range(i):
        print('* ',end='')
        print('t ',end='')
    print('\r')
print('\n')

num=1
for i in range(n):
    for j in range(i+1):
        print(num,end=' ')
        num=num+1
    print('\t')
print('\n')

num=1
for i in range(n):
    num=1
    for j in range(i+1):
        print(num,end=' ')
        num=num+1
    print('\t')
print('\n')

num=1
for i in range(n):
    for j in range(i+1):
        print(num,end=' ')
    print('\t')
    num=num+1
print('\n')

char=65
for i in range(n):
    for j in range(i+1):
        print(chr(char),end=" ")
    char=char+1
    print('\t')
print('\n')

char=65
for i in range(n):
    for j in range(i+1):
        print(chr(char),end=" ")
        char=char+1
    print('\t')


