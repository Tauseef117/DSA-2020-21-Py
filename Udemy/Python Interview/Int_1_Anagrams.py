def anagrams(s1,s2):
    d={}
    s1=s1.replace(' ','')
    s2=s2.replace(' ','')
    if len(s1)!=len(s2):
        return False
    else:
        for letter in s1:
            if letter in d:
                d[letter]+=1
            else:
                d[letter]=1

        for letter in s2:
            if letter in d:
                d[letter]-=1
            else:
                d[letter]=1

        for key in d:
            if d[key]!=0:
                return False
        return True

s1=input()
s2=input()
print(anagrams(s1,s2))