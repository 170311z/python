# -*- coding: utf-8 -*-

import urllib2

f = urllib2.urlopen('http://qitta.com/advent-calendar/2014')
print f.code

headers = f.info()

print headers['content-type']

print f.read()