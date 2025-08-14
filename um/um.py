import re
import sys


def main():
    print(count(input("Text: ")))





def count(s):
    cnt = 0
    lista = s.split()
    for i in lista:
        if re.search(r"^[\.|,|\s]*um[\.|,|\|?|!]*$", i, re.IGNORECASE):
            cnt += 1
    return(cnt)








if __name__ == "__main__":
    main()