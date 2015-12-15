import urllib2
response = urllib2.urlopen('http://yahoo.co.jp/')
content = response.read()
print(content)
headers = response.info()
#print(headers['content-type'])
#print(headers['date'])
