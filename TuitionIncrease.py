# TuitionIncrease.py

''' 
This program calculates tuition (per semester) on a 
yearly basis with the percent increase and amount
of years.

'''

def main():

	# Enter tuition fee
	t = float(input("Enter the current tuition fee: "))

	while t < 0:
		print("ERROR: The tuition fee cannot be negative.")
		t = float(input("Enter the current tuition fee: "))

	
	# Enter tuition increase rate 
	x = int(input("Enter the percent increase: "))

	while x < 0:
		print("ERROR: The tuition increase rate cannot be negative.")
		x = int(input("Enter the percent increase: "))

	
	# Enter number of years
	y = int(input("Enter the number of years: "))
	
	while y < 0:
		print("ERROR: The amount of years cannot be negative.")
		y = int(input("Enter the number of years: "))


	# Print header
	print("%4s %16s" %("Year", "  Projected Tuition (per Semester)"))
	print("---------------------------------------")

	# Calculate interest amount
	for year in range(1, y+1):
		tuitionInterest = t * x/100

		# Update per semester tuition
		t += tuitionInterest

		print("%d %6s %7.2f" %(year, "$", t))

	print()

main()	