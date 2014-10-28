'''
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

'''
Idea:
1. Create a palindrome number checker function.
2. Enumerate from the upper bound 999*999 to lower bound 100*100 of 
the product of two 3-digit number. If the number is a palindrome, check
whether it is a product of two 3-digit number.
'''

def checkPalindrom(n):
	length = 1
	target = n
	while target >= 10:
		length += 1
		target /= 10
	#check whether the Most significant digit(MSD) is equal to the LSD. 
	target = n
	leftBase = 10 ** (length - 1)
	i = 0
	while i < length/2:
		i += 1
		if target / leftBase != target % 10:
			return False
		#Remove MSD
		target = target % leftBase
		leftBase /= 100
		#Remove LSD
		target = target / 10
	return True

'''More efficient way to check palindrome.
Check the reverse of n is equal to n or not
'''
def checkPalindromPlus(n):
	origin = n
	reverse = 0
	while n > 0:
		reverse = 10 * reverse + n % 10
		n = n / 10
	return (reverse == origin)


def checkValidity(i):
	left = 999
	while left >= 100:
		if i % left == 0:
			quotient = i / left
			if quotient >= 100 and quotient <= 999:
				return True
		left -= 1
	return False


#Find largest palindrome which is a product of two 3-digit number
def Find():
	upper = 999 * 999
	lower = 100 * 100
	i = upper
	for i in xrange(upper, lower, -1):
		if checkPalindromPlus(i) and checkValidity(i):
			print i
			quit()
	print "No such number found"

Find()
#Result: 906609


