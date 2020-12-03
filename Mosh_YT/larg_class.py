#from maxfile import max
from Mosh_YT import maxfile

maxfile.max
numbers=[]
n=int(input("Enter the count of numbers "))
for i in range(0,n):
    ele=int(input())
    numbers.append(ele)
print(numbers)
large=max(numbers)
print(large)

