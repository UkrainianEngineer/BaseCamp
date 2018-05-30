import random

print("HI, i'm going to create rand array and calc. its param")

data = []

for i in range(1,random.randint(10,20)) :
    data.append(random.randint(1,99))

print('Array are: ' + str(data))

max_numb = data[0]
min_numb = data[0]
summ = 0
#max
for i in data :
    if max_numb < i :
        max_numb = i

print('MAX = '+ str(max(data)))

#min
for i in data :
    if min_numb > i :
        min_numb = i
#summ        
for i in data :
    summ += i
#average
average = summ / len(data)
 
print('Min num is: ' + str(min_numb) +'\n'+ 'Max num is: ' + str(max_numb))
print('Summ of nums is: ' + str(summ) +'\n'+ 'Average is: ' + str(round(average,2)))    
