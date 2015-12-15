import urllib2, urllib
params = {'alpha': 'abc', 'space':  ' ', 'slash': '/'}
query_string = urllib.urlencode(params)
print(query_string)
url = 'http://yourdomain.com/?' + query_string
