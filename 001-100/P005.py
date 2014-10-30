'''
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of 
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?

Solution:
1.
From 1 to n, get smallest multiple of 1 * 2 * 3 * ... * i, say sp(i),
sp(i + 1) = sp(i) * (i+1) / gcd(sp(i), i+1)

2. assume we have created a prime list. Then
lcm(20) = 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19
because 2^4 <= 20 < 2^5, 3^2 <= 20 < 3^3.
means 2^k <= 20 < 2^(k+1), find k for every prime which is smaller than 20.
let 2^k = 20 -> klog(2) = log(20), k = floor(log(20) / log(2))

'''
def gcd(a, b):
	if a < b:
		return gcd(b,a)
	temp = a % b
	while temp != 0:
		a = b
		b = temp
		temp = a % b
	return b

def minMultiple(n):
	multiple = 1
	for i in xrange(2, n, 1):
		multiple = multiple * i / gcd(multiple, i)
	return multiple

print minMultiple(20)
