import random


def main():
    i = 0
    i2=0
    score = 0
    s = get_level()
    while i < 10:
        nums  = generate_integer(s)
        result = nums[0] + nums[1]
        while i2<=3:
            answer = int(input(f"{nums[0]} + {nums[1]} ="))
            if answer != result:
                i2+=1
                if i2 == 3 :
                    print("EEE")
                    print(f"{nums[0]}  +  {nums[1]} = {result}")
                    break
                else:
                    print("EEE")
                    continue
            elif answer == result:
                break
        i2 = 0
        i += 1
        if answer == result:
            score += 1
        continue
    print(f"Score: {score}")

def get_level():
    while True:
        n = input("Level: ")
        try:
            n = int(n)
        except ValueError:
            continue
        else:
            if 1 <= n <= 3:
                return(n)
            else:
                continue


def generate_integer(level):
        if level == 1:
            num1 = random.randrange(0, 10)
            num2 = random.randrange(0, 10)
            return(num1 , num2)
        elif level == 2:
            num1 = random.randrange(10, 100)
            num2 = random.randrange(10, 100)
            return(num1 , num2)
        elif level == 3:
            num1 = random.randrange(100,1000)
            num2 = random.randrange(100,1000)
            return(num1 , num2)



if __name__ == "__main__":
    main()