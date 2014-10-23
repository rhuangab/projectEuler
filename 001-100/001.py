#001: Multiples of 3 and 5
import sys
def main(n):
	#sum of all multiples of 3 and 5
	sum = 0
	for i in range(int(n)):
		if i % 3 == 0 or i%5==0:
			sum += i
	print sum

n = raw_input("Enter the end num: ")
main(n)

