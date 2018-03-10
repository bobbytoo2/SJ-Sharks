
# EvenOddCounter.py


'''This program will determine how many even
odd numbers will be randomly selected out of
the amount of integers determined by user.'''

import random

def main():

	r = int(input("Enter the number of random integers to generated: "))

	if r < 0:
		print("ERROR, cannot determine negative number!")
		r = int(input("Enter the number of random integers to generated: "))

	even = 0
	odd = 0

	for i in range(1, r+1):
		rNumbers = random.randint(1, 101)

		numbers = rNumbers % 2

		if (numbers == 0):
			even += 1
		else:
			odd += 1
	#Validation loop
	print("Out of %d random numbers, %d were odd, and %d \
were even." %(r, odd, even))

#Call main
main()