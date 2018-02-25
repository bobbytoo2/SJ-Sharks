'''Create a program that calculates your amount of change to be given.

At the market, you are purchasing 3 items: apple, banana, and orange.
You have a $20.00 bill in your pocket.

Each apple costs $0.75
Each banana costs $0.80
Each orange costs $0.99

Calculate the change after calculating sub-total.

'''
Cash = float(20.00)

Apple = float(0.75)
Banana = float(0.80)
Orange = float(0.99)

ApBaOr = Apple + Banana + Orange # Price of the three items together.

MaxApples = Cash/Apple # Max amount of apples is 26
MaxBananas = Cash/Banana # Max amount of bananas is 25
MaxOranges = Cash/Orange # Max amount of oranges is 20

MaxTotal = Cash/ApBaOr

Err = "Error! Not enough money for the selected quantity!"

def main():
	
	# User inputs quantity of apples bananas and oranges.

	QuantApples = int(input("Enter amount of apples to purchase: "))
	QuantBananas = int(input("Enter amount of bananas to purchase: "))
	QuantOranges = int(input("Enter amount of oranges to purchase: "))

	# Computes total price of quantities selected.

	AppleTotal = float(QuantApples * Apple)
	BananaTotal = float(QuantBananas * Banana)
	OrangeTotal = float(QuantOranges * Orange)

	# Calculates Sub-total cost

	SubTotal = AppleTotal + BananaTotal + OrangeTotal
	print("Your sub-total is: $%.2f" %SubTotal)

	if SubTotal > Cash:
		print(Err)
	else:
		AmtChange = Cash - SubTotal # Calculates amount of change due.
		print("Your amount of change is: $%.2f" %AmtChange)

#Call main
main()











