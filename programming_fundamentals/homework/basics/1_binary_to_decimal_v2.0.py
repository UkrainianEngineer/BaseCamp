__author__ = "Pavlo Zablotskyy"
__maintainer__ = "Pavlo Zablotskyy"
__email__ = "pavlo.zablotskyy@gmail.com"

test_year = 11111000101
# reversing the number for easier multiplication
test_year_reverse = int(str(test_year)[::-1])
count = 0
dec_year = 0

for x in str(test_year_reverse):
	dec_year = dec_year + int(x)*(pow(2,count))
	count = count + 1

print (dec_year)
