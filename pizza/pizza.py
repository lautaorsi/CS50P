import sys
from tabulate import tabulate


def core(x):
    table = []
    file = open(x, "r")
    for line in file:
        table.append(line.split(','))
    headers = table[0]
    headers[len(headers)-1] = (headers[len(headers)-1]).replace('\n', '')
    del table[0]


    print (tabulate(table, headers, tablefmt="grid"))

def main():
    try:
         x = sys.argv[1]
    except IndexError:
         sys.exit('Too few command-line arguments')

    try:
         x = sys.argv[2]
    except IndexError:
         if ".csv" not in sys.argv[1]:
               sys.exit('Not a CSV file')
         else:
               try:
                    core(x)
               except FileNotFoundError:
                    sys.exit('File does not exist')
    else:
          sys.exit('Too many command-line arguments')















if __name__ == "__main__":
    main()


