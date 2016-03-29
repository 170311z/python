import math
import collections
import sys

param = sys.argv[1]
param = int(param)

def trial_division_sqrt(n):
	prime_count = collections.Counter()

	for i in xrange(2, int(math.sqrt(n)) + 2):
		while n % i == 0:
			n /= i
			prime_count[i] += 1
	if n > 1:
		prime_count[n] += 1

	print prime_count

trial_division_sqrt(param)
