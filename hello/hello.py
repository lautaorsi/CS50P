def main():
    name = input("What's your name?")
    print(hello(name))

def hello(to="World"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()