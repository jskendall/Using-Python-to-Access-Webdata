import urllib
import xml.etree.ElementTree as ET
# Modules to read from a file and parse XML
total = 0




url = raw_input('Enter URL: ')

print 'Retrieving', url
# Open the given file
uh = urllib.urlopen(url)
# Read entire contents of file into a string
data = uh.read()
print 'Retrieved',len(data),'characters'
# Use ElementTree to parse the XML data
tree = ET.fromstring(data)
# Find all the children of comments/comment
lst = tree.findall('comments/comment')
print 'Character count: ', len(lst)

# Go through the children of comments/comment and add up the value of the count nodes
for item in lst:
	rel = item.find('count').text
	total = total + int(rel)
# Print the total from all the count nodes
print 'Total: ', total
