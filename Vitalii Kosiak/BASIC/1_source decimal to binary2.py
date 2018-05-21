print("Decimal to binary")
try:
    birth_d = int(input("Please write your year of brith \n "))
    print("Thank! Your yaer of brith is %d \n " % birth_d)
   
    res = ""
 
    while birth_d > 0:
        temp = str(birth_d % 2)
        res = temp + res
        birth_d = int(birth_d / 2)
    print("Your year of brith in binary is:")
    print(res)
    print("\n")
except:
    print("Error! Wrong input data!")
 
#36/2 = 18  _0
#18/2 = 9   _0
#9/2 = 4    _1
#4/2 = 2    _0
#2/2 = 1    _0
#1/2 = 0.5  _1
#100100b = 36d
