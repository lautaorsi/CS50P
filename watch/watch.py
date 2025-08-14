import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"(https?://)?(www\.)?youtube\.com/embed/", s):
        ns = s.split('src=')
        if len(ns) == 1:
            return(None)
        else:
            ns = ns[1].split('/')
            ns = ns[-2].split('"')
            return(f'https://youtu.be/{ns[0]}')
    else:
        return(None)







if __name__ == "__main__":
    main()