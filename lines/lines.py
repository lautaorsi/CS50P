import sys


def count(fname):
     counter = 0

     file = open(fname, "r")
     for line in file:
          newline = line.strip()
          if len(newline) == 0:
               continue
          else:
               if newline[0] != '#':
                    counter += 1
     print(counter)

def main():
     try:
         x = sys.argv[1]
     except IndexError:
         sys.exit('Too few command-line arguments')

     try:
         x = sys.argv[2]
     except IndexError:
         if ".py" not in sys.argv[1]:
               sys.exit('Not a Python file')
         else:
               try:
                    count(x)
               except FileNotFoundError:
                    sys.exit('File does not exist')
     else:
          sys.exit('Too many command-line arguments')












if __name__ == "__main__":
    main()