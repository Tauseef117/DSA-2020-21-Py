def balanced_paran(str):
    depth=0
    for i in range(len(str)):
        char = str[i]
        if char=="(":
            depth+=1
        elif char==")":
            if depth>0:
                depth-=1
            else:
                return False
    return depth==0

print(balanced_paran("22)"))
print(balanced_paran("(a+b)(a-b)"))
print(balanced_paran("(a(b+c)-d)((e+f)"))
