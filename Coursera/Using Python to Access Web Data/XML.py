import urllib.request, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_522143.xml'
output = urllib.request.urlopen(url).read()
tree = ET.fromstring(output)

total = 0
for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        total += int(comment.find('count').text)

print(total)

#Solution 2


import urllib.request, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL- ')
output = urllib.request.urlopen(url).read()
tree = ET.fromstring(output)

lst = tree.findall('comments/comment')
print('Count: ', len(lst))
num = 0
for item in lst:
    x = item.find('count').text
    num = num + int(x)
print ('Sum: ', num)