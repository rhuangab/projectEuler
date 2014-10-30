'''
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of 
the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum.

Solution:
brute force
sumOfsq = (2n + 1)(n + 1)n/6
'''

def difference(n):
	sumOfSquare = (n + 1) * n / 2
	#sumOfSquare = (2*n+1)*(n+1)*n/6
	sumOfSquare = sumOfSquare ** 2
	squareOfSum = 0;
	for i in xrange(1, n+1, 1):
		squareOfSum += i ** 2
	return sumOfSquare - squareOfSum

print difference(100)