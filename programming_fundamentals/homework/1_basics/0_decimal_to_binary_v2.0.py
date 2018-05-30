__author__ = "Pavlo Zablotskyy"
__maintainer__ = "Pavlo Zablotskyy"
__email__ = "pavlo.zablotskyy@gmail.com"

# enter decimal birthday representation
int_birthdate = int(input("Please enter a decimal year of your birth: "))

def dec_to_bin(dec_year):
	bin_birthdate = ''
	while (dec_year > 0):
		# save reminder
		bin_birthdate = bin_birthdate + str(dec_year % 2)	
		dec_year = int(dec_year / 2)
		# return reminders in reverse (correct) order
	return bin_birthdate[::-1]

print (dec_to_bin(int_birthdate))
