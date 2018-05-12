power_button = True

power = input("Please turn on cofeemachine, write 'on': ")
if power != "on":
	print("Goodbay")
else:
	while power_button:
		woter = input("Please pour water into the coffee machine, write 'pour': ")
		if woter == "pour":
			coffee = input("Please put coffee in the coffee machine, write 'put': ")
			if coffee == "put":
				cup = input("Please put cup in the coffee machine, write 'put': ") 
				if cup == "put":
					start_button = input("Please press start button, write 'start': ")
					if start_button == "start":
						print("Your coffee is done")
						power_button = input("You can off coffee machine, write 'off': ")
						if power_button == "off":
							print("Goodbay")
							break



