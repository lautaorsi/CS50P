def main():
    a = shorten(input("Input: "))


def shorten(word):
    r = ""
    for i in word:
        low_i = i.lower()
        if low_i != "a" and low_i != "e" and low_i != "i" and low_i != "o" and low_i != "u":
            r += i
    print(r)
if __name__ == "__main__":
    main()