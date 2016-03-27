# -*- coding: utf-8 -*-
# swywlm を復号
import sys
param = sys.argv
n = param[1]
n = int(n)
def caesar(n):
	a = int("s".encode('hex'), 16)
	b = int("w".encode('hex'), 16)
	c = int("y".encode('hex'), 16)
	d = int("w".encode('hex'), 16)
	e = int("l".encode('hex'), 16)
	f = int("m".encode('hex'), 16)

	a -= n
	b -= n
	c -= n
	d -= n
	e -= n
	f -= n

	a = format(a, 'x')
	b = format(b, 'x')
	c = format(c, 'x')
	d = format(d, 'x')
	e = format(e, 'x')
	f = format(f, 'x')


	print a.decode('hex') , b.decode('hex') , c.decode('hex') , d.decode('hex') , e.decode('hex') , f.decode('hex')

caesar(n)



