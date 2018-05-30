print('{0:#^41}\nUse "y"- "yes", "n" - "no"'.format('Preparation cofee'))

ask = ''

if str(input ('Is water in kattle? ')) != 'y' :
    while ask != 'y' :
        ask = str(input ('Put it. Did you put it? '))
ask = ''

if str(input ('Is water in kettle about 100*C? ')) != 'y' :
    while ask != 'y' :
        ask = str(input ('Hot up it. Is water in about 100*C now? '))
        
print('\nPut coffee in a cup')
print('\nAdd boiling water')

if str(input ('\nWould you like some sugar? ')) == 'y' :
    print('\nAdd suagar!')
    
if str(input ('\nWould you like milk in cofee? ')) == 'y' :
    print('\nAdd milk!')
print('\nCofee is ready!')
