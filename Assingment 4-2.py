repeat = 0

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
pos = raw_input('Enter Position -')
rep = raw_input('Enter Repeat -')

while repeat <= int(rep):
	position = 0
	print 'Retreiving: ', url

	html = urllib.urlopen(url).read()

	soup = BeautifulSoup(html)

	tags = soup('a')
	
	for tag in tags:
		position = position + 1
		if position > (int(pos)): break
		url = tag.get('href', None)
		
	repeat = repeat + 1


