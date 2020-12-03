import collections
def find_mis(ar1,ar2):
    d=collections.defaultdict(int)
    for num in ar2:
        if num in d:
            d[num]+=1
        #else:          #works if comment removed also
            #d[num]=1   #not required as default dictionary works as it adds auto

    for num in ar1:
        if d[num]==0:
            return num
        else:
            d[num]-=1

print(find_mis([5,5,7,7],[5,7,7]))

#another solution will be summing up both arrays and subtracting but it will reach memory limit for big numbers

def find_mis2(ar1,ar2):
    result=0
    for num in ar1+ar2:
        result^=num
    return result

print(find_mis2([5,5,7,7],[5,7,7]))