import urllib2, urllib
#params = {'q': u'キーワード', 'page': 1}
#query_string = urllib.urlencode(params) ← マルチバイト文字が含まれるのでエラー
params = {'q': u'キーワード'.encode('utf8'), 'page': 1}
print(urllib.urlencode(params))
