vowel=['a','e','i','o','u','A','E','I','O','U']
for k in range(int(input())):
    string = input()
    count=0
    length = len(string)
    for i in range(length):
        for j in range(i, length):
            ele=(string[i:j + 1])
            for k in ele:
                for l in k:
                    if l in vowel:
                        count+=1
    print(count)

for k in range(int(input())):
    string = input().lower()
    count=0
    length = len(string)
    for i in range(length):
        if string[i] in 'aeiou':
            count = count +(i+1)*(length-i)
    print(count)



