import urllib.request, urllib.error
import json
url = input('Enter URL- ')
output = urllib.request.urlopen(url).read()
data=output.decode()
try:
    js=json.loads(data)
except:
    js=None
sum=0
for i in range(len(js['comments'])):
    sum+=int(js['comments'][i]['count'])
print('Sum is',sum)

#solution 2
import urllib.request, urllib.error
import json
url = input('Enter URL- ')
output = urllib.request.urlopen(url).read()
data=output.decode()
try:
    js=json.loads(data)
except:
    js=None
count_val=[i['count'] for i in js['comments']]
print(sum(count_val))