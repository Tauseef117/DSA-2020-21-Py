# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

tag_list=[]

url = input('Enter URL: ')
count=int(input('Enter Count: '))
position=int(input('Enter Position: '))

for _ in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        tag_list.append(tag)
    url=tag_list[position - 1].get('href', None)
    tag_list=[]
print ('Retrieving:',url)
#http://py4e-data.dr-chuck.net/known_by_Cedar.html