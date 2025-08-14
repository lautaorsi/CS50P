while True:
    f = input("Fraction: ").split("/")
    try:
        x= int(f[0])
        y= int(f[1])
        res = x/y
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        if x <= y:
            break
        else:
            continue
def convert(a, b):
     return(round((a/b)*100))
p = convert(x, y)

def gauge(c):
    if c <= 1:
        print("E")
    elif c >= 99:
        print("F")
    else:
        print(f"{p}%")
gauge(p)