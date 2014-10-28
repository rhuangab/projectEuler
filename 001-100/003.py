#Largest prime factor
#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#
#Thought:
#Use Fermat's algorithm find a^2 - b^2 = N, so (a+b)(a-b)= N. a+b and a-b are factors of N.
#Begin from 2, find the largest factor of n, said m, then find the largest factor of m.
#Keep on loop until m is a prime, output m.
#
import math
def largestPrimeFactor(n):
	i = 2
	curFactor = n
	while True:
		sqrtOfN = math.sqrt(curFactor)
		while curFactor % i != 0 and i <= sqrtOfN:
			i += 1
		if curFactor % i == 0:
			curFactor =  curFactor / i
			i = 2
		elif i > sqrtOfN:
			print curFactor
			break

largestPrimeFactor(600851475143)
		