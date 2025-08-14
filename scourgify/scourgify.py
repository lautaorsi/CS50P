import sys
from tabulate import tabulate



def out(x, y):
    rfile = open(x, 'r')
    table = []
    for line in rfile:
            nline = line.split(',')
            nline[0] = nline[0].replace('"','')
            nline[1] = nline[1].replace('"','')
            nline[len(nline)-1] = (nline[len(nline)-1]).replace('\n', '')
            lst = nline[0]
            fst = nline[1]
            nline[1] = lst.replace(' ', '')
            nline[0] = fst.replace(' ', '')
            table.append(nline)
    del table[0]
    nfile = open(y, 'w')
    nfile.write('first,last,house\n')
    for i in table:
         line = f'{i[0]},{i[1]},{i[2]}\n'
         nfile.write(line)


def main():
    try:
         x = sys.argv[1]
         y = sys.argv[2]

    except IndexError:
         sys.exit('Too few command-line arguments')

    try:
         x = sys.argv[3]
         y = sys.argv[2]
    except IndexError:
         if ".csv" not in sys.argv[1]:
               sys.exit('Not a CSV file')
         else:
               try:
                    out(x, y)
               except FileNotFoundError:
                    sys.exit('File does not exist')
    else:
          sys.exit('Too many command-line arguments')


if __name__ == "__main__":
    main()
