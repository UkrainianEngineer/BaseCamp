import sys
import random

arr = []

def rand_arr() :
    i = 0
    while i < random.randint(10, 20) :
        arr.append(random.randint(1, 100))
        i+=1

def err_and_out() :
    if input() == '' :
        sys.exit(1)
    else :
        sys.exit(1)

answ = input('Do you want me to create new random array? Enter "y" -> yes, "n" -> no. \n')

if answ == 'y' :
    print('I\'m creating it. \n')
    rand_arr()
elif answ == 'n' :
    print('I won\'t create it. Enter any key for exit.')
    err_and_out()
    
else :
    print('"y" - new array "x" or any key - close program')
    if input() == 'y' :
        rand_arr()
    else :
        sys.exit(1)

print('Our array is: ' + str(arr))
print('Our array contain ' + str(len(arr)) + ' num')
####################################################################
try :
    bs = int(input('Enter num for begin of slicing: '))
except :
    print('Wrong num! Enter any key for exit.')
    err_and_out()
print('First num of slicing is ' + str(bs))
####################################################################    
try :
    es = int(input('Enter num for end of slicing: '))
except :
    print('Wrong num! Enter any key for exit.')
    err_and_out()
print('Second num of slicing is ' + str(es))
#################################################################### 
if bs < len(arr) or es < len(arr) or bs <= 0 or es <= 0 :
    pass
else :
    print('Wrong num! Num is out of arr!')

sume = sum(arr[bs:es])

print('The sum is {}.'.format(sume))
