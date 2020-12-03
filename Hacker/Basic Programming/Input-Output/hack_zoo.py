str=input()
x,y=0,0
length=len(str)
if length<=20 :
    for i in str:
        if i in ('z','Z','O','o'):
           if i =='Z' or i =='z':
               x+=1
           if i =='O' or i =='o':
               y+=1
    if(2*x==y):
        print('Yes')
    else:
        print('No')

#2

zoo=input()
if 2*zoo.count('z')==zoo.count('o'):
	print('Yes')
else:
	print('No')