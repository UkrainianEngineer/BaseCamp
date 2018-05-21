import random
b=random.randint(1, 9)
a = 0
while a < 100 :
    b=random.randint(1, 9)
    print(b)
    b = random.gauss(1, 1)
    print(b)
    random.lognormvariate(2, 3)
    print(b)
    a = a + 5
    
