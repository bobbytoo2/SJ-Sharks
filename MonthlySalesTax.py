
# MonthlySalesTax

''' 
This program will calculate your monthly sales with
state and federal sales tax.


State sales tax: 5%
Federal sales tax: 2.5%'''


stateSalesTax = 0.05
federalSalesTax = 0.025

def main():

	# Enter the month total sales
	monthSales = eval(input("Enter the total sales for the month: "))
	
	#Print validation loop
	while monthSales < 0:
		print("ERROR, cannot have negative monthly sales!")
		#Return to input
		monthSales = eval(input("Enter the total sales for the month: "))


	calcStateTax(monthSales)
	calcFedSalesTax(monthSales)
	calcTotalTax(monthSales)

def calcStateTax(monthSales):
	stateTax = float(monthSales * stateSalesTax)
	
	#Print State Tax
	print("State Tax: $%.2f" %(stateTax))

def calcFedSalesTax(monthSales):
	fedTax = float(monthSales * federalSalesTax)

	#Print Federal Tax
	print("Federal Tax: $%.2f" %(fedTax))

def calcTotalTax(monthSales):
	totalTax = (monthSales * stateSalesTax + monthSales * federalSalesTax)
	
	#Print Federal Tax
	print("Total Tax: $%.2f" %(totalTax))



#Call main
main()