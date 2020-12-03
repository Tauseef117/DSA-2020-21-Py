from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.bbc.com/sport/football/46897172"

try:
    page = urlopen(url)
except:
    print("Error opening the URL")

soup = BeautifulSoup(page, 'html.parser')


content = soup.find('div', {"class": "story-body sp-story-body gel-body-copy"})

article = ''
for i in content.findAll('p'):
    article = article + ' ' +  i.text
print(article)

with open('scraped_text.txt', 'w') as file:
    file.write(article)