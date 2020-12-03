for i in range(int(input())):
    n=int(input())
    string=input()
    count=0
    if len(string)==n:
        for i in range(0,len(string)):
            if i<n-1:
                if string[i].isdigit():
                    if string[i + 1].isalpha():
                        count += 1
                    else:
                        continue
                else:
                    continue
            elif string[-1].isdigit():
                count+=1
    print(count)