n = int(input())
bride = list(input())
groom = list(input())
for i in bride:
    if i in groom:
        groom.remove(i)
    else:
        print(len(groom))
        exit()
print(0,end=' ')