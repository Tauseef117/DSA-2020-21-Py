lineslist=[]
emaildict={}
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
print("\nOUTPUT")

with open("mbox-short.txt") as f:
  for line in f:
    lineslist = line.split()
    if line.startswith('From '):
      email=lineslist[1]
      if email not in emaildict:
        emaildict[email] = 1
      else:
        emaildict[email] += 1
print (emaildict)

largest = None
for email in emaildict:
    count = emaildict[email]
    if largest is None or count > largest :
        largest = count
        largestemail = email
print('Largest:', largestemail, largest)