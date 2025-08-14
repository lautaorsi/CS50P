import random

while True:
    level = input("Level: ")
    try:
        level = int(level)
    except ValueError:
        continue
    else:
        break
num = int(random.randrange(level + 1))
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if guess == num:
            print("Just right!")
            break
        elif guess < num:
            print("Too small!")
            continue
        elif guess > num:
            print("Too large!")
            continue
        elif guess > level:
            continue

