n=int(input())
s=input()
st=[]
for i in range(len(s)):
    if len(st)==0 or s[i]!=st[-1]:
        st.append(s[i])
     #   print(st)
    else:
        st.pop(-1) #st.pop(0)
     #   print(st)
print(len(st))
print(''.join(st))