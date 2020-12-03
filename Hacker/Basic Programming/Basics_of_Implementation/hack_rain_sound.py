# Write your code here
import math
for i in range(int(input())):
    l,r,s=map(int,input().split())
    if l>r or s>r or math.ceil(l/s)>math.floor(r/s):
        print('-1 -1')

    else:
        print(math.ceil(l/s),math.floor(r/s))