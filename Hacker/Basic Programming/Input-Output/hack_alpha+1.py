alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def LetterChanges(s):
    new = []
    for i in s:
        if i in alpha:
            if alpha[alpha.index(i) + 1] in 'aeiou':
                new.append(alpha[alpha.index(i) + 1].upper())
            else:
                new.append(alpha[alpha.index(i) + 1])
        else:
            new.append(i)
    return ''.join(new)
str=input()
print(LetterChanges(str))