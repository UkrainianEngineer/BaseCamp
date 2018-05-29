import random
print('Enter "x" if you want to exit!')
while True :   
    a = random.randint(0, 9)
    a1 = random.randint(0, 9)
    b = input(str('Вгадай число: '))
    c = ['0','1','2','3','4','5','6','7','8','9','x']   
    if b == str(a) or b == str(a1) :
        print ('Вірно!' + 'Числа були ' + str(a) + ' i ' + str(a1))
    elif b == 'x':
        print('exit')
        break
    elif b not in c :
        print ('Тільки цифри!')    
    else:
        print('Не вірно! ' + 'Числа були ' + str(a) + ' i ' + str(a1) )
