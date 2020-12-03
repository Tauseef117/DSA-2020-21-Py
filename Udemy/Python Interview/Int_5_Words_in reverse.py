def rev(s):
    return ' '.join(s.split()[::-1])

def rev2(s):
    return ' '.join(reversed(s.split()))

def rev3(s):
    words=[]
    space=[' ']
    length=len(s)
    i=0
    while(i<length):
        if s[i] not in space:
            word_start=i
            while i<length and s[i] not in space:
                i+=1
            words.append(s[word_start:i])
    return ' '.join(reversed(words))

print(rev3(' ant is back'))