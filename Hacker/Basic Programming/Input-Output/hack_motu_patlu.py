nobricks = int(input())
bricks = nobricks
moto, patlu= 0, 0

for i in range(1, nobricks + 1):
    patlu = patlu + i;
    moto = moto + i * 2;
    bricks = bricks - i - i * 2;
    if (patlu + moto < nobricks and bricks < i):
        print("Patlu")
        exit()
print('Motu')




