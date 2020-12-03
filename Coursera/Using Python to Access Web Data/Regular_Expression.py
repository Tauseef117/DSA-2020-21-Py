import re
fhand = open('f.txt')
a=re.findall('[0-9]+',fhand.read())
s=0
for i in a:
    i=int(i)
    s+=i
print(s)