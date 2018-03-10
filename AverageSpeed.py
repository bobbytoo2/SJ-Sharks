# AverageSpeed.py


'''This program collects the user input and calculates
the average speed of vehicles over a time period.'''

def main():

	#Get the number of vehicles participating.
	numberOfVehicles = int(input("Enter the number of\
 vehicles participating : "))

	
	#Print validation loop(s).
	while numberOfVehicles < 0:
		print("ERROR, cannot have a negative amount of vehicles!")
		numberOfVehicles = int(input("Enter the number of\
 vehicles participating : "))
	
	while numberOfVehicles == 0:
		print("ERROR, cannot have an average speed assessment\
 without having vehicles!")
		numberOfVehicles = int(input("Enter the number of\
 vehicles participating : "))


	#Get the number of hours traveled.
	numberOfHours = int(input("Enter the number of\
 hours travelled : "))

	
	#Print validation loop(s).
	while numberOfHours < 0:
		print("ERROR, cannot have nagative hours of driving!")
		#Return to input.
		numberOfHours = int(input("Enter the number of\
 hours travelled : "))

	while numberOfHours == 0:
		print("ERROR, you must have at least one hour to\
 assess an average speed!")
		#Return to input.
		numberOfHours = int(input("Enter the number of\
 hours travelled : "))


	message = ""

	#Determine each vehicle's average speed.
	for vehicle in range(1, numberOfVehicles+1):
		#Initialize an accumulator for speed.
		total = 0.00
		print()
		for hour in range(1, numberOfHours+1):

			#Get a vehicle's speeds.
			print("Enter the avg. speed of vehicle"\
			, vehicle, "during hour", hour, end=" ")
			speed = float(input(": "))

			#Print validation loop(s).
			while speed < 0:
				print("ERROR, cannot have a negative speed!")
				#Return to input.
				print("Enter the avg. speed of vehicle"\
				, vehicle, "during hour", hour, end=" ")
				speed = float(input(": "))

			#Add the speed to the accumulator.
			total += speed

		#Calculate the average speed of the vehicle.
		average = total / numberOfHours

		message += "%4d %12.2f %11.2f\n" %(vehicle, total, average)

	# Display the header.
	print("Vehicle", "Total Speed", "Avg. Speed")
	print("=======", "===========", "==========")
	print(message)

    
#Call main
main()
