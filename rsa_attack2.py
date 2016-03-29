# -*- coding: utf-8 -*-
import sys
p = sys.argv[1]
q = sys.argv[2]
e = sys.argv[3]
p = int(p)
q = int(q)
e = int(e)
n = p * q

#最大公約数を求める
def gcd(a,b):
	while b:
		a, b = b, a%b
	return a

#最小公倍数を求める
def lcm(a,b):
	return a * b / gcd(a,b)

l = lcm(p - 1, q - 1)

print gcd(e,l)

# 拡張ユークリッド互除法
def gcd2(a,b):
	if b == 0:
		u = 1
		v = 0
	else:
		q = a / b
		r = a % b
		(u0, v0) = gcd2(b, r)
		u = v0
		v = u0 - q * v0
	return (u, v)

d = gcd2(e, l)[0]
if d < 0:
	d += l

print d
