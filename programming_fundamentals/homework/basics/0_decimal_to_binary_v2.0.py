__author__ = "Pavlo Zablotskyy"
__maintainer__ = "Pavlo Zablotskyy"
__email__ = "pavlo.zablotskyy@gmail.com"

# enter decimal birthday representation
int_birthdate = int(input("Please enter a decimal year of your birth: "))
# init empty string
bin_birthdate = ''

while (int_birthdate > 0):
	# save reminder
	bin_birthdate = bin_birthdate + str(int_birthdate % 2)	
	int_birthdate = int(int_birthdate / 2)

# print reminders in reverse (correct) order
print (bin_birthdate[::-1])
