#9.4 Write a program to read through the mbox.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. ' \
#'After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1: name = "mbox.txt"
handle = open(name)
count = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        word = line.split()
        a = word[1]
        if a in count:
            count[a] = count[a]+ 1
        else:
            count[a] = 1
    else:
        continue
bigcount=None
bigword=None
for i,j in count.items():
    if bigcount is None or j>bigcount:
        bigword = i
        bigcount=j

print(bigcount, bigword)