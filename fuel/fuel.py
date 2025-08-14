i = 0
while i == 0 :
    f = input("Fraction: ").split("/")
    try:
        x= int(f[0])
        y= int(f[1])
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        if x <= y:
            break
        else:
            continue
p = round((x/y)*100)
if p <= 1:
    print("E")
elif p >= 99:
        print("F")
else:
        print(f"{p}%")
