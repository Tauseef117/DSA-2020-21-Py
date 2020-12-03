fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
fname2 = input('Enter file name: ')
try:
    fhand2 = open(fname2)
except FileNotFoundError:
    print('File cannot be opened:', fname2)
print("OUTPUT 1 :- Common names")
common=set(fhand).intersection(fhand2)
c=0
for i in common:
    print(i.strip())
    c+=1
print("OUTPUT 2\nThe count of common names in both files are",c-1)
print("\nOUTPUT 3 :- Names only in File 1")
fhand = open(fname,'r')
diff=set(fhand).difference(common)
for i in diff:
    print(i.strip())
