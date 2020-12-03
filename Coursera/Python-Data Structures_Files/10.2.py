#10.2 Write a program to read through the mbox.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.



name = input("Enter file:")
if len(name) < 1 : name = "mbox.txt"
handle = open(name)
dic=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From '):
        word=line.split()
        a=word[5]
        b=a[:2]
        if b in dic:
            dic[b]=dic[b]+1
        else:
            dic[b]=1
    else:
        continue
for i,j in sorted(dic.items()):
    print(i,j)