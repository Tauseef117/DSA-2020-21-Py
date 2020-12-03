for k in range(int(input())):
    length = int(input())
    string = input().lower()
    count=0
    for i in range(1,length):
        if string[i] in 'aeiou':
            if string[i-1] not in 'aeiou':
                count+=1
    print(count)