lineslist=[]
domaindict={}
fname = input('Enter file name: ')
try:
    fhand = open(fname)
    print(fhand.read())
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
print("\nOUTPUT")

with open("mbox-short.txt") as f:
  for line in f:
    lineslist = line.split()
    if line.startswith('From '):
      email=lineslist[1]
      domain = email.split('@')[1]
      if domain not in domaindict:
        domaindict[domain] = 1
      else:
        domaindict[domain] += 1
print (domaindict)