t = 0
while t < 50:
    A_due = 50 - t
    print("Amount due: " , A_due )
    v = int(input("Insert coin: "))
    if v == 25 or v == 10 or v ==  5:
        t += v
print("Change owed: " , -(A_due-v))