arr = [5, -15, 9, 2, 1, 32, -40, 3, 9, 45]

maxi = 0  

for i in arr:
    if maxi < i:
       maxi = i
       
assert maxi == max(arr), message        
print(maxi)
      
