menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
i = 0
t = 0
while i == 0:
    try:
        s = input("Item: ").lower().title()
        for item in menu:
            if s == item:
                t += float(menu[s])
                print("$" + format(t, '.2f'))
    except EOFError:
        break

