r=int(input())
c=int(input())
for row in range(r):
    for col in range(c):
        if col==0 or col==5:
            print('*',end='')
        elif row==col:
            print('*', end='')
        else:
            print(end=' ')
    print('\r')
print('\t')

for row in range(r):
    for col in range(c):
        if col==0 or col==5 or row ==0 or row ==5:
            print('*',end='')
        else:
            print(end=' ')
    print('\r')
print('\t')

for row in range(r):
    for col in range(c):
        if col==0 or col==5 or row ==0 or row ==5:
            print('*',end='')
        else:
            print(end=' ')
    print('\r')
print('\t')

for row in range(r):
    for col in range(c):
        if col==0 or col==5 or row ==0 or row ==5 or row==3:
            print('*',end='')
        else:
            print(end=' ')
    print('\r')
print('\t')