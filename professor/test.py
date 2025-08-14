import random

level = int(input(""))
i = 0
if level == 1:
    num1 = random.randrange(0, 10)
    num2 = random.randrange(0, 10)
    i += 1
elif level == 2:
    num1 = random.randrange(10, 100)
    num2 = random.randrange(10, 100)
    i += 1
elif level == 3:
    num1 = random.randrange(100,1000)
    num2 = random.randrange(100,1000)
    i += 1

print( num1 , num2)