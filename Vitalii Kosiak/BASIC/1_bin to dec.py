try:
    inp_num = int(input("Write binary num: \n"))
except:
    print("Wrong num")

st = str(inp_num)
le = len(st) #довжина

i = 0
res = 0
while i <((len(st))) :
    k = 0
    temp = (int(st[i]))
    if temp == 0 | temp == 1 :
        while k < ((len(st)) - i - 1) :
            temp = temp* 2
            k = k+1
            #print(temp)
        
        res = res + temp
        i = i + 1
    else:
        print("Only '1' and '0'")
        res = 0
        break
print(res)



