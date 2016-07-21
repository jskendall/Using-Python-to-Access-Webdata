import urllib
import json

comm = 0
cnt = 0

url = raw_input('Enter URL: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()


info = json.loads(str(data))

for item in info['comments']:
    print 'Item ', item
    cnt += 1
    comm += int(item['count'])
print 'Total', comm
print 'Count', cnt
