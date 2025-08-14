list = {}
while True :
    try:
        s = input("").lower()

    except EOFError:
        break
    if s in list:
        list[s] += 1
    else:
        list[s] = 1
print("\n")
for item in sorted(list):
    print(list[item], item.upper())
