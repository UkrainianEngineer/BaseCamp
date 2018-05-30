#check int
try:
    inp_num = int(input("Write binary num: \n"))
except:
    print("Wrong num!")

st = str(inp_num) #input number
le = len(st) #lenght of input number it need for culc.

i = 0 #count var whole num
res = 0 #var of result

while i <((len(st))) : #expression
    k = 0 #count var diff num
    temp = (int(st[i])) #take num
    if temp == 0 or temp == 1 : #check num for bin
        while k < ((len(st)) - i - 1) : #expression
            temp = temp* 2 #mull
            k = k+1 #count iter
            #print(temp)
        
        res = res + temp #calc result
        i = i + 1
    else:
        print("Only '1' and '0'!")
        res = 0
        break
print(res) #output



