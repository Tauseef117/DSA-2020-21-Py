#open read/write close operations
#r,w
# a append          #rb read binary
# r+ read + write
import os
u=open('one.txt','w')  #Creates file if not present
print(u)

# f =open('two.txt','x') #General method to create
# print(f)
# f.close()

f =open('two.txt','w')
f.write("data is data but i am ur beta  tht is what\n")
print(f)
f.write("what is up  tht is what\n")
print(f)
f.close()

f1 =open('two.txt','r')
print(f1.read())
f1.close()

f1 =open('two.txt','r')
print(f1.readline())
f1.close()

f1 =open('two.txt','r')
print(f1.readline(10))
f1.close()

f1 =open('two.txt','r')
print(f1.readable())
print(f1.writable())  #False as mode is r
f1.close()

f1 =open('two.txt','r+')
print(f1.readable())
print(f1.writable())
f1.close()



